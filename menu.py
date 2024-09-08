import pygame_menu
import pygame as pg
import pygame_menu.events
from setting import*
import main


class Menu:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Битва магов")
        self.menu = pygame_menu.Menu(title="Битва Магов", theme=pygame_menu.themes.THEME_DARK,width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.menu.add.label("Режим 2 игрока")
        self.menu.add.selector("Левый игрок:", [("Маг огня", 1), ("Маг молний", 2), ("Монах земли", 3)], onchange=self.mag)
        self.menu.add.selector("Правый игрок:", [("Маг огня", 1), ("Маг молний", 2), ("Монах земли", 3)], onchange=self.mag2)
        self.menu.add.button("Играть", action=self.play)
        self.menu.add.label("Режим с ботом")
        self.menu.add.selector("Противник:", [("Маг огня", 1), ("Маг молний", 2), ("Мона земли", 3)], onchange=self.mag3)
        self.menu.add.button("Играть", action=self.play2)
        self.menu.add.button("Выйти из игры", action=pygame_menu.events.EXIT)
        self.player1 = 1
        self.player2 = 1
        self.menu.mainloop(self.screen)

    def difficulty(self, info, number):
        print(info)
        print(number)

    def mag(self, info, number):
        self.player1 = number

    def mag2(self, info, number):
        self.player2 = number

    def mag3(self, info, number):
        self.player2 = number

    def play(self):
        game = main.Game(1, self.player1, self.player2)

    def play2(self):
        game = main.Game(2, self.player1, self.player2)

menu = Menu()
