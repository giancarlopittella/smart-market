import sys
import tela_inicio

from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)

janela = tela_inicio.TelaCPF()
janela.show()

sys.exit(app.exec())