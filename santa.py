import pygame as p
import random as rand
from santalib import *
p.init()

def create_house():
    house = House(rand.randint(1,4))       #rand num for which num house
    house.rect.y = 500
    house.x = 1280
    house.rect.x = 1280
    all_sprites_list.add(house)
    houses.add(house)
def create_snowman():
    snowman = SnowMan()
    snowman.rect.y = 458
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
    for i in range(round((640+270*speed/2))):    #change *2 to /2 if game lags
        snow = Snow(rand.randint(1,4),speed)
        snow.rect.y = rand.randint(0,600)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def more_snow():
    for i in range(round((80+45*speed/2))):      #change *2 to /2 if game lags
        snow = Snow(rand.randint(1,4),speed)
        snow.rect.y = rand.randint(-100,0)
        snow.y = snow.rect.y
        xplus = (720-snow.y/snow.speedy)*snow.speedx
        snow.rect.x = rand.randint(0,round(1280+xplus))
        snow.x = snow.rect.x
        all_sprites_list.add(snow)
        snows.add(snow)
def create_present(num):
    present = Present(num,20,20)
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
def create_tree(size, x = 1380):
    tree = Tree(size)
    if size == 'big':
        tree.rect.y = 360
    if size == 'small':
        tree.rect.y = 340
    tree.x = x
    tree.rect.x = 1380
    all_sprites_list.add(tree)
    trees.add(tree)
def setup():
    global s_text, l_text, clock, lives, all_sprites_list, stars, houses, snowmen, background, snows, ground, speed, presents, score, trees
    #background = p.display.set_mode([1280,720])
    background = p.display.set_mode([1280,720],p.FULLSCREEN | p.SCALED)
    speed = 3        #set to 3
    score = 0
    lives = 1000
    all_sprites_list = p.sprite.Group()
    houses = p.sprite.Group()
    stars = p.sprite.Group()
    snows = p.sprite.Group()
    presents = p.sprite.Group()
    snowmen = p.sprite.Group()
    trees = p.sprite.Group()
    create_stars()
    #create ground
    ground = Rect((255,255,255),1280,220)       #1280,120
    ground.rect.x = 0
    ground.rect.y = 500        #600
    all_sprites_list.add(ground)


    for i in range(-80,1380,80):
        create_tree('small',i)
        
    for i in range(-100,1380,100):
        create_tree('big',i)

        
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
    global present_wait
    for event in p.event.get():
        if event.type == p.QUIT:
            close()
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                close()
            if present_wait >= 60:
                present_wait = 0
                if event.key == p.K_1:
                    create_present(1)
                if event.key == p.K_2:
                    create_present(2)
                if event.key == p.K_3:
                    create_present(3)
                if event.key == p.K_4:
                    create_present(4)

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
        if sprite.rect.x < -135:
            if sprite.present == False:
                lives = lives - 1
            sprite.kill()
    for sprite in snowmen:
        if sprite.rect.x < -135:
            sprite.kill()
    for sprite in trees:
        if sprite.rect.x < -135:
            sprite.kill()
            
def present_sense():
    global score, lives
    for sprite in presents:
        if sprite.rect.x < -20:           #if off screen kill
            sprite.kill()
            break
        if sprite.rect.y > 600 and sprite.falling == True:                #if landed on ground
            sprite.falling = False                                        #stop falling
            lst = p.sprite.spritecollide(sprite, houses, False)           #if collision with house
            if len(lst) == 1 and lst[0].num == sprite.num:          #check if house is correct number
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
    global house_count, house_max, speed, tree_count, tree_count_s
    houses.update(speed)
    snowmen.update(speed)
    trees.update(speed)
    presents.update(speed)

    if tree_count_s >= 80:
        create_tree('small')
        tree_count_s = 0
    
    if tree_count >= 100:
        create_tree('big')
        tree_count = 0
    
    if house_count >= house_max:
        if rand.randint(1,3) == 1:
            create_snowman()
        else:
            create_house()
        house_count = 0
        #house_max = round(rand.randint(400,600)*speed/9)
    house_max = rand.random()*(speed*80-speed*60)+speed*60       #get rand between speed*60 and speed*80
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
    global count, house_count, house_max, speed, present_wait, tree_count, tree_count_s
    count = 25
    house_count = 1
    bgu = 1
    counttest = 0
    house_max = round(rand.randint(400,600)*speed/9)
    present_wait = 0
    tree_count = 100
    tree_count_s = 80
    while True:
        events()
        for i in range(2):
            delete_sprites()
            present_sense()         #detect if presents have landed
            update_sprites()
        if bgu == 2:
            update_sprites_background()
            bgu = 0
        update_screen()
        game_over()
        bgu = bgu + 1
        present_wait = present_wait + 1
        tree_count = tree_count + speed*2
        tree_count_s = tree_count_s + speed*2
        speed = speed * 1.0001
if __name__ == '__main__':
    setup()
    p.time.wait(2000)
    loop()
