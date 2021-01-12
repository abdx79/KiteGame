import pygame as pg


def per(per, tot):
    return tot - (tot * per / 100)


class kite:
    def __init__(self):
        print("Asklm")
        pg.init()
        self.log = 0
        self.horiz = 0.5
        self.verti = 0.4
        self.WWidth = 950
        self.Wheight = 700
        self.Display = pg.display.set_mode((self.WWidth, self.Wheight))
        pg.display.set_caption("Kite Game")
        self.End = False
        # self.Kite, b1, b2, th, po = self.makeKite(400, 30, 50, (255, 0, 0))
        self.x = 200
        self.y = 500
        while not self.End:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.End = True

            self.player()
            pg.display.flip()
            self.Display.fill((0, 0, 0))

    def player(self, x=300, y=400, log=0):
        log = 0
        pressed = pg.key.get_pressed()

        if not pressed[pg.K_DOWN]:
            if self.y > per(40, self.Wheight):
                self.y += self.verti
            else:
                self.y += self.verti - 0.3
        else:
            self.y -= self.verti
        if pressed[pg.K_UP]:
            self.y += 0.5
        if pressed[pg.K_DOWN] and pressed[pg.K_LEFT]:
            print("Analog Left")
            log = 30
        if pressed[pg.K_DOWN] and pressed[pg.K_RIGHT]:
            log = -30
            print("Analog Right")
        if pressed[pg.K_LEFT]:
            self.x -= self.horiz
        if pressed[pg.K_RIGHT]:
            self.x += self.horiz

        if self.y < 20:
            self.y = 20
        if self.x < 50:
            self.x = 50
        if self.x > self.WWidth - 50:
            self.x = self.WWidth - 50
        if self.y > self.Wheight:
            self.y = self.Wheight

        Kite, b1, b2, th, po = self.makeKite(self.x, self.y, 50, (255, 0, 0), alog=log)

    def collision(self, playercoord, botcoord):
        if playercoord.colliderect(botcoord):
            print("col")

    def thread(self, points):
        x = points[0]
        y = points[1] + 60
        bottom = self.Wheight
        return pg.draw.aaline(self.Display, (0, 255, 0), (x, y), (int(self.WWidth / 2), bottom))

    def makeKite(self, x, y, w, rgb=(255, 255, 255), ad=4, alog=0):

        h = w + 20
        p1 = (x, y)
        p0 = (x - w + alog, y + h + ad)
        p2 = (x + w + alog, y + h + ad)
        p3 = (x + alog, y + (h * 2) + (ad * 2))
        pointy = [(p1[0], p1[1] + 3), (p3[0], p3[1] - 3)]
        pointx = [(p0[0] + 2, p0[1]), (p2[0] - 2, p2[1])]
        z = [*pointx, *pointy]
        pointy1 = [(p1[0], p1[1] + 3), (p3[0], p3[1] - 3)]
        pointx1 = [(p2[0] - 2, p2[1]), (p0[0] + 2, p0[1])]
        z1 = [*pointx1, *pointy1]

        mage = pg.draw.polygon(self.Display, rgb, (p0, p1, p2, p3))
        # x = pg.draw.line(self.Display, (0, 0, 0), *pointx, width=2)
        # x = pg.draw.line(self.Display, (0, 0, 0), *pointy, width=2)
        Bd1 = pg.draw.aalines(self.Display, (0, 0, 0), True, z)
        Bd2 = pg.draw.aalines(self.Display, (0, 0, 0), True, z1)

        # return pg.draw.polygon(self.Display, rgb, (p0, p1, p2, p3))
        # return p0, p1, p2, p3
        return p1, Bd1, Bd2, self.thread(p1), mage

    def bot(self):
        self.kites = []
        Kite, b1, b2, th, po = self.makeKite(400, 30, 50, (255, 0, 0))
        self.kites.append([kite, po, th])


if __name__ == '__main__':
    kite()
