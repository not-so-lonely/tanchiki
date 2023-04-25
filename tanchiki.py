from pygame import*



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


###################################################################################
###################################################################################
###################################################################################
###################################################################################


class sprait(sprite.Sprite):
    def __init__(self, kartinka, x, y):
        super().__init__()
        self.image = transform.scale(image.load(kartinka), (72, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

###################################################################################
###################################################################################

class igrok(sprait):
    def upravl(self):
        self.ris()
        knopki = key.get_pressed()
        if knopki[K_RIGHT] and self.rect.x<630:
            self.rect.x += 5
        if knopki[K_LEFT] and self.rect.x>-20:
            self.rect.x -= 5
        if knopki[K_UP] and self.rect.y>0:
            self.rect.y -= 5
        if knopki[K_DOWN] and self.rect.y<550:
            self.rect.y += 5

###################################################################################
###################################################################################

class bullet(sprait):
    def __init__(self, kartinka, x, y):
        super().__init__(kartinka, x, y)
        self.image = transform.scale(image.load(kartinka), (20, 20))
    def vistrel(self):
        self.ris()
        self.rect.x += 7

###################################################################################
###################################################################################
###################################################################################
###################################################################################


tanksus = igrok('tank_gg.png',300,210)





###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################





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
    okno.blit(lvl1,(0,0))



    tanksus.upravl()

    clock.tick(FPS) 

    display.update()