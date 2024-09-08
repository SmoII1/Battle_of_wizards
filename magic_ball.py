import pygame as pg
from setting import*
import plaeyr
import random


class Magicball:

    def __init__(self, kartinka, x, y, skorost, igra, moshnost):
        self.moshnost = moshnost
        self.kartinka = kartinka
        self.igra = igra
        self.skorost = skorost
        self.yvorot = random.randint(1, 4)
        self.rect = pg.Rect([x, y], self.kartinka.get_size())
        self.hitbox = pg.Rect([0, 0], [self.rect.width // 2, self.rect.height // 2])

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.rect)

    def dvishenie(self):
        self.rect.x = self.rect.x + self.skorost
        self.hitbox.center = self.rect.center
