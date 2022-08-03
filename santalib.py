import pygame as p
import random as rand
class Rect(p.sprite.Sprite):
    def __init__(self,colour,width,height,name = ''):
        self.name = name
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

class House(p.sprite.Sprite):
    def __init__(self,num,name = ''):
        global speed
        self.num = num          #store num in sprite
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        #get correct image depending on num
        if self.num == 1:
            self.image = house1
        elif self.num == 2:
            self.image = house2
        elif self.num == 3:
            self.image = house3
        elif self.num == 4:
            self.image = house4
        
        self.image.set_colorkey((0,0,0,0))    #remove background
        
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)        #create sprite mask
        self.present = False                #boolean to check if house has a present on it
    def update(self,speed):
        self.x = self.x - speed
        self.rect.x = round(self.x)


class SnowMan(p.sprite.Sprite):
    def __init__(self,name = ''):
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        self.image = snowman_img
        self.image.set_colorkey((0,0,0,0))
        self.rect = self.image.get_rect()
    def update(self,speed):
        self.x = self.x - speed
        self.rect.x = round(self.x)


class Sleigh(p.sprite.Sprite):
    def __init__(self,name = ''):
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        self.image = sleigh_img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()


class Tree(p.sprite.Sprite):
    def __init__(self,size,name = ''):
        self.name = name
        self.x = 0
        p.sprite.Sprite.__init__(self)
        if size == 'big':
            self.size = 1
            self.image = tree_img
        if size == 'small':
            self.size = 0
            self.image = tree_img_small
        self.image.set_colorkey((0,0,0,0))
        self.rect = self.image.get_rect()
    def update(self,speed):
        if self.size:
            self.x = self.x - speed*0.9
        else:
            self.x = self.x - speed*0.8
        temp = round(self.x)
        self.rect.x = temp         #takes too long


        
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
    def __init__(self,radius,speed,name = ''):
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
    def __init__(self,num,name = ''):
        self.name = name
        self.num = num
        p.sprite.Sprite.__init__(self)
        #get correct present img
        if num == 1:
            self.image = present1
        if num == 2:
            self.image = present2
        if num == 3:
            self.image = present3
        if num == 4:
            self.image = present4
            
        self.image.set_colorkey((0,0,0,0))
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)        #create sprite mask
        self.speedy = 0.4
        self.count = 1
        self.divider = int(100/3)+1
        self.falling = True
    def update(self,speed):
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

def setup_lib():
    global tree_img, tree_img_small, snowman_img, sleigh_img, house1, house2, house3, house4, present1, present2, present3, present4
    
    #must load images before game to avoid lag
    tree_img = p.image.load('img_fhd/tree.png').convert()        #big tree
    tree_img_small = p.image.load('img_fhd/tree_s.png').convert()   #small tree


    
    snowman_img = p.image.load('img_fhd/snowman.png').convert()

    sleigh_img = p.image.load('img_fhd/sleigh.png').convert()

    #houses
    house1 = p.image.load('img_fhd/house1.png').convert()
    house2 = p.image.load('img_fhd/house2.png').convert()
    house3 = p.image.load('img_fhd/house3.png').convert()
    house4 = p.image.load('img_fhd/house4.png').convert()

    #presents
    present1 = p.image.load('img_fhd/present1.png').convert()
    present2 = p.image.load('img_fhd/present2.png').convert()
    present3 = p.image.load('img_fhd/present3.png').convert()
    present4 = p.image.load('img_fhd/present4.png').convert()


