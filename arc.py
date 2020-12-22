import pygame as p
p.init()
background = p.display.set_mode([1280,720])
p.draw.arc(background,(255,255,255),(0,0,1280,720),0,0)
p.display.flip()
xc = 0
x = 3.8
y = 5.6
yc = 0
clock = p.time.Clock()
while True:
    for event in p.event.get():
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                p.display.quit()
                raise SystemExit
            if event.key == p.K_LEFT:
                xc = 0.01
                print(x)
            if event.key == p.K_RIGHT:
                xc = -0.01
                print(x)
            if event.key == p.K_UP:
                yc = 0.01
                print(y)
            if event.key == p.K_DOWN:
                yc = -0.01
                print(y)
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                xc = 0
                print(x)
            if event.key == p.K_RIGHT:
                xc = 0
                print(x)
            if event.key == p.K_UP:
                yc = 0
                print(y)
            if event.key == p.K_DOWN:
                yc = 0
                print(y)
    clock.tick(60)
    x = x + xc
    y = y + yc
    background.fill([0,0,0])
    p.draw.circle(background,(255,255,255),(50,100),50)
    p.draw.circle(background,(255,255,255),(50,30),25)
    p.draw.circle(background,(0,0,0),(40,25),5)
    p.draw.circle(background,(0,0,0),(60,25),5)
    p.draw.circle(background,(0,0,0),(50,70),5)
    p.draw.circle(background,(0,0,0),(50,90),5)
    p.draw.circle(background,(0,0,0),(50,110),5)
    p.draw.circle(background,(0,0,0),(50,130),5)
    p.draw.circle(background,(255,165,0),(50,35),5)
    p.draw.arc(background,(0,0,0),(40,20,20,30),3.9,5.6)
    p.draw.arc(background,(255,0,0),(25,25,50,40),x,y,10)
    p.display.flip()
