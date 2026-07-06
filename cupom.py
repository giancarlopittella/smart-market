import os
import sys

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)

from PyQt6.QtCore import Qt


class TelaCupom(QWidget):

    def __init__(self, total, forma_pagamento, itens):
        super().__init__()

        self.setWindowTitle("Cupom Fiscal")
        self.setGeometry(400, 100, 450, 600)

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
            }

            QTextEdit {
                background-color: white;
                font-size: 16px;
                border: none;
                padding: 15px;
            }

            QPushButton {
                padding: 15px;
                background-color: #4ade80;
                color: black;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
            }

            QPushButton:hover {
                background-color: #22c55e;
            }
        """)

        layout = QVBoxLayout()

        titulo = QLabel("MERCADO")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)

        cupom = QTextEdit()
        cupom.setReadOnly(True)

        texto = "=========== CUPOM FISCAL ===========\n\n"

        for item in itens:
            texto += (
                f'{item["nome"]}\n'
                f'Qtd: {item["quantidade"]}    '
                f'R$ {item["preco"]:.2f}\n\n'
            )

        texto += f"""
-----------------------------------

TOTAL: R$ {total:.2f}

Forma de Pagamento:
{forma_pagamento}

Obrigado pela preferência!

Volte Sempre!
"""

        cupom.setText(texto)

        btn_finalizar = QPushButton("🖨️ Imprimir Cupom")
        btn_finalizar.clicked.connect(self.nova_compra)

        layout.addWidget(titulo)
        layout.addWidget(cupom)
        layout.addWidget(btn_finalizar)

        self.setLayout(layout)

    def nova_compra(self):
        os.execl(sys.executable, sys.executable, *sys.argv)