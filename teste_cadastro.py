import sys

from PyQt6.QtWidgets import QApplication
from cadastro_produto import TelaCadastroProduto

app = QApplication(sys.argv)

janela = TelaCadastroProduto()
janela.show()

sys.exit(app.exec())