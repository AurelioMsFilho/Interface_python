from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import sys
class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Definindo um titulo para a janela
        self.setGeometry(500, 500, 900, 720) # Definindo o Tamanho da janela
        self.setWindowIcon(QIcon('/home/aurelio/Imagens/6c1e5af3b28948b4ef2219e4f84ebc25.jpg'))
        self.Interface()

    def Interface(self):
        texto1 = QLabel('Olá Mundo!!!', self)
        texto1.resize(250, 250)
        texto1.move(100, 5)

        botao1 = QPushButton('Sair', self)
        botao1.move(100, 200)
        botao1.clicked.connect(self.sair)



        texto2 = QLabel('Aurélio Filho', self)
        texto2.resize(250, 250)
        texto2.move(200, 5)



    def sair(self):
        sys.exit(qt.exec())


        self.show()


qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
