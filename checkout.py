import pygame

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QAbstractItemView,
    QHeaderView
)

from PyQt6.QtCore import Qt

from pagamento import TelaPagamento
from database import conectar


class TelaCheckout(QWidget):
    def __init__(self):
        super().__init__()

        pygame.mixer.init()

        self.setWindowTitle("Terminal Autoatendimento")
        self.setGeometry(300, 100, 1000, 600)

        self.total_compra = 0
        self.itens_compra = []
        self.linhas_produtos = {}

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1b2e;
                color: white;
            }

            QLineEdit {
                padding: 10px;
                border-radius: 8px;
                background-color: #2b2640;
                color: white;
                font-size: 16px;
            }

            QPushButton {
                padding: 10px;
                border-radius: 8px;
                background-color: #4ade80;
                color: black;
                font-weight: bold;
            }

            QTableWidget {
                background-color: #2b2640;
                color: white;
                font-size: 15px;
                gridline-color: #444
            }
                           
            QHeaderView::section {
                background-color: #4ade80;
                color: black;
                font-weight: bold;
                font-size: 14px;
                padding: 8px;
                border: none;           
            }

            QTableCornerButton::section {
                background-color: #4ade80;
                border: none;           
            }                              
        """)

        layout = QVBoxLayout()

        titulo = QLabel("Terminal Autoatendimento")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo.setStyleSheet("""
            font-size: 28px;
            color: #4ade80;
            font-weight: bold;
        """)

        self.codigo_input = QLineEdit()
        self.codigo_input.setPlaceholderText(
            "Digite ou bip o código de barras"
        )

        self.codigo_input.returnPressed.connect(
            self.bipar_produto
        )

        btn_bipar = QPushButton("Bipar Produto")
        btn_bipar.clicked.connect(self.bipar_produto)

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(3)

        self.tabela.setHorizontalHeaderLabels([
            "Produto",
            "Quantidade",
            "Preço"
        ])

        # REMOVE PERMISSAO DE EDITAR
        self.tabela.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.tabela.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.tabela.setSelectionMode(
            QAbstractItemView.SelectionMode.NoSelection
        )

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.total = QLabel("TOTAL: R$ 0,00")

        self.total.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)

        btn_finalizar = QPushButton(
            "Finalizar Compra"
        )

        btn_finalizar.clicked.connect(
            self.abrir_pagamento
        )

        layout.addWidget(titulo)
        layout.addWidget(self.codigo_input)
        layout.addWidget(btn_bipar)
        layout.addWidget(self.tabela)
        layout.addWidget(self.total)
        layout.addWidget(btn_finalizar)

        self.setLayout(layout)

    def bipar_produto(self):

        codigo = self.codigo_input.text().strip()

        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id, nome, preco
                FROM produtos
                WHERE codigo_barras = %s
            """, (codigo,))

            produto = cursor.fetchone()

            if produto:

                produto_id = produto[0]
                nome = produto[1]
                preco = float(produto[2])

                try:
                    pygame.mixer.music.load(
                        "assets/beep.mp3"
                    )
                    pygame.mixer.music.play()
                except:
                    pass

                if produto_id in self.linhas_produtos:

                    linha = self.linhas_produtos[produto_id]

                    quantidade = int(
                        self.tabela.item(linha, 1).text()
                    ) + 1

                    self.tabela.setItem(
                        linha,
                        1,
                        QTableWidgetItem(str(quantidade))
                    )

                    self.tabela.setItem(
                        linha,
                        2,
                        QTableWidgetItem(
                            f"R$ {preco * quantidade:.2f}"
                        )
                    )

                    for item in self.itens_compra:

                        if item["produto_id"] == produto_id:

                            item["quantidade"] += 1

                            break

                else:

                    linha = self.tabela.rowCount()

                    self.tabela.insertRow(linha)

                    self.linhas_produtos[produto_id] = linha

                    self.tabela.setItem(
                        linha,
                        0,
                        QTableWidgetItem(nome)
                    )

                    self.tabela.setItem(
                        linha,
                        1,
                        QTableWidgetItem("1")
                    )

                    self.tabela.setItem(
                        linha,
                        2,
                        QTableWidgetItem(
                            f"R$ {preco:.2f}"
                        )
                    )

                    self.itens_compra.append({
                        "produto_id": produto_id,
                        "nome": nome,
                        "preco": preco,
                        "quantidade": 1
                    })

                self.total_compra += preco

                self.total.setText(
                    f"TOTAL: R$ {self.total_compra:.2f}"
                )                

            else:

                QMessageBox.warning(
                    self,
                    "Produto não encontrado",
                    "Código de barras inválido."
                )

            cursor.close()
            conn.close()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Erro",
                str(e)
            )

        self.codigo_input.clear()

    def abrir_pagamento(self):

        if self.total_compra == 0:

            QMessageBox.warning(
                self,
                "Carrinho vazio",
                "Adicione pelo menos um produto."
            )

            return

        self.pagamento = TelaPagamento(
            self.total_compra,
            self.itens_compra
        )

        self.pagamento.show()