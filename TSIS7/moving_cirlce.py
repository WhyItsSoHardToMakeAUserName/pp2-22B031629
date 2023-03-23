import pygame as py
py.init()
screen = py.display.set_mode((500,500))
Done = True
pos = [250,250]
while Done == True:
    for event in py.event.get():
        if event.type == py.KEYDOWN:    
            if event.key == py.K_ESCAPE:
                Done = False
            if event.key == py.K_w:
                if pos[1]-20>20:
                    pos[1] -= 20
            if event.key == py.K_a:
                if pos[0]-20>20:
                    pos[0] -= 20    
            if event.key == py.K_s:
                if pos[1]+20<490:
                    pos[1] += 20
            if event.key == py.K_d:
                if pos[0]+20<490:
                    pos[0] += 20
    screen.fill([0,0,0])
    py.draw.circle(screen,"red",pos,20)
    py.display.update()
