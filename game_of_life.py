import pygame
from random import randint

fenster = pygame.display.set_mode([1920, 1080])
fenster.fill((100,100,100))



class Node:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.value = 0




class Board:

    def __init__(self , rows , columns):
        self._rows = rows
        self._columns = columns   
        self._grid = [[Node(row_cells,column_cells) for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._generate_board()

    def draw_board(self):
        for x in range(self._rows):
            for y in range(self._columns):
                pygame.draw.rect(fenster, self._grid[x][y].color, pygame.Rect(x*5, y*5, 5, 5))

        pygame.display.update()


    def _generate_board(self):
        for row in self._grid:
            for column in row:
                chance_number = randint(0,10)
                if chance_number == 1:
                    column.color = (244, 244, 244)
                    column.value = 1


    def check_status(self):
        
        grid = self._grid.copy()
        amount_of_neighbours = 0

        for i in range(self._rows):
            for j in range(self._columns):
    
                total = grid[i][(j-1)%self._columns].value \
                    + grid[i][(j+1)%self._columns].value + grid[(i-1)%self._rows][j].value + grid[(i+1)%self._rows][j].value \
                    + grid[(i-1)%self._rows][(j-1)%self._columns].value + grid[(i-1)%self._rows][(j+1)%self._columns].value \
                    + grid[(i+1)%self._rows][(j-1)%self._columns].value + grid[(i+1)%self._rows][(j+1)%self._columns].value
        
        


                if grid[i][j].value == 1:
                    if (total < 2) or (total > 3):
                        self._grid[i][j].value = 0
                        self._grid[i][j].color = (0, 0, 0)
                else:
                    if total == 3:
                        self._grid[i][j].value = 1
                        self._grid[i][j].color = (244, 244, 244)
       
    
  
    

    
    
    


clock = pygame.time.Clock()
running = True
board = Board(384, 216)
paused = False
while running:

    if not paused:
        clock.tick(10)
        board.draw_board()
        board.check_status()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.display.set_caption("Paused")
                paused = not paused