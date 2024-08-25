import pygame as pg
import magic_ball
from setting import*


class Player_2(pg.sprite.Sprite):
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
        self.priset = False
        self.spisok_prisest_r = []
        self.spisok_prisest_l = []
        self.spisok_attaka_r = []
        self.spisok_attaka_l = []

        self.magic_ball_r = load_image("images/lightning wizard/magicball.png", 100, 200)
        self.magic_ball_l = pg.transform.flip(self.magic_ball_r, True, False)
        self.spisok_magic_ball = []

        self.zdorovie = 200
        self.zarad = 0
        self.attaka = False
        self.vremia_attacka = 0

        self.image = load_image("images/lightning wizard/idle1.png", 300, 450)
        self.igra = igra

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH-170, SCREEN_HEIGHT // 2)
        self.upload()
        self.hitbox = pg.Rect([0, 0], [self.rect.width // 2, self.rect.height // 2])
        self.upload()

    def draw(self):
        self.igra.screen.blit(self.image, self.rect)
        if self.zarad > 0:
            pg.draw.rect(self.igra.screen, [0, 0, 0], [self.rect.x+30, self.rect.y, 250, 30], 5)
            pg.draw.rect(self.igra.screen, [255, 0, 0], [self.rect.x+35, self.rect.y+5, self.zarad, 20])
        pg.draw.rect(self.igra.screen, [255, 0, 0], [SCREEN_WIDTH-270, 480, 200, 30], 5)
        pg.draw.rect(self.igra.screen,[255, 0, 0], [SCREEN_WIDTH-270, 480, self.zdorovie, 30])
        pg.draw.rect(self.igra.screen, [0, 0, 0], self.hitbox, 5)
        for m_b in self.spisok_magic_ball:
            m_b.draw()

    def dvishenie(self):
        self.priset = False
        mish = pg.mouse.get_pressed()
        a = pg.key.get_pressed()
        if self.attaka == False:
            self.spisok_animatoin = self.spisok_dixanie_r if self.napravlenie == 1 else self.spisok_dixanie_l
        if a[pg.K_LEFT] is True:
            self.napravlenie = -1
            self.rect.x = self.rect.x - 2
            self.spisok_animatoin = self.spisok_xodit_l
        elif a[pg.K_RIGHT] is True:
            self.napravlenie = 1
            self.spisok_animatoin = self.spisok_xodit_r
            self.rect.x = self.rect.x + 2
        elif a[pg.K_RSHIFT] is True:
            self.priset = True
            self.spisok_animatoin = self.spisok_prisest_r if self.napravlenie == 1 else self.spisok_prisest_l
        elif mish[2] is True and self.attaka == False:
            self.spisok_animatoin = self.spisok_zarad_r if self.napravlenie == 1 else self.spisok_zarad_l
            self.zarad = self.zarad+1
            if self.zarad == 240:
                magic_ball_pic = self.magic_ball_r if self.napravlenie == 1 else self.magic_ball_l
                m_b = magic_ball.Magicball(magic_ball_pic, self.rect.x + 215, self.rect.y + 95, self.napravlenie*5, self.igra, self.zarad // 3)
                self.spisok_magic_ball.append(m_b)
                self.spisok_animatoin = self.spisok_attaka_r if self.napravlenie == 1 else self.spisok_attaka_l
                self.vremia_attacka = pg.time.get_ticks()
                self.attaka = True
                self.zarad = 0
        elif mish[2] is False and self.zarad >= 40:
            magic_ball_pic = self.magic_ball_r if self.napravlenie == 1 else self.magic_ball_l
            m_b = magic_ball.Magicball(magic_ball_pic, self.rect.x + 215, self.rect.y + 95, self.napravlenie*5, self.igra, self.zarad // 3)
            self.spisok_magic_ball.append(m_b)
            self.attaka = True
            self.spisok_animatoin = self.spisok_attaka_r if self.napravlenie == 1 else self.spisok_attaka_l
            self.vremia_attacka = pg.time.get_ticks()
            self.attaka = True
            self.zarad = 0

        if pg.time.get_ticks() - self.vremia_attacka >= 1500:
            self.attaka = False

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
            r = load_image("images/lightning wizard/idle" + str(a) + ".png", 300, 450)
            for b in range(1, 20):
                self.spisok_dixanie_r.append(r)
            l = pg.transform.flip(r, True, False)
            for c in range(1, 20):
                self.spisok_dixanie_l.append(l)
        for b in range(1, 5):
            r = load_image("images/lightning wizard/move" + str(b) + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_xodit_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_xodit_l.append(l)
        for b in range(1):
            r = load_image("images/lightning wizard/down" + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_prisest_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_prisest_l.append(l)
        for b in range(1):
            r = load_image("images/lightning wizard/charge" + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_zarad_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_zarad_l.append(l)
        for b in range(1):
            r = load_image("images/lightning wizard/attack" + ".png", 300, 450)
            for n in range (1, 10):
                self.spisok_attaka_r.append(r)
            l = pg.transform.flip(r, True, False)
            for m in range (1, 10):
                self.spisok_attaka_l.append(l)
