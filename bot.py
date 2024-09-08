from typing import Any
import pygame as pg
from setting import* 
import magic_ball
import random


class Bot(pg.sprite.Sprite):
    def __init__(self, igra):
        super().__init__()

        self.spisok_zarad_r = []
        self.spisok_zarad_l = []
        self.spisok_dixanie_r = []
        self.spisok_dixanie_l = []
        self.spisok_xodit_r = []
        self.spisok_xodit_l = []
        self.spisok_animatoin = self.spisok_dixanie_r
        self.a = 0
        self.napravlenie = -1
        self.spisok_prisest_r = []
        self.spisok_prisest_l = []
        self.spisok_attaka_r = []
        self.spisok_attaka_l = []
        self.priset = False
        self.igra = igra

        self.magic_ball_l = load_image("images/" + self.igra.mag_pic2 + "/magicball.png", 100, 200)
        self.magic_ball_r = pg.transform.flip(self.magic_ball_l, True, False)
        self.spisok_magic_ball = []

        self.zdorovie = 200
        self.zarad = 0
        self.attaka = False
        self.vremia_attacka = 0
        self.xodit = False
        self.rustoyanie = 0

        self.image = load_image("images/" + self.igra.mag_pic2 + "/idle1.png", 300, 450)

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH-170, SCREEN_HEIGHT // 2)
        self.upload()
        self.hitbox = pg.Rect([0, 0], [self.rect.width // 2, self.rect.height // 2])

    def draw(self):
        self.igra.screen.blit(self.image, self.rect)
        if self.zarad > 0:
            pg.draw.rect(self.igra.screen, [0, 0, 0], [self.rect.x+30, self.rect.y, 250, 30], 5)
            pg.draw.rect(self.igra.screen, [255, 0, 0], [self.rect.x+35, self.rect.y+5, self.zarad, 20])
        pg.draw.rect(self.igra.screen, [255, 0, 0], [SCREEN_WIDTH-270, 480, 200, 30], 5)
        pg.draw.rect(self.igra.screen,[255, 0, 0], [SCREEN_WIDTH-270, 480, self.zdorovie, 30])
        for m_b in self.spisok_magic_ball:
            m_b.draw()

    def dvishenie(self):
        mish = pg.mouse.get_pressed()
        a = pg.key.get_pressed()
        self.priset = False
        if self.attaka == False:
            self.spisok_animatoin = self.spisok_dixanie_r if self.napravlenie == 1 else self.spisok_dixanie_l
        for m_b in self.igra.player_1.spisok_magic_ball:
            if abs(m_b.hitbox.centerx - self.hitbox.centerx) < 200 and m_b.yvorot != 1 and self.attaka == False:
                self.priset = True
                self.spisok_animatoin = self.spisok_prisest_r if self.napravlenie == 1 else self.spisok_prisest_l
        if random.randint(1, 1200) < 5 and self.attaka is False and self.xodit == False:
            if self.igra.player_1.rect.centerx < self.rect.centerx:
                self.napravlenie = -1
            else:
                self.napravlenie = 1
            self.attaka = True
            m_b_pic = self.magic_ball_r if self.napravlenie == 1 else self.magic_ball_l
            if self.napravlenie == -1:
                m_b = magic_ball.Magicball(m_b_pic, self.rect.x - 50, self.rect.y + 95, self.napravlenie*10, self.igra, random.randint(40, 80))
            else:
                m_b = magic_ball.Magicball(m_b_pic, self.rect.x + 215, self.rect.y + 95, self.napravlenie*10, self.igra, random.randint(40, 80))
            self.spisok_magic_ball.append(m_b)
            self.vremia_attacka = pg.time.get_ticks()
        if self.attaka is True:
            if self.igra.player_1.rect.centerx < self.rect.centerx:
                self.napravlenie = -1
            else:
                self.napravlenie = 1
            self.spisok_animatoin = self.spisok_attaka_r if self.napravlenie == 1 else self.spisok_attaka_l
            if pg.time.get_ticks() - self.vremia_attacka >= 1500:
                self.attaka = False
        if random.randint(1, 1000) < 5 and self.priset is False and self.xodit is False:
            self.xodit = True
            self.napravlenie = (-1) ** random.randint(0, 1)
            self.rustoyanie = random.randint(50, 300)
        if self.xodit is True:
            self.spisok_animatoin = self.spisok_xodit_r if self.napravlenie == 1 else self.spisok_xodit_l
            self.rect.x = self.rect.x + self.napravlenie*2
            self.rustoyanie = self.rustoyanie - 2
            if self.rustoyanie <= 0:
                self.xodit = False
            if self.rect.right >= 900 and self.napravlenie == 1:
                self.xodit = False
            elif self.rect.x <= 0 and self.napravlenie == -1:
                self.xodit = False

    def animation(self):
        if self.a < len(self.spisok_animatoin):
            self.image = self.spisok_animatoin[self.a]
            self.a = self.a + 1
        else:
            self.a = 0

    def update(self):
        self.dvishenie()
        self.animation()
        for m_b in self.spisok_magic_ball:
            m_b.dvishenie()
        self.hitbox.center = self.rect.center

    def upload(self):
        for a in range(1, 4):
            r = load_image("images/" + self.igra.mag_pic2 + "/idle" + str(a) + ".png", 300, 450)
            for b in range(1, 20):
                self.spisok_dixanie_r.append(r)
            l = pg.transform.flip(r, True, False)
            for c in range(1, 20):
                self.spisok_dixanie_l.append(l)
        for b in range(1, 5):
            r = load_image("images/" + self.igra.mag_pic2 + "/move" + str(b) + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_xodit_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_xodit_l.append(l)
        for b in range(1):
            r = load_image("images/" + self.igra.mag_pic2 + "/down" + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_prisest_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_prisest_l.append(l)
        for b in range(1):
            r = load_image("images/" + self.igra.mag_pic2 + "/charge" + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_zarad_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_zarad_l.append(l)
        for b in range(1):
            r = load_image("images/" + self.igra.mag_pic2 + "/attack" + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_attaka_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_attaka_l.append(l)
