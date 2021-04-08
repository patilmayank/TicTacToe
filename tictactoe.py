import pygame
import time

class Board:
    def __init__(self, screenSize):
        pygame.init()
        pygame.font.init()
        self.screenSize = screenSize
        self.margin = screenSize // 20
        self.screen = pygame.display.set_mode((screenSize, screenSize))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self.turn = "X"
        self.board = [
            [None, None, None], 
            [None, None, None], 
            [None, None, None]
            ]
    
    def reset(self):
        self.board = [
            [None, None, None], 
            [None, None, None], 
            [None, None, None]
            ]
        self.turn = "X"
        return self.board
        
        
    def step(self, row, col):
        if self.board[row][col] != None:
            return False
            
        self.board[row][col] = self.turn
        
        if (
            # Vertical columns
            self.board[0][0] == self.board[0][1] == self.board[0][2] == self.turn or 
            self.board[1][0] == self.board[1][1] == self.board[1][2] == self.turn or 
            self.board[2][0] == self.board[2][1] == self.board[2][2] == self.turn or 
            # Horizontal Rows
            self.board[0][0] == self.board[1][0] == self.board[2][0] == self.turn or
            self.board[0][1] == self.board[1][1] == self.board[2][1] == self.turn or
            self.board[0][2] == self.board[1][2] == self.board[2][2] == self.turn or 
            # Diagonals
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.turn or 
            self.board[2][0] == self.board[1][1] == self.board[0][2] == self.turn
            ):
            self.winner = self.turn
            return True

        if all(self.board[0] + self.board[1] + self.board[2]):
            self.winner = "Neither"
            return True

        # Next turn
        if self.turn=="X":
            self.turn = "O"
        else:
            self.turn = "X"
        return False
            

    def drawItem(self, row, col, item):
        squareSize = self.screenSize//3
        TL = (squareSize*col + self.margin, squareSize*row + self.margin)
        thickness = self.screenSize//60

        if item is None:
            return
        
        elif item == 'X':
            BL = (squareSize*col + self.margin, squareSize*(row+1) - self.margin)
            TR = (squareSize*(col+1) - self.margin, squareSize*(row) + self.margin)
            BR = (squareSize*(col+1) - self.margin, squareSize*(row+1) - self.margin)
            pygame.draw.line(self.screen, (0,0,255), TL, BR, thickness)
            pygame.draw.line(self.screen, (0,0,255), TR, BL, thickness)
              
        elif item == "O":
            circleSize = squareSize-1.75*self.margin
            pygame.draw.ellipse(self.screen, (255,0,0), (TL[0],TL[1], circleSize, circleSize), thickness)

    def render(self):

        self.screen.fill((51, 51, 51))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # self.board --> [['X', None, 'O'], ['O', None, None], [None, None, None]]
        for row in range(3):
            for col in range(3):
                item = self.board[row][col]
                self.drawItem(row, col, item)

        pygame.display.flip()

    def endGame(self):
        while True:
            self.screen.fill((51, 51, 51))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if self.winner == "X":
                self.screen.fill((0, 0, 255))
            elif self.winner == "O":
                self.screen.fill((255, 0, 0))
            else:
                self.screen.fill((255, 0, 255))
                
            textsurface = self.myfont.render(self.winner + ' is the Winner!', False, (0, 0, 0))
            screen_rect = self.screen.get_rect()
            surf_rect = textsurface.get_rect(center=screen_rect.center)

            self.screen.blit(textsurface, surf_rect)

            # self.screen.blit(textsurface,(self.screenSize//2,self.screenSize//2))

            pygame.display.flip()