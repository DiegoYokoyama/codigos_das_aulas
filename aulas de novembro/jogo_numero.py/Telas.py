from Menu import *
from AcerteONumero import *
class Telas(App):
    def build(self):
        gerenciar_tela = ScreenManager()
        gerenciar_tela.add_widget(Menu(name='menu_principal'))
        gerenciar_tela.add_widget(AcerteONumero(name='game'))
        return gerenciar_tela


if __name__ == '__main__':
    Telas().run()