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

def draw_board(screen, row, col, update):
    colors = [p.Color(240,216,191,255), p.Color(186,85,70,255)]
    for r in range(8):
        for c in range(8):
            color = colors[(r+c)%2]
            p.draw.rect(screen, color, p.Rect(c*(height//8), r*(width//8), (width//8), (height//8)))
    if update:
        if (row+col)%2 == 0:
            p.draw.rect(screen, p.Color(244,232,169,255), p.Rect(col*(height//8), row*(width//8), (width//8), (height//8)))
        else:
            p.draw.rect(screen, p.Color(217,167,108,255), p.Rect(col*(height//8), row*(width//8), (width//8), (height//8)))

def draw_pieces(screen, board):
    for r in range(8):
        for c in range(8):
            if board[r][c]:
                screen.blit(images[board[r][c].color + '_' + board[r][c].typ], p.Rect(c*(height//8), r*(width//8), (width//8), (height//8)))

def get_mouse_row_col(pos):
    row = pos[1]//(width//8)
    col = pos[0]//(width//8)
    return row, col

def move(board, row, col):
    pass                

if __name__ == "__main__":
    b = Board()
    # adding white pawns
    for j in range(8):
        b.board[6][j] = Pawn([6, j], 'white', 'pawn') # pos, color, typ)
    
    # adding blackk pawns
    for j in range(8):
        b.board[1][j] = Pawn([1, j], 'black', 'pawn')
    
    # adding white pieces
    b.board[7][0] = Rook([7, 0], 'white', 'rook')
    b.board[7][1] = Knight([7, 1], 'white', 'knight')
    b.board[7][2] = Bishop([7, 2], 'white', 'bishop')
    b.board[7][3] = Queen([7, 3], 'white', 'queen')
    b.board[7][4] = King([7, 4], 'white', 'king')
    b.board[7][5] = Bishop([7, 5], 'white', 'bishop')
    b.board[7][6] = Knight([7, 6], 'white', 'knight')
    b.board[7][7] = Rook([7, 7], 'white', 'rook')

    # adding black pieces
    b.board[0][0] = Rook([0, 0], 'black', 'rook')
    b.board[0][1] = Knight([0, 1], 'black', 'knight')
    b.board[0][2] = Bishop([0, 2], 'black', 'bishop')
    b.board[0][3] = Queen([0, 3], 'black', 'queen')
    b.board[0][4] = King([0, 4], 'black', 'king')
    b.board[0][5] = Bishop([0, 5], 'black', 'bishop')
    b.board[0][6] = Knight([0, 6], 'black', 'knight')
    b.board[0][7] = Rook([0, 7], 'black', 'rook')

    white = Player('white')
    white.is_turn_player = True
    black = Player('black')
    piece = None

    # b.board = b.board[6][4].move([5, 4], b.board)
    # if white.is_turn_player:
    #     white.is_turn_player, black.is_turn_player = False, True
    # else:
    #     white.is_turn_player, black.is_turn_player = True, False

    # b.board = b.board[1][4].move([2, 4], b.board)
    # if white.is_turn_player:
    #     white.is_turn_player, black.is_turn_player = False, True
    # else:
    #     white.is_turn_player, black.is_turn_player = True, False

    # b.board = b.board[7][2].move([5, 2], b.board)
    # if white.is_turn_player:
    #     white.is_turn_player, black.is_turn_player = False, True
    # else:
    #     white.is_turn_player, black.is_turn_player = True, False

    # b.board = b.board[0][3].move([4, 7], b.board)
    # if white.is_turn_player:
    #     white.is_turn_player, black.is_turn_player = False, True
    # else:
    #     white.is_turn_player, black.is_turn_player = True, False

    # player = white if white.is_turn_player else black
    # if not b.is_pinned(b.board[6][5], player, [5, 5]):
    #     b.board = b.board[6][5].move([5, 5], b.board)
    #     if white.is_turn_player:
    #         white.is_turn_player, black.is_turn_player = False, True
    #     else:
    #         white.is_turn_player, black.is_turn_player = True, False

    # p.init()
    # screen = p.display.set_mode((width, height))
    # p.display.set_caption('Chess')
    # load_images()
    # run = True
    # clock = p.time.Clock()
    
    # while run:
    #     draw_board(screen)
    #     draw_pieces(screen, b.board)
    #     clock.tick(FPS)
    #     p.display.flip()
    #     for event in p.event.get():
    #         if event.type == p.QUIT:
    #             run = False
    #         if event.type == p.KEYDOWN:
    #             if event.key == p.K_ESCAPE:
    #                 p.quit()
    

    p.init()
    screen = p.display.set_mode((width, height))
    p.display.set_caption('Chess')
    load_images()
    run = True
    clock = p.time.Clock()
    update = False
    row, col = 0, 0
    
    sq_selected = []
    player_clicks = []

    while run:
        draw_board(screen, row, col, update)
        draw_pieces(screen, b.board)
        clock.tick(FPS)
        p.display.flip()
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.quit()
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                row, col = get_mouse_row_col(pos)
                if b.board[row][col]:
                    if (b.board[row][col].color == white.color and white.is_turn_player) or (b.board[row][col].color == black.color and black.is_turn_player):
                        piece = b.board[row][col]
                        update = True

                if sq_selected == [row, col]: # the user clicked the same square twice
                    sq_selected = [] # deselect
                    player_clicks = [] # clear player clicks
                else:
                    sq_selected = [row, col]
                    player_clicks.append(sq_selected) # append for both 1st and 2nd clicks
                    if (not piece and len(player_clicks) == 1):
                        sq_selected = [] # deselect
                        player_clicks = [] # clear player clicks
                        update = False
                    if len(player_clicks) == 2: # after 2nd click
                        if b.board[player_clicks[0][0]][player_clicks[0][1]] and b.board[player_clicks[1][0]][player_clicks[1][1]] and b.board[player_clicks[0][0]][player_clicks[0][1]].color == b.board[player_clicks[1][0]][player_clicks[1][1]].color:
                            sq_selected = [] # deselect
                            player_clicks = [] # clear player clicks
                            update = False
                            continue
                        if piece:
                            player = white if piece.color == white.color else black
                            row, col = player_clicks[1][0], player_clicks[1][1]
                            if [row, col] in piece.get_possible_moves(b.board) and not b.is_pinned(piece, player, [row, col]):
                                b.board = piece.move([row, col], b.board)
                                update = False
                                if white.is_turn_player:
                                    white.is_turn_player, black.is_turn_player = False, True
                                else:
                                    white.is_turn_player, black.is_turn_player = True, False
                        piece = None
                        sq_selected = [] # deselect
                        player_clicks = [] # clear player clicks
                        update = False
                        # continue
            
        # draw_board(screen)
        # draw_pieces(screen, b.board)
        # clock.tick(FPS)
        # p.display.flip()
    