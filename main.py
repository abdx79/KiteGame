import pygame as pg


class kite:
    def __init__(self):
        print("Asklm")
        pg.init()
        self.Display = pg.display.set_mode((950, 700))
        pg.display.set_caption("Kite Game")
        self.End = False
        kxy = [150, 20]
        d = 20
        self.Kite = self.makeKite(200, 30, 50)
        self.Kite = self.makeKite(400, 180, 50, (255, 0, 0))
        # self.Kite = pg.draw.polygon(self.Display, (255, 255, 255), (self.makeKite(200, 30, 50)))
        while not self.End:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.End = True
            pg.display.flip()

    def makeKite(self, x, y, w, rgb=(255, 255, 255), ad=4):
        h = w + 20
        p1 = (x, y)
        p0 = (x-w, y+h+ad)
        p2 = (x+w, y+h+ad)
        p3 = (x, y+(h*2)+(ad*2))
        pg.draw.polygon(self.Display, rgb, (p0, p1, p2, p3))
        x = pg.draw.line(self.Display, (0, 0, 0), (p1[0],p1[1]+3), (p3[0], p3[1]-3),width=2)
        x = pg.draw.line(self.Display, (0, 0, 0), (p0[0]+2, p0[1]), (p2[0]-2, p2[1]),width=2)
        pg.display.flip()
        # return pg.draw.polygon(self.Display, rgb, (p0, p1, p2, p3))
        # return p0, p1, p2, p3


if __name__ == '__main__':
    kite()

