
import pygame
pygame.init()
    
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
mode = 'red'
draw_mode = 'pen'
points = []
points_list = []
rect_list = []
rect_points = []
rect_start = ()
rect_end = ()
def draw_circle():
    pass
def draw_rect(start,end,color,md):
    width = abs(end[0][0] - start[0][0])
    height = abs(start[0][1] - end[0][1])
    if md == 'romb':
        if start[0][1] > end[0][1]:#top
                pygame.draw.polygon(screen,color,(start[0],(start[0][0]+height//2,start[0][1]-height//2),(start[0][0],end[0][1]),(start[0][0]-height//2,start[0][1]-height//2)))
        elif start[0][1] < end[0][1]:#bot 
                pygame.draw.polygon(screen,color,(start[0],(start[0][0]+height//2,start[0][1]+height//2),(start[0][0],end[0][1]),(start[0][0]-height//2,start[0][1]+height//2)))

    
    if md == 'eq_triangle':
        print(f"({start[0]},({end[0][0]},{end[0][1]-height},({start[0][0]+width//2}{start[0][1]+height}))")
        if start[0][0] > end[0][0]:#left part
            if start[0][1] > end[0][1]:#top
                pygame.draw.polygon(screen,color,(start[0],(end[0][0],start[0][1]),(start[0][0]-width//2,start[0][1]-width)))
            elif start[0][1] < end[0][1]:#bot 
                pygame.draw.polygon(screen,color,(start[0],(end[0][0],start[0][1]),(start[0][0]-width//2,start[0][1]+width)))
        if start[0][0] < end[0][0]:#right part 
            if start[0][1] > end[0][1]:#top
                pygame.draw.polygon(screen,color,(start[0],(end[0][0],start[0][1]),(start[0][0]+width//2,start[0][1]-width)))
            elif start[0][1] < end[0][1]:#bot
                pygame.draw.polygon(screen,color,(start[0],(end[0][0],start[0][1]),(start[0][0]+width//2,start[0][1]+width)))
    if md=='rectangle' or md=='square':
        if md == 'square':
            if width>height:
                width = height
            else:
                height = width
        if start[0][0] > end[0][0]:#left part
            if start[0][1] > end[0][1]:#top
                pygame.draw.rect(screen,color,pygame.Rect(start[0][0]-width,start[0][1]-height,width,height))
            elif start[0][1] < end[0][1]:#bot 
                pygame.draw.rect(screen,color,pygame.Rect(start[0][0]-width,start[0][1],width,height))
        if start[0][0] < end[0][0]:#right part 
            if start[0][1] > end[0][1]:#top
                pygame.draw.rect(screen,color,pygame.Rect(start[0][0],start[0][1]-height,width,height))
            elif start[0][1] < end[0][1]:#left
                pygame.draw.rect(screen,color,pygame.Rect(start[0][0],start[0][1],width,height))
    if md =='circle':
        if start[0][0] > end[0][0]:#left part
            if start[0][1] > end[0][1]:#top
                pygame.draw.ellipse(screen,color,pygame.Rect(start[0][0]-width,start[0][1]-height,width,height))
            elif start[0][1] < end[0][1]:#bot 
                pygame.draw.ellipse(screen,color,pygame.Rect(start[0][0]-width,start[0][1],width,height))
        if start[0][0] < end[0][0]:#right part 
            if start[0][1] > end[0][1]:#top
                pygame.draw.ellipse(screen,color,pygame.Rect(start[0][0],start[0][1]-height,width,height))
            elif start[0][1] < end[0][1]:#left
                pygame.draw.ellipse(screen,color,pygame.Rect(start[0][0],start[0][1],width,height))
    if md == 'right_triangle':
        if start[0][0] > end[0][0]:#left part
            if start[0][1] > end[0][1]:#top
                pygame.draw.polygon(screen,color,(start[0],end[0],(start[0][0]-width,start[0][1])))
            elif start[0][1] < end[0][1]:#bot 
                pygame.draw.polygon(screen,color,(start[0],end[0],(start[0][0]-width,start[0][1])))
        if start[0][0] < end[0][0]:#right part 
            if start[0][1] > end[0][1]:#top
                pygame.draw.polygon(screen,color,(start[0],end[0],(start[0][0]+width,start[0][1])))
            elif start[0][1] < end[0][1]:#left
                pygame.draw.polygon(screen,color,(start[0],end[0],(start[0][0]+width,start[0][1])))
def draw_line(surface,pnt_list,index = 1):
    
    for pnt in pnt_list:
        if pnt[0] == 'blue':
            color = (0, 0, 255)
        elif pnt[0] == 'red':
            color = (255, 0, 0)
        elif pnt[0] == 'green':
            color = (0, 255, 0)
        elif pnt[0] == 'black':
            color = (0, 0, 0)
        start_pos,end_pos = pnt[1],pnt[1]
        for i in range(1,len(pnt)):
            start_pos = end_pos
            end_pos = pnt[i]
            
            pygame.draw.line(surface,color,start_pos,end_pos)

while True:
    screen.fill((0,0,0))
    pressed = pygame.key.get_pressed()
    mouse_state = pygame.mouse.get_pressed()
    
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and ctrl_held:
                pass
            if event.key == pygame.K_F4 and alt_held:
                pass
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'
            elif event.key == pygame.K_e:
                mode = 'black'
            
            if event.key == pygame.K_p:
                draw_mode = 'pen'
            elif event.key == pygame.K_c:
                draw_mode = 'circle'
            elif event.key == pygame.K_o:
                draw_mode = 'rectangle'
            elif event.key == pygame.K_s:
                draw_mode = 'square'
            elif event.key == pygame.K_t:
                draw_mode = 'right_triangle'
            elif event.key == pygame.K_l:
                draw_mode ='eq_triangle'
            elif event.key == pygame.K_q:
                draw_mode = "romb"
                
        if event.type == pygame.MOUSEMOTION and mouse_state[0] == True:
            position = event.pos
            if draw_mode == 'pen':
                if len(points)==0:
                    points.append (mode)

                points = points + [position]
                
                if points not in points_list:
                    if points != []:
                        points_list.append(points)
            if draw_mode == 'rectangle' or draw_mode == 'circle' or draw_mode == 'square' or draw_mode =='eq_triangle' or draw_mode=='romb' or draw_mode == "right_triangle":
                i = 1
                if len(rect_points)==0:
                    rect_points.append(mode)
                    rect_start = [position]
                    rect_points.append(draw_mode)
                    rect_points.append(rect_start)
                else:
                    rect_end = [position]
                    draw_rect(rect_start,rect_end,rect_points[0],rect_points[1])
        else:
            points = []
            if rect_start!=():
                
                if rect_points not in rect_list and rect_points!=[]:
                    rect_points.append(rect_end)
                    rect_list.append(rect_points)
                rect_points = []
                    
        print(rect_list)
        for cub in rect_list:
            draw_rect(cub[2],cub[3],cub[0],cub[1])
        draw_line(screen,points_list)
        
        pygame.display.flip()
        clock.tick(60)