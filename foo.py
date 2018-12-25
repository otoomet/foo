#!/usr/bin/python3
import pygame as pg
import random as r
pg.init()
pic = pg.image.load("hullmyts.png")
picWidth = 0.05
# width of pick in terms of pct of screen width
dpic = pg.image.load("khullmyts2.png")
dpicWidth = picWidth
plt = pg.image.load("platform.png")
pltWidth = 0.08

screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("sgfndfhgkdfbrhgfdscergchdfnkgsdfkjghsvrshtgskrutgspldrutskrdjhtgankjhfairuthvaleiruthacpmeriuthvalneriutelrimtgbajnflkauhrntkvuahlarhtbakvjrhgnakterutvhndkhfaldrjvankrjhgcnakfrhmvladuhgsnkdfhsldrghsvlkrrjtghsvrthgslkjvfsklgshlkruvslkjghslveirghmslvdjgvslnuygrnuhavtleritbhanoerigksadrjghdjhgnliudrgndrhgaserghvrkdighaerliubyakerhnalerijthaelrithaceriutvbaeprtivauiayhrtvalbrtvbalerrhgtvkprdhtgncsketgsnkdfhgksnerytgkcgspguksjhtkucdhgnvksg")

## Scale images to the suitable size on the screen
picW = picWidth*screen.get_width()
picH = pic.get_height()*picW/pic.get_width()
pic = pg.transform.scale(pic, (int(picW), int(picH)))
##
pltW = pltWidth*screen.get_width()
pltH = plt.get_height()*pltW/plt.get_width()
plt = pg.transform.scale(plt, (int(pltW), int(pltH)))

## ground thickness: how far down (in pixels) will the CH fall
groundThickness = int(0.06*screen.get_height()) + pic.get_height()

do = True
dist = 5
up = True
down = True
left = True
right = True 
mup = False
mdown = False
mleft = False
mright = False
timer = pg.time.Clock()
lifes = 5
font = pg.font.SysFont("Times", 24)
dfont = pg.font.SysFont("Times", 32)
pfont = pg.font.SysFont("Times", 50)
pause = False
gameover = False
jp = 30
player = pg.sprite.Group()
platform = pg.sprite.Group()
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.yvel = 0
        self.xvel = 0
        self.onair = True
    def update(self, mup, mdown, mleft, mright):
        if self.rect.y <= 0:
            up = False
        else:
            up = True
        if self.rect.y >= screenh - groundThickness:
            down = False
        else:
            down = True
        if self.rect.x+ self.xvel <= 0:
            left = False
            self.xvel = 0
        else:
            left = True
        if self.rect.x + self.xvel >= screenw-148:
            right = False
            self.xvel=0
        else:
            right = True
        if mup:# and not self.onair:
            self.yvel -= jp
        if mdown and down:
            self.rect.y += dist
        if mleft and left:
            if self.onair:
                self.xvel -= 0.5
            else:
                self.xvel -= 5
        if mright and right:
            if self.onair:
                self.xvel += 0.5
            else:
                self.xvel += 5
        if self.rect.y + self.yvel <= screenh - groundThickness:
            self.onair = True
        else:
            self.onair = False
        self.rect.y += self.yvel
        if self.onair:
            self.yvel += 1
        else:
            self.yvel=0
        if left and right:
            self.rect.x += self.xvel
        if not self.onair:
            self.xvel = round(self.xvel*0.4)
    def getxy(self):
        return(self.rect.x,self.rect.y)
class Platform(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = plt
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def getxy(self):
        return(self.rect.x,self.rect.y)
def reset():
    lifes = 5
    player.empty()
    hullmyts = Player(screenw/2,screenh/2)
    player.add(hullmyts)
hullmyts = Player(screenw/2,screenh/2)
player.add(hullmyts)
platboi = Platform(screenw/2,screenh/2)
platform.add(platboi)
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            do = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                mup = True
            elif event.key == pg.K_DOWN:
                mdown = True
            elif event.key == pg.K_LEFT:
                mleft = True
            elif event.key == pg.K_RIGHT:
                mright = True
            elif event.key == pg.K_p:
                pause = True
            elif event.key == pg.K_r:
                reset()
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                mup = False
            elif event.key == pg.K_DOWN:
                mdown = False
            elif event.key == pg.K_LEFT:
                mleft = False
            elif event.key == pg.K_RIGHT:
                mright = False
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pause = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = False
        pd = "PAUSED"
        ptext = dfont.render(pd, True, (127,127,127))
        ptext_rect = ptext.get_rect()
        ptext_rect.centerx = screen.get_rect().centerx
        ptext_rect.y = 50
        screen.blit(ptext,ptext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
    if lifes == 0:
        uded = "GAME OVER"
        dtext = dfont.render(uded, True, (255,0,0))
        dtext_rect = dtext.get_rect()
        dtext_rect.centerx = screen.get_rect().centerx
        dtext_rect.y = 30
        screen.blit(dtext,dtext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
        gameover = True
    while gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    gameover = False
                    reset()
    col = pg.sprite.spritecollide(hullmyts, platform,False)
    #if len(col) > 0:
    screen.fill((0,0,0))
    score = ("Lifes: " + str(lifes))
    text = font.render(score, True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text,text_rect)
    player.update(mup,mdown, mleft, mright)
    mup = False
    platform.draw(screen)
    player.draw(screen)
    pg.display.update()
    timer.tick(60)

pg.quit()
