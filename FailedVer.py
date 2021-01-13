import pygame as pg
import random
from threading import Thread
from time import sleep


def per(per, tot):
    return tot - (tot * per / 100)


def Merge(dict1, dict2):
    print(f">>>In merge {dict1 | dict2}")
    return dict1 | dict2


def around(present_v, last_value, limt=50):
    x0 = [i for i in range(int(last_value[0]), int(last_value[0]) + limt, 1)]
    y0 = [i for i in range(int(last_value[1]), int(last_value[1]) - limt, -1)]
    x = False
    y = False
    if not present_v[0] in x0:
        x = True
    if not present_v[1] in y0:
        y = True
    return x, y

    # print(l,present_v,last_value)


class colors:
    color_list = [(223, 255, 0), (255, 191, 0), (255, 127, 80), (222, 49, 99),
                  (159, 226, 191), (64, 224, 208), (100, 149, 237), (204, 204, 255)]
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)
    cyan = (0, 255, 255)


class kite:
    def __init__(self):
        self.x_pos = random.randint(0, 400)
        self.y_pos = random.randint(50, 400)
        self.kites = {}
        print("Asklm")
        pg.init()
        self.log = 0
        self.horiz = 0.5
        self.regiskite = []
        self.verti = 0.4
        self.WWidth = 950
        self.po = 0
        self.Wheight = 700
        self.Display = pg.display.set_mode((self.WWidth, self.Wheight))
        pg.display.set_caption("Kite Game")
        self.End = False
        # self.Kite, b1, b2, th, po = self.makeKite(400, 30, 50, (255, 0, 0))
        self.x = 200
        self.bot0(5)
        self.y = 500
        while not self.End:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.End = True

            playi = self.player()
            # for
            self.managebots()
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
            log = 30
        if pressed[pg.K_DOWN] and pressed[pg.K_RIGHT]:
            log = -30
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

        self.makeKite(self.x, self.y, 50, (255, 0, 0), alog=log, thk=True)

    def collision(self, playercoord, botcoord):
        if playercoord.colliderect(botcoord):
            print("col")

    def thread(self, points=None, tpx=None):
        cc = int(self.WWidth / 2)
        x = points[0]
        y = points[1] + 60
        bottom = self.Wheight
        if not tpx is None:
            pg.draw.aaline(self.Display, (0, 255, 0), (x, y), (cc, bottom))
        else:
            if x < cc:
                mx = x - 120
            else:
                mx = x + 120
            return pg.draw.aaline(self.Display, (0, 255, 0), (x, y), (mx, bottom))

    def managebots(self):
        for kite11 in self.kites:
            self.runbot(self.kites[kite11])

    # def makek(self,*args, **kwargs):
    def makeKite(self, x, y, w=50, rgb=(255, 255, 255), ad=4, alog=0, thk=None):
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
        Bd1 = pg.draw.aalines(self.Display, (0, 0, 0), True, z)
        Bd2 = pg.draw.aalines(self.Display, (0, 0, 0), True, z1)
        # sleep(0.001)
        self.thread(p1, thk)
        # return p1, Bd1, Bd2, self.thread(p1, thk), mage

    # def makeKite(self, *args, **kwargs):
    #     Thread(target=self.makek, args=args, kwargs=kwargs, daemon=True).start()

    # def makeKite(self, x, y, w=50, rgb=(255, 255, 255), ad=4, alog=0,thk=None):

    def botruner(self, info):
        sleep(0.001)
        px = random.randint(info["coord"][0] - 5, info["coord"][0] + 5)
        py = random.randint(info["coord"][1] - 5, info["coord"][1] + 5)
        plx = self.x
        ply = self.y
        cx, cy = around((px, py), (plx, ply))
        if not cx or not cy:
            # self.runbot(kite, coord)
            self.makeKite(px, py, rgb=info["color"])
        else:
            self.makeKite(px, py, rgb=info["color"])

    def runbot(self, *args):
        Thread(target=self.botruner, args=args, daemon=True).start()

    def bot0(self, no_bots):
        e = self.WWidth - 50
        s = int(e / no_bots)
        print(f"DIVI: {s}")
        frox = range(50, e, +s)
        print(frox)
        ys = [random.randint(30, 100) for i in range(len(frox))]
        vcc = (random.choice([0, 255, 0, 255]), random.choice([0, 255, 0, 255]), random.choice([0, 255, 0, 255]))

        for x in frox:
            colorx = random.choice(colors.color_list)

            self.bot1((x, ys[frox.index(x)]), 50, colorx, end=e, step=s)

    def bot1(self, coords=(400, 30), size=50, color=(255, 0, 0), end=0, step=0):
        self.makeKite(coords[0], coords[1], size, color)
        self.kites = Merge(self.kites,
                           {f"{self.po}": {"coord": (coords[0] + 50, coords[1]), "size": size, "color": color,
                                           "end": end, "step": step}})
        self.po += 1


if __name__ == '__main__':
    kite()
