import pygame as p
import random as rand
from santalib import *
p.init()

def create_house():
    r = rand.randint(200,255)
    g = rand.randint(50,150)
    house = House((r,g,0),rand.randint(1,4))
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
        snow = Snow(rand.randint(1,4),speed)
        snow.rect.y = rand.randint(0,600)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def more_snow():
    for i in range(round((80+45*speed)/2)):
        snow = Snow(rand.randint(1,4),speed)
        snow.rect.y = rand.randint(-100,0)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def create_present(col):
    present = Present(col,20,20)
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
    lives = 5
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
            if event.key == p.K_1:
                create_present('red')
            if event.key == p.K_2:
                create_present('blue')
            if event.key == p.K_3:
                create_present('green')
            if event.key == p.K_4:
                create_present('yellow')

def close():
    p.display.quit()
    raise SystemExit

def delete_sprites():
    global lives
    for sprite in snows:
        if sprite.rect.y > 700:
            sprite.kill()
        if sprite.rect.x < 0:
            sprite.kill()
    for sprite in houses:
        if sprite.rect.x < -100:
            if sprite.present == False:
                lives = lives - 1
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
            lst = p.sprite.spritecollide(sprite, houses, False)
            if len(lst) == 1 and lst[0].colour == sprite.colour:
                house = lst[0]
                score = score + 1
                house.present = True
                
            else:
                score = score - 1
            
        

def update_sprites_background():
    global count
    snows.update()
    if count == 25:
        more_snow()
        count = 0
    count = count + 1
def update_sprites():
    global house_count, house_max, speed
    houses.update(speed)
    snowmen.update(speed)
    presents.update(speed)
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
        speed = speed + 0.0003
if __name__ == '__main__':
    setup()
    p.time.wait(2000)
    loop()
