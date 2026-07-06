from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

from database import conectar


class TelaCadastroProduto(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(300, 100, 600, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1b2e;
                color: white;
            }
                           
            QHeaderView::section {
                background-color: #f5f5f5;
                color: black;
                padding: 6px;
                font-weight: bold;
                 }               

            QLineEdit {
                padding: 10px;
                border-radius: 8px;
                background-color: #2b2640;
                color: white;
                font-size: 16px;
            }

            QPushButton {
                padding: 12px;
                border-radius: 8px;
                background-color: #4ade80;
                color: black;
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()

        titulo = QLabel("Cadastro de Produtos")
        titulo.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código de Barras")

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome do Produto")

        self.preco = QLineEdit()
        self.preco.setPlaceholderText("Preço")

        self.estoque = QLineEdit()
        self.estoque.setPlaceholderText("Estoque")

        btn = QPushButton("Cadastrar Produto")
        btn.clicked.connect(self.cadastrar_produto)

        layout.addWidget(titulo)
        layout.addWidget(self.codigo)
        layout.addWidget(self.nome)
        layout.addWidget(self.preco)
        layout.addWidget(self.estoque)
        layout.addWidget(btn)

        self.setLayout(layout)

    def cadastrar_produto(self):
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO produtos
                (codigo_barras, nome, preco, estoque)
                VALUES (%s, %s, %s, %s)
            """, (
                self.codigo.text(),
                self.nome.text(),
                float(self.preco.text()),
                int(self.estoque.text())
            ))

            conn.commit()

            QMessageBox.information(
                self,
                "Sucesso",
                "Produto cadastrado com sucesso!"
            )

            self.codigo.clear()
            self.nome.clear()
            self.preco.clear()
            self.estoque.clear()

            cursor.close()
            conn.close()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Erro",
                str(e)
            )