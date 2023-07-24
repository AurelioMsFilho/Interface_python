from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import sys
import pro
class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Meu Programa') # Definindo um titulo para a janela
        self.setGeometry(500, 500, 900, 720) # Definindo o Tamanho da janela
        self.setWindowIcon(QIcon('/home/aurelio/Imagens/6c1e5af3b28948b4ef2219e4f84ebc25.jpg'))
        self.Interface()

        #self.show()# tenho que ver o codigo completo
    def Interface(self):
        texto1 = QLabel('Login', self)
        texto1.move(40, 50)

        botao1 = QPushButton('Sair'.upper(), self)
        botao1.move(100, 200)
        botao1.clicked.connect(self.sair)

        self.caixa_texto1 = QLineEdit(self)
        self.caixa_texto1.setPlaceholderText('Digite seu nome de usuário')
        self.caixa_texto1.move(90, 48)

        texto2 = QLabel('Senha: ', self)
        texto2.move(40, 75)

        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.setPlaceholderText('Digite sua senha')
        self.caixa_texto2.setEchoMode(QLineEdit.EchoMode.Password)
        self.caixa_texto2.move(90, 72)

        botao2 = QPushButton('Entrar', self)
        botao2.clicked.connect(self.salva_dados)
        botao2.move(117, 98)

        self.show()# tenho que ver o codigo completo
    def sair(self):
        sys.exit(qt.exec())

    def salva_dados(self):
        base = []
        base.append(self.caixa_texto1.text())
        base.append(self.caixa_texto2.text())
        print(base)

    # def Invertido(self):
    #     self.texto1.setText('!!!odnum álO'.upper())

qt = QApplication(sys.argv)
app = JanelaPrincipal()
sys.exit(qt.exec())
