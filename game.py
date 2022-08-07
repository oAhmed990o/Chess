from piece import Piece
from king import King
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight
from pawn import Pawn
from board import Board
from player import Player
import pygame as p

images = {}
width, height = 896, 896
FPS = 60

def load_images():
    pieces = ['white_pawn', 'white_knight', 'white_bishop', 'white_rook', 'white_queen', 'white_king', 
    'black_pawn', 'black_knight', 'black_bishop', 'black_rook', 'black_queen', 'black_king']
    # load pieces
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load('art/' + piece + '.png'), (width//8, height//8))

def draw_board(screen):
    colors = [p.Color(240,216,191,255), p.Color(186,85,70,255)]
    for r in range(8):
        for c in range(8):
            color = colors[(r+c)%2]
            p.draw.rect(screen, color, p.Rect(c*(height//8), r*(width//8), (width//8), (height//8)))

def draw_pieces(screen, board):
    for r in range(8):
        for c in range(8):
            if board[r][c]:
                screen.blit(images[board[r][c].color + '_' + board[r][c].typ], p.Rect(c*(height//8), r*(width//8), (width//8), (height//8)))
                

if __name__ == "__main__":
    b = Board()
    # adding white pawns
    for j in range(8):
        b.board[6][j] = Pawn([6, j], 'white', 'pawn') # pos, color, typ)
    
    # adding balck pawns
    for j in range(8):
        b.board[1][j] = Pawn([1, j], 'black', 'pawn')
    
    # adding white pieces
    b.board[7][0] = Rook([7, 0], 'white', 'rook')
    b.board[7][1] = Bishop([7, 1], 'white', 'bishop')
    b.board[7][2] = Knight([7, 2], 'white', 'knight')
    b.board[7][3] = Queen([7, 3], 'white', 'queen')
    b.board[7][4] = King([7, 4], 'white', 'king')
    b.board[7][5] = Knight([7, 5], 'white', 'knight')
    b.board[7][6] = Bishop([7, 6], 'white', 'bishop')
    b.board[7][7] = Rook([7, 7], 'white', 'rook')

    # adding black pieces
    b.board[0][0] = Rook([0, 0], 'black', 'rook')
    b.board[0][1] = Bishop([0, 1], 'black', 'bishop')
    b.board[0][2] = Knight([0, 2], 'black', 'knight')
    b.board[0][3] = Queen([0, 3], 'black', 'queen')
    b.board[0][4] = King([0, 4], 'black', 'king')
    b.board[0][5] = Knight([0, 5], 'black', 'knight')
    b.board[0][6] = Bishop([0, 6], 'black', 'bishop')
    b.board[0][7] = Rook([0, 7], 'black', 'rook')
    
    # for i in range(8):
    #     for j in range(8):
    #         if b.board[i][j]:
    #             print(b.board[i][j].typ, end = ' ')
    #         else:
    #             print('None', end = ' ')
    #     print('\n')

    p.init()
    screen = p.display.set_mode((width, height))
    p.display.set_caption('Chess')
    load_images()
    run = True
    clock = p.time.Clock()
    while run:
        draw_board(screen)
        draw_pieces(screen, b.board)
        clock.tick(FPS)
        p.display.flip()
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.quit()