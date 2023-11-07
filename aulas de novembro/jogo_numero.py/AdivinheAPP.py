from MainMenu import *
from AdivinheNumero import *
class AdivinheAPP(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenu(name='main_menu'))
        screen_manager.add_widget(AdivinheNumero(name='game'))
        return screen_manager


if __name__ == '__main__':
    AdivinheAPP().run()