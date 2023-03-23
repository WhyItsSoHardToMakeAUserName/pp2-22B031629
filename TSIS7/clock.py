import pygame as py
import datetime
py.init()
screen = py.display.set_mode((829,836),py.RESIZABLE)
bg = py.image.load('images/main-clock.png')
left = py.image.load('images/left-hand.png')
right = py.image.load('images/right-hand.png') 
bg_rect = bg.get_rect(center=(829 // 2, 836 // 2))
right_rect = right.get_rect(center=(829 // 2, 836 // 2))
left_rect = left.get_rect(center=(829 // 2, 836 // 2))

check = True
angle_s = 0
angle_m = 0
while check:
    t = datetime.datetime.now()
    minute, second = t.minute, t.second
    angle_s = second * (-6) + 90
    angle_m = minute * (-6) + 80
    screen.blit(bg, bg_rect)
    rotated_lh = py.transform.rotate(left, angle_s)
    rotated_lh_rect = rotated_lh.get_rect(center=(829 // 2, 836 // 2))
    rotated_rh = py.transform.rotate(right, angle_m)
    rotated_rh_rect = rotated_rh.get_rect(center=(829 // 2, 836 // 2))
    screen.blit(rotated_lh, rotated_lh_rect)
    screen.blit(rotated_rh, rotated_rh_rect)
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                check = False
    py.display.update()