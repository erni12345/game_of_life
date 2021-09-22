import pygame
from random import randint

fenster = pygame.display.set_mode([1920, 1080])
fenster.fill((100,100,100))



def create_rec(lst):
    for x in range(len(lst)):
        for y in range(len(lst[0])):

            if lst[x][y] == 1:
                pygame.draw.rect(fenster, (244, 244, 244), pygame.Rect(x*10, y*10, 10, 10))
            else:
                pygame.draw.rect(fenster, (0, 0, 0), pygame.Rect(x*10, y*10, 10, 10))

    pygame.display.update()

 


    
    
def check_status(lst, x, y):
    
    amount_of_neighbours = 0

    if x > 0:
        if lst[x-1][y] == 1:
            amount_of_neighbours += 1
    if x < len(lst)-1:
        if lst[x+1][y] == 1:
            amount_of_neighbours += 1
    if y > 0:
        if lst[x][y-1] == 1:
            amount_of_neighbours += 1
    if y < len(lst[0])-1:
        if lst[x][y+1]== 1:
            amount_of_neighbours += 1
    if x > 0 and y < len(lst[0])-1:
        if lst[x-1][y+1]== 1:
            amount_of_neighbours += 1
    if x > 0 and y > 0:
        if lst[x-1][y-1]== 1:
            amount_of_neighbours += 1
    if x < len(lst)-1 and y < len(lst[0])-1:
        if lst[x+1][y+1]== 1:
            amount_of_neighbours += 1
    if x < len(lst)-1 and y > 0:
        if lst[x+1][y-1]== 1:
            amount_of_neighbours += 1
    
    


    check_dic_1 = {0:False, 1: False, 2:True, 3:True, 4:False,5:False,6:False,7:False,8:False,}
    if lst[x][y] == 1:
        return check_dic_1[amount_of_neighbours]
    else:
        if amount_of_neighbours == 3:
            return True
        else:
            return False
        



def update_grid(lst):

    og = [[x for x in y] for y in lst]

    for x in range(len(lst)):
        for y in range(len(lst)):
            if check_status(og, x, y):
                lst[x][y] = 1
            else:
                lst[x][y] = 0
    return lst
    
    
    




clock = pygame.time.Clock()
running = True
display_list = [[randint(0,1) for x in range(108)] for x in range(108)]
while running:
    clock.tick(250)
    create_rec(display_list)
    display_list = update_grid(display_list)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False