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
        global speed
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


class Sleigh(p.sprite.Sprite):
    def __init__(self,name = ''):
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        self.image = p.transform.scale(p.image.load('sleigh.png'),(200,108))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()


        
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
        global speed
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
class Present(p.sprite.Sprite):
    def __init__(self,colour,width,height,name = ''):
        self.name = name
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.speedy = 0.1
        self.count = 1
        self.divider = int(100/3)+1
        self.falling = True
    def update(self):
        if self.falling:
            self.speedy = self.speedy + 0.05
            self.speedx = (self.count+speed)/self.divider
            if self.speedx > speed:
                self.speedx = speed
            self.y = self.y + self.speedy
            self.x = self.x - self.speedx
            self.count = self.count + 1
        else:
            self.x = self.x - speed
            
        self.rect.y = round(self.y)
        self.rect.x = round(self.x)


#text class
class Text(p.sprite.Sprite):
    def __init__(self,text,size,colour):
        p.sprite.Sprite.__init__(self)
        self.colour = colour
        self.font = p.font.SysFont('calibri',size)
        self.set(text)
    def set(self,text):
        self.image = self.font.render(str(text),True,self.colour)
        self.rect = self.image.get_rect()
    

def create_house():
    r = rand.randint(200,255)
    g = rand.randint(50,150)
    house = House1((r,g,0))
    house.rect.y = 420
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
    snowmen.add(snowman)
def create_stars():
    for i in range(rand.randint(20,40)):
        star = Star((255,223,100),rand.randint(1,3))
        star.rect.x = rand.randint(0,1280)
        star.rect.y = rand.randint(0,580)
        all_sprites_list.add(star)
        stars.add(star)
def create_snow():
    for i in range(round((640+270*speed)/2)):
        snow = Snow(rand.randint(1,4))
        snow.rect.y = rand.randint(0,600)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def more_snow():
    for i in range(round((80+45*speed)/2)):
        snow = Snow(rand.randint(1,4))
        snow.rect.y = rand.randint(-100,0)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def create_present():
    present = Present((255,0,0),20,20)
    present.x = 300
    present.rect.x = present.x
    present.y = 200
    present.rect.y = present.y
    presents.add(present)
    all_sprites_list.add(present)
def create_sleigh():
    sleigh = Sleigh()
    sleigh.rect.x = 250
    sleigh.rect.y = 175
    all_sprites_list.add(sleigh)
def setup():
    global s_text, l_text, clock, lives, all_sprites_list, stars, houses, snowmen, background, snows, ground, speed, presents, score
    background = p.display.set_mode([1280,720])
    #background = p.display.set_mode([1280,720],p.FULLSCREEN | p.SCALED)
    speed = 3
    score = 0
    lives = 3
    all_sprites_list = p.sprite.Group()
    houses = p.sprite.Group()
    stars = p.sprite.Group()
    snows = p.sprite.Group()
    presents = p.sprite.Group()
    snowmen = p.sprite.Group()
    create_stars()
    ground = Rect((255,255,255),1280,120)
    ground.rect.x = 0
    ground.rect.y = 600
    all_sprites_list.add(ground)
    create_house()
    create_snow()
    create_sleigh()

    #score text
    s_text = Text(score,50,(200,200,200))
    s_text.rect.x = 1200
    s_text.rect.y = 30
    all_sprites_list.add(s_text)

    #lives text
    l_text = Text(lives,50,(200,0,0))
    l_text.rect.x = 1120
    l_text.rect.y = 30
    all_sprites_list.add(l_text)
    
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
            if event.key == p.K_SPACE:
                create_present()

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
    for sprite in snowmen:
        if sprite.rect.x < -100:
            sprite.kill()
def present_sense():
    global score, lives
    for sprite in presents:
        if sprite.rect.y > 740 or sprite.rect.x < -20:
            sprite.kill()
            break
        if sprite.rect.y > 600 and sprite.falling == True:
            sprite.falling = False
            if len(p.sprite.spritecollide(sprite, houses, False)) == 1:
                score = score + 1
            else:
                lives = lives - 1
            
        

def update_sprites_background():
    global count
    snows.update()
    if count == 25:
        more_snow()
        count = 0
    count = count + 1
def update_sprites():
    global house_count, house_max, speed
    houses.update()
    snowmen.update()
    presents.update()
    if house_count == house_max:
        if rand.randint(1,3) == 1:
            create_snowman()
        else:
            create_house()
        house_count = 0
        house_max = round(rand.randint(400,600)*speed/9)
    house_count = house_count + 1
    
def update_screen():
    s_text.set(score)
    s_text.rect.x = 1200
    s_text.rect.y = 30
    
    l_text.set(lives)
    l_text.rect.x = 1120
    l_text.rect.y = 30
    
    background.fill([0,0,50])
    all_sprites_list.draw(background)
    p.display.flip()
    clock.tick(60)
def game_over():
    if lives == 0:
        p.time.wait(2000)
        close()
def loop():
    global count, house_count, house_max, speed
    count = 25
    house_count = 1
    bgu = 1
    counttest = 0
    house_max = round(rand.randint(400,600)*speed/9)
    while True:
        events()
        for i in range(2):
            delete_sprites()
            present_sense()
            update_sprites()
        if bgu == 2:
            update_sprites_background()
            bgu = 0
        update_screen()
        game_over()
        bgu = bgu + 1
        speed = speed + 0.0002
if __name__ == '__main__':
    setup()
    loop()
