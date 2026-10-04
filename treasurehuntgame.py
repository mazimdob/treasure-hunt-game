import pygame 
import random
import time 

pygame.init()
pygame.display.set_caption("tresaure hunt")

screen_Width=900
screen_Height=700
screen=pygame.display.set_mode((screen_Width,screen_Height))

def changebackround():
    image=pygame.image.load("bghunt.png")
    image=pygame.transform.scale(image,(screen_Width,screen_Height))
    screen.blit(image,(0,0))

class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pirate.png")
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Non_collectable (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("rat.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class Collectable (pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

allsprites=pygame.sprite.Group()
item_list=pygame.sprite.Group()
rat_list=pygame.sprite.Group()

pirate=Pirate()
allsprites.add(pirate)

for i in range(20):
    rat=Non_collectable()
    rat.rect.x=random.randrange(screen_Width)
    rat.rect.y=random.randrange(screen_Height)
    rat_list.add(rat)
    allsprites.add(rat)

images=["item1a.png","item2a.png","item3a.png"]
for i in range (50):
    item=Collectable(random.choice(images))
    item.rect.x=random.randrange(screen_Width)
    item.rect.y=random.randrange(screen_Height)
    item_list.add(item)
    allsprites.add(item)

WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
GREEN=(0,255,0)
playing=True
score=0

clock=pygame.time.Clock()
start_time=time.time()

myfont=pygame.font.SysFont("Times New Roman",22)
text=myfont.render("score="+str(0),True,BLACK)

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    timeElapsed=time.time()-start_time
    if timeElapsed>=60:
        if score>20:
            screen.fill(GREEN)
            myfont=pygame.font.SysFont("comic",50)
            text1=myfont.render("treasure collected",True,BLACK)

        else:
            screen.fill(RED)
            myfont=pygame.font.SysFont("comic",50)
            text1=myfont.render("treasure not collected",True,BLACK)

        screen.blit(text1,(250,40))
    else:
        changebackround()
        countdown=myfont.render("Time Left:"+str(60-int(timeElapsed)),True, BLACK)
        screen.blit(countdown,(20,10))

        keys=pygame.key.get_pressed()
        if keys [pygame.K_UP]:
            if pirate.rect.y>0:
                pirate.rect.y-=5

        if keys[pygame.K_DOWN]:
            if pirate.rect.y<630:
                pirate.rect.y+=5

        if keys [pygame.K_RIGHT]:
            if pirate.rect.x<850:
                pirate.rect.x+=5

        if keys [pygame.K_LEFT]:
            if pirate.rect.x>0:
                pirate.rect.x-=5
        item_hit_list=pygame.sprite.spritecollide(pirate,item_list,True )

        for item in item_hit_list:
            score +=1
            text=myfont.render("score="+str(score),True,BLACK)

        rat_hit_list=pygame.sprite.spritecollide(pirate, rat_list, True)

        for rat in rat_hit_list:
            score -=5
            text=myfont.render("score="+str(score),True,BLACK)
    screen.blit(text,(20,50))

    allsprites.draw(screen)
    pygame.display.update()

pygame.quit()
        