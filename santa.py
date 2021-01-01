import pygame as p
import random as rand
p.init()

class Rect(p.sprite.Sprite):
    def __init__(self,colour,width,height,name = ''):
        self.name = name
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

class House1(p.sprite.Sprite):
    def __init__(self,colour,name = ''):
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([100,200])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        p.draw.rect(self.image,colour,(0,50,100,150))
        #chimney
        if rand.randint(0,1) == 1:
            p.draw.rect(self.image,colour,(10,10,20,40))
            p.draw.rect(self.image,(255,255,255),(10,10,20,5))
            
        else:
            p.draw.rect(self.image,colour,(70,10,20,40))
            p.draw.rect(self.image,(255,255,255),(70,10,20,5))
            
        p.draw.polygon(self.image,(255,255,255),[(0,50),(50,0),(100,50)])
        #windows
        p.draw.rect(self.image,(25,25,50),(10,70,30,40))
        p.draw.rect(self.image,(84,42,0),(10,70,30,40),2)
        p.draw.rect(self.image,(25,25,50),(60,70,30,40))
        p.draw.rect(self.image,(84,42,0),(60,70,30,40),2)
        if rand.randint(0,1) == 1:
            p.draw.rect(self.image,(25,25,50),(60,145,30,40))
            p.draw.rect(self.image,(100,50,0),(60,145,30,40),2)

            p.draw.rect(self.image,(100,50,25),(10,145,30,65))
            p.draw.rect(self.image,(84,42,0),(10,145,30,65),2)
            
        else:
            p.draw.rect(self.image,(25,25,50),(10,145,30,40))
            p.draw.rect(self.image,(84,42,0),(10,145,30,40),2)

            p.draw.rect(self.image,(100,50,25),(60,145,30,65))
            p.draw.rect(self.image,(84,42,0),(60,145,30,65),2)
        self.rect = self.image.get_rect()
    def update(self):
        self.x = self.x - speed
        self.rect.x = round(self.x)


class SnowMan(p.sprite.Sprite):
    def __init__(self,name = ''):
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([100,200])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        p.draw.circle(self.image,(255,255,255),(50,150),50)
        p.draw.circle(self.image,(255,255,255),(50,80),25)
        p.draw.circle(self.image,(0,0,0),(40,75),5)
        p.draw.circle(self.image,(0,0,0),(60,75),5)
        p.draw.circle(self.image,(0,0,0),(50,120),5)
        p.draw.circle(self.image,(0,0,0),(50,140),5)
        p.draw.circle(self.image,(0,0,0),(50,160),5)
        p.draw.circle(self.image,(0,0,0),(50,180),5)
        p.draw.circle(self.image,(255,165,0),(50,85),5)
        p.draw.arc(self.image,(0,0,0),(40,70,20,30),3.9,5.6)
        p.draw.arc(self.image,(255,0,0),(25,75,50,40),3.6,5.9,10)
        p.draw.polygon(self.image,(255,0,0),[(55,110),(65,105),(80,130),(65,135)])   #scarf
        p.draw.polygon(self.image,(255,0,0),[(50,0),(26,65),(74,65)])   #hat
        p.draw.polygon(self.image,(0,255,0),[(26,65),(74,65),(75,70),(25,70)])   #hat
        self.rect = self.image.get_rect()
    def update(self):
        self.x = self.x - speed
        self.rect.x = round(self.x)


        
class Star(p.sprite.Sprite):
    def __init__(self,colour,radius,name = ''):
        self.name = name
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([radius*2+1,radius*2+1])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        p.draw.line(self.image,colour,(1,1),(radius*2-1,radius*2-1))
        p.draw.line(self.image,colour,(radius*2-1,1),(1,radius*2-1))
        p.draw.line(self.image,colour,(radius,0),(radius,radius*2))
        p.draw.line(self.image,colour,(0,radius),(radius*2,radius))
        self.rect = self.image.get_rect()
        
class Snow(p.sprite.Sprite):
    def __init__(self,radius,name = ''):
        self.name = name
        self.x = 0
        self.y = 0
        self.speedy = rand.uniform(1,5)
        self.speedx = rand.uniform(radius/4,(radius-radius/2.5)*speed)
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([radius*2,radius*2])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        p.draw.circle(self.image,(255,255,255),(radius,radius),radius)
        self.rect = self.image.get_rect()
    def update(self):
        self.y = self.y + self.speedy
        self.rect.y = round(self.y)
        self.x = self.x - self.speedx
        self.rect.x = round(self.x)

def create_house():
    r = rand.randint(200,255)
    g = rand.randint(50,150)
    house = House1((r,g,0))
    house.rect.y = 460
    house.x = 1280
    house.rect.x = 1280
    all_sprites_list.add(house)
    houses.add(house)
def create_snowman():
    snowman = SnowMan()
    snowman.rect.y = 410
    snowman.x = 1280
    snowman.rect.x = 1280
    all_sprites_list.add(snowman)
    houses.add(snowman)
def create_stars():
    for i in range(rand.randint(20,40)):
        star = Star((255,223,100),rand.randint(1,3))
        star.rect.x = rand.randint(0,1280)
        star.rect.y = rand.randint(0,580)
        all_sprites_list.add(star)
        stars.add(star)
def create_snow():
    for i in range(round(640+270*speed)):
        snow = Snow(rand.randint(1,4))
        snow.rect.y = rand.randint(0,600)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def more_snow():
    for i in range(round(80+45*speed)):
        snow = Snow(rand.randint(1,4))
        snow.rect.y = rand.randint(-100,0)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def setup():
    global clock, all_sprites_list, stars, houses, background, snows, ground, speed
    background = p.display.set_mode([1280,720])
    speed = 1.5
    all_sprites_list = p.sprite.Group()
    houses = p.sprite.Group()
    stars = p.sprite.Group()
    snows = p.sprite.Group()
    create_stars()
    ground = Rect((255,255,255),1280,120)
    ground.rect.x = 0
    ground.rect.y = 600
    all_sprites_list.add(ground)
    create_house()
    create_snow()
    background.fill([0,0,50])
    all_sprites_list.draw(background)
    p.display.flip()
    clock = p.time.Clock()

def events():
    for event in p.event.get():
        if event.type == p.QUIT:
            close()
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                close()

def close():
    p.display.quit()
    raise SystemExit

def delete_sprites():
    for sprite in snows:
        if sprite.rect.y > 700:
            sprite.kill()
        if sprite.rect.x < 0:
            sprite.kill()
    for sprite in houses:
        if sprite.rect.x < -100:
            sprite.kill()
def update_sprites_background():
    global count
    snows.update()
    if count == 25:
        more_snow()
        count = 0
    count = count + 1
def update_sprites():
    global house_count, house_max
    houses.update()
    if house_count == house_max:
        if rand.randint(1,1) == 1:
            create_snowman()
        else:
            create_house()
        house_count = 0
        house_max = round(rand.randint(400,600)/speed)
    house_count = house_count + 1
def update_screen():
    background.fill([0,0,50])
    all_sprites_list.draw(background)
    p.display.flip()
    clock.tick(60)
def loop():
    global count, house_count, house_max
    count = 25
    house_count = 1
    bgu = 1
    counttest = 0
    house_max = round(rand.randint(400,600)/speed)
    while True:
        events()
        for i in range(2):
            delete_sprites()
            update_sprites()
        if bgu == 2:
            update_sprites_background()
            bgu = 0
        update_screen()
        bgu = bgu + 1
if __name__ == '__main__':
    setup()
    loop()
