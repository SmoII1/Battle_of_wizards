import pygame as pg
from setting import*
import plaeyr
import bot
import player_2
import pygame.freetype

pg.init()
shrift = pygame.freetype.Font("shrift.otf", 25)


class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Битва магов")

        self.background = load_image("images/background.png", SCREEN_WIDTH, SCREEN_HEIGHT)

        self.player_1 = plaeyr.Player(self)
        self.bot = player_2.Player_2(self)
        self.clock = pg.time.Clock()
        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

    def update(self):
        self.player_1.update()
        self.bot.update()
        for m_b in self.player_1.spisok_magic_ball:
            if m_b.hitbox.colliderect(self.bot.hitbox) and self.bot.priset is False:
                self.bot.zdorovie = self.bot.zdorovie - m_b.moshnost
                self.player_1.spisok_magic_ball.remove(m_b)
        for m_b in self.bot.spisok_magic_ball:
            if m_b.hitbox.colliderect(self.player_1.hitbox) and self.player_1.priset is False:
                self.player_1.zdorovie = self.player_1.zdorovie - m_b.moshnost
                self.bot.spisok_magic_ball.remove(m_b)

    def draw(self):
        # Отрисовка интерфейса
        self.screen.blit(self.background, (0, 0))

        self.player_1.draw()
        self.bot.draw()

        if self.player_1.zdorovie <= 0:
            shrift.render_to(self.screen, [0, 0], "Победил правый игрок", [255, 0, 0])
        elif self.bot.zdorovie <= 0:
            shrift.render_to(self.screen, [0, 0], "Победил левый игрок", [255, 0, 0])

        pg.display.flip()


if __name__ == "__main__":
    Game()
