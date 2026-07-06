import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

from PyQt6.QtCore import Qt

from checkout import TelaCheckout
from cadastro_produto import TelaCadastroProduto


class TelaCPF(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Terminal Autoatendimento")
        self.setGeometry(300, 100, 800, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1b2e;
            }

            QLabel {
                color: white;
            }

            QLineEdit {
                padding: 15px;
                border: 2px solid #444;
                border-radius: 8px;
                background-color: #2b2640;
                color: white;
                font-size: 16px;
            }

            QPushButton {
                padding: 15px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(20)

        titulo = QLabel("Terminal Autoatendimento")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: #4ade80;
        """)

        subtitulo = QLabel(
            "Deseja incluir CPF na nota fiscal?"
        )

        subtitulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        subtitulo.setStyleSheet("""
            font-size: 20px;
        """)

        self.input_cpf = QLineEdit()
        self.input_cpf.setPlaceholderText(
            "000.000.000-00"
        )

        btn_confirmar = QPushButton(
            "Confirmar CPF"
        )

        btn_confirmar.setStyleSheet("""
            background-color: #67e8f9;
            color: black;
        """)

        btn_confirmar.clicked.connect(
            self.abrir_checkout
        )

        btn_sem_cpf = QPushButton(
            "Continuar sem CPF"
        )

        btn_sem_cpf.setStyleSheet("""
            background-color: #3f3f46;
            color: white;
        """)

        btn_sem_cpf.clicked.connect(
            self.abrir_checkout
        )

        btn_admin = QPushButton(
            "Área Administrativa"
        )

        btn_admin.setStyleSheet("""
            background-color: #facc15;
            color: black;
        """)

        btn_admin.clicked.connect(
            self.abrir_admin
        )

        layout.addStretch()

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)
        layout.addWidget(self.input_cpf)

        layout.addWidget(btn_confirmar)
        layout.addWidget(btn_sem_cpf)
        layout.addWidget(btn_admin)

        layout.addStretch()

        self.setLayout(layout)

    def abrir_checkout(self):
        self.checkout = TelaCheckout()
        self.checkout.show()
        self.close()

    def abrir_admin(self):
        self.admin = TelaCadastroProduto()
        self.admin.show()

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    janela = TelaCPF()
    janela.show()

    sys.exit(app.exec()) 