from tictactoe import *

size = 600
board = Board(size)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            (posX, posY) = pygame.mouse.get_pos()
            row = posY//(size//3)
            col = posX//(size//3)
            #get row and col number
            done = board.step(row, col)
            if done:
                break
    board.render()

print('endgame')
board.endGame()