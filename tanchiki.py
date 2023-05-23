from pygame import*
from random import randint
#что еще делать: враги
#спрайт коллайд рект

clock = time.Clock()#часы для игры
FPS = 120
okno = display.set_mode((700, 600))
display.set_caption("BATTLE CITY")

###################################################################################
###################################################################################

zastavochniy_ekran = image.load('zastavka2.0.png')
zastavochniy_ekran = transform.scale(zastavochniy_ekran , (700, 600))

geor = image.load('gameover.png')
geor = transform.scale(geor,(700,600))

lvl1 = image.load('lvl1.png')
lvl1 = transform.scale(lvl1,(700,600))

gameover = image.load("gameover.png")
gameover = transform.scale(gameover,(700,600))
###################################################################################
###################################################################################
###################################################################################
###################################################################################


class stena(sprite.Sprite):
    def __init__(self,  x, y,width,height):
        super().__init__()
        self.image = Surface((width,height))
        #self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def ris(self):
        okno.blit(self.image, (self.rect.x , self.rect.y )) 
class sprait(sprite.Sprite):
    def __init__(self, kartinka, x, y, napr):
        super().__init__()
        self.image = transform.scale(image.load(kartinka), (35, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.napr = napr #задаем типо направление
        self.lasx = x
        self.lasy = y

    def ris(self):
        if self.napr=="up":
            okno.blit(self.image, (self.rect.x, self.rect.y))
        elif self.napr =="left":
            self.newimage = transform.rotate(self.image, 90) #делаем новую картинку через старую + что то
            okno.blit(self.newimage, (self.rect.x, self.rect.y)) #вставляем новую картнику
        elif self.napr =="down":
            self.newimage = transform.rotate(self.image, 180) #делаем новую картинку через старую + что то
            okno.blit(self.newimage, (self.rect.x, self.rect.y)) #вставляем новую картнику
        elif self.napr =="right":
            self.newimage = transform.rotate(self.image, 270) #делаем новую картинку через старую + что то
            okno.blit(self.newimage, (self.rect.x, self.rect.y)) #вставляем новую картнику
###################################################################################
###################################################################################

class igrok(sprait):
    def upravl(self):
        self.ris()
        knopki = key.get_pressed()
        if knopki[K_RIGHT] and self.rect.x<630:
            self.napr = "right"
            self.lasx=self.rect.x
            self.lasy=self.rect.y
            self.rect.x += 5
        if knopki[K_LEFT] and self.rect.x>-20:
            self.napr = "left"
            self.lasx=self.rect.x
            self.lasy=self.rect.y
            self.rect.x -= 5
        if knopki[K_UP] and self.rect.y>-5:
            self.napr = "up"
            self.lasx=self.rect.x
            self.lasy=self.rect.y
            self.rect.y -= 5
        if knopki[K_DOWN] and self.rect.y<550:
            self.napr = "down"
            self.lasx=self.rect.x
            self.lasy=self.rect.y
            self.rect.y += 5



###################################################################################
###################################################################################

class bullet(sprait):
    def __init__(self, kartinka, x, y,napr):
        super().__init__(kartinka, x, y, napr)
        self.image = transform.scale(image.load(kartinka), (4, 4))
        if tanksus.napr == "up":
            self.napr == "up"
        if tanksus.napr == "down":
            self.napr == "down"
        if tanksus.napr == "left":
            self.napr == "left"
        if tanksus.napr == "right":
            self.napr == "right"
    def vistrel(self):
        self.ris()
       # self.napr = tanksus.napr
        if self.napr == "up":
            self.rect.y -= 7
        if self.napr == "down":
            self.rect.y += 7
        if self.napr == "left":
            self.rect.x -= 7
        if self.napr == "right":
            self.rect.x += 7

lifes = 3

class vrag(sprait):
    def __init__(self, kartinka, x, y,napr):
        super().__init__(kartinka, x, y, napr)
        self.image = transform.scale(image.load(kartinka), (30, 30)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ezda(self,x1,x2):
        self.ris()
        if self.rect.x < x1:
            self.napr = "right"
        if self.rect.x > x2:
            self.napr = "left"
        if self.napr == "left":
            self.rect.x -= 3   
        else:
            self.rect.x += 3
    def collide(self, p):
        if sprite.collide_rect(self,p):
            tanksus.rect.x = 333
            tanksus.rect.y = 428
            global lifes
            lifes -= 1









###################################################################################
###################################################################################
###################################################################################
###################################################################################


tanksus = igrok('tank_gg.png',333,428, "up")

puli = list()


tankvrag = vrag('tank_gg2.png',650,255,"left")
tankvrag2 = vrag('tank_gg2.png',650,355,"left")

walls = [
    stena(0, 0, 60, 600), #
    stena(640, 0, 60, 600), #
    stena(60, 47, 50, 207), #
    stena(160, 47, 56, 207), #
    stena(270, 47, 54, 160), #
    stena(377,47,55,160), #
    stena(485,47,55,207), #
    stena(593,47,47,207), #
    stena(108,300, 108,48), # 
    stena(485,300,108,48), #
    stena(60,392,48,160), # 
    stena(160,394,54,160), #
    stena(483,394,54,160), # 
    stena(593,394,54,160) #
]


###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################




lose = False
game = False
menu = True
while menu:
    for i in event.get(): #ппроверка очереди событий
        if i.type == QUIT: #если щелк по крестику то стоп типо
            menu = False
    
        if i.type == MOUSEBUTTONDOWN:
            if i.button == 1:
                print(i.pos)
                if i.pos[0]> 270 and i.pos[0] < 450 and i.pos[1]> 350 and i.pos[1] < 390:
                    #зарегестрировать нажатие даже на голой картинке
                    game = True
                    menu = False
                if i.pos[0]> 280 and i.pos[0] < 430 and i.pos[1]> 420 and i.pos[1] < 450:
                    menu = False

    okno.blit(zastavochniy_ekran,(0,0))


    clock.tick(FPS) 

    display.update()



while game:
    for i in event.get(): #ппроверка очереди событий
        if i.type == QUIT: #если щелк по крестику то стоп типо
            game = False

        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                b = bullet('bullet.png', tanksus.rect.x + 18, tanksus.rect.y, tanksus.napr)
                puli.append(b)        

    if lifes == 0:
        game = False
        lose = True
    

    if i.type == MOUSEBUTTONDOWN:
        if i.button == 1:
            print(i.pos)
      

    for w in walls:
        w.ris()
        if sprite.collide_rect(w, tanksus):
            tanksus.rect.x = tanksus.lasx
            tanksus.rect.y = tanksus.lasy
    okno.blit(lvl1,(0,0)) 
    for b in puli:
        b.vistrel()
        for ww in walls:
            if sprite.collide_rect(ww, b):
                puli.remove(b)
        if sprite.collide_rect(b, tankvrag):
            puli.remove(b)
            tankvrag.rect.x = 1000
            tankvrag.rect.y = 1000

        if sprite.collide_rect(b, tankvrag2):
            puli.remove(b)
            tankvrag2.rect.x = 1000
            tankvrag2.rect.y = 1000

    if sprite.collide_rect(tankvrag, tanksus):
        lifes -= 1
        tanksus.rect.x = 333
        tanksus.rect.y = 485

    if sprite.collide_rect(tankvrag2, tanksus):
        lifes -= 1
        tanksus.rect.x = 333
        tanksus.rect.y = 485


    if tankvrag.rect.x > 700 and tankvrag.rect.y > 700 and tankvrag2.rect.x > 700 and tankvrag2.rect.y > 700:
        game = False
        lose = True



    tankvrag.ezda(60,600)
    tankvrag2.ezda(180, 540)
    tanksus.upravl()

    clock.tick(FPS) 

    display.update()


while lose:
    for i in event.get(): #ппроверка очереди событий
        if i.type == QUIT: #если щелк по крестику то стоп типо
            lose = False
    
    okno.blit(gameover,(0,0))
    clock.tick(FPS) 

    display.update()
