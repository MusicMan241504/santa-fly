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
    def __init__(self,colour,randnum,name = ''):
        global speed
        self.colour = ['red','blue','green','yellow'][randnum-1]
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
            p.draw.rect(self.image,self.colour,(10,145,30,65))
            p.draw.rect(self.image,(84,42,0),(10,145,30,65),2)
            
        else:
            p.draw.rect(self.image,(25,25,50),(10,145,30,40))
            p.draw.rect(self.image,(84,42,0),(10,145,30,40),2)

            p.draw.rect(self.image,self.colour,(60,145,30,65))
            p.draw.rect(self.image,(84,42,0),(60,145,30,65),2)
        self.rect = self.image.get_rect()
        self.present = False
    def update(self,speed):
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
        p.draw.circle(self.image,(1,1,1),(40,75),5)
        p.draw.circle(self.image,(1,1,1),(60,75),5)
        p.draw.circle(self.image,(1,1,1),(50,120),5)
        p.draw.circle(self.image,(1,1,1),(50,140),5)
        p.draw.circle(self.image,(1,1,1),(50,160),5)
        p.draw.circle(self.image,(1,1,1),(50,180),5)
        p.draw.circle(self.image,(255,165,0),(50,85),5)
        p.draw.arc(self.image,(0,0,0),(40,70,20,30),3.9,5.6)
        p.draw.arc(self.image,(255,0,0),(25,75,50,40),3.6,5.9,10)
        p.draw.polygon(self.image,(255,0,0),[(55,110),(65,105),(80,130),(65,135)])   #scarf
        p.draw.polygon(self.image,(255,0,0),[(50,0),(26,65),(74,65)])   #hat
        p.draw.polygon(self.image,(0,255,0),[(26,65),(74,65),(75,70),(25,70)])   #hat
        self.rect = self.image.get_rect()
    def update(self,speed):
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
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def update(self,speed):
        if self.size:
            self.x = self.x - speed*0.9
        else:
            self.x = self.x - speed*0.8
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
    def __init__(self,colour,width,height,name = ''):
        self.name = name
        self.colour = colour
        p.sprite.Sprite.__init__(self)
        self.image = p.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.speedy = 0.1
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

def setup():
    global tree_img, tree_img_small
    tree_img = p.image.load('tree2.png')
    tree_img_small = p.transform.scale(p.image.load('tree2.png'),(108,192))

if __name__ != '__main__':
    setup()
