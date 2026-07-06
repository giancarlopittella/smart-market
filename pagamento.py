from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox
)

from PyQt6.QtCore import Qt

from database import conectar
from cupom import TelaCupom


class TelaPagamento(QWidget):
    def __init__(self, total, itens_compra, cpf=""):
        super().__init__()

        self.total = total
        self.itens_compra = itens_compra
        self.cpf = cpf

        self.setWindowTitle("Pagamento")
        self.setGeometry(300, 100, 700, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1b2e;
                color: white;
            }

            QPushButton {
                padding: 20px;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()

        titulo = QLabel("Forma de Pagamento")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 30px;
            color: #4ade80;
            font-weight: bold;
        """)

        valor = QLabel(f"TOTAL: R$ {self.total:.2f}")
        valor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        valor.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)

        btn_pix = QPushButton("PIX")
        btn_cartao = QPushButton("CARTÃO")
        btn_dinheiro = QPushButton("DINHEIRO")

        btn_pix.clicked.connect(
            lambda: self.finalizar("PIX")
        )

        btn_cartao.clicked.connect(
            lambda: self.finalizar("CARTÃO")
        )

        btn_dinheiro.clicked.connect(
            lambda: self.finalizar("DINHEIRO")
        )

        layout.addWidget(titulo)
        layout.addWidget(valor)
        layout.addWidget(btn_pix)
        layout.addWidget(btn_cartao)
        layout.addWidget(btn_dinheiro)

        self.setLayout(layout)

    def finalizar(self, forma_pagamento):

        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO vendas
                (cpf, forma_pagamento, total)
                VALUES (%s, %s, %s)
                RETURNING id
            """, (
                self.cpf,
                forma_pagamento,
                self.total
            ))

            venda_id = cursor.fetchone()[0]

            for item in self.itens_compra:

                cursor.execute("""
                    INSERT INTO itens_venda
                    (
                        venda_id,
                        produto_id,
                        quantidade,
                        preco_unitario
                    )
                    VALUES (%s, %s, %s, %s)
                """, (
                    venda_id,
                    item["produto_id"],
                    item["quantidade"],
                    item["preco"]
                ))

            conn.commit()

            cursor.close()
            conn.close()

            self.cupom = TelaCupom(
                self.total,
                forma_pagamento,
                self.itens_compra
            )

            self.cupom.show()
            self.hide()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Erro",
                str(e)
            )