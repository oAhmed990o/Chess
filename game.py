import copy
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

def promote(board, pos, type):
    x, y = pos
    color = board[x][y].color
    if type.lower() == 'q':
         promoted = Queen([x, y], color, 'queen')
    elif type.lower() == 'n':
        promoted = Knight([x, y], color, 'knight')
    elif type.lower() == 'r':
        promoted = Rook([x, y], color, 'rook')
    elif type.lower() == 'b':
        promoted = Bishop([x, y], color, 'bishop')
    else:
        return
    board[x][y] = promoted
    return board

def key_to_char(key):
    if key == p.K_q:
        return 'q'
    if key == p.K_n:
        return 'n'
    if key == p.K_r:
        return 'r'
    if key == p.K_b:
        return 'b'
    else:
        return ''

def draw_text(screen, font_size, text):
    font = p.font.SysFont('Cairo', font_size, True, False)
    text_object = font.render(text, 0, p.Color('Black'))
    text_location = p.Rect(0, 0, width, height).move(width/2 - text_object.get_width()/2, height/2 - text_object.get_height()/2)
    screen.blit(text_object, text_location)

def switch_players(white):
    if white.is_turn_player:
        return [False, True]
    else:
        return [True, False]

def board_to_string(board):
    ans = []
    for i in range(8):
        for j in range(8):
            if not board[i][j]:
                ans.append('..')
                continue
            color = 'w' if board[i][j].color == 'white' else 'b'
            if board[i][j].typ == 'pawn':
                ans.append(color + 'p')
            elif board[i][j].typ == 'bishop':
                ans.append(color + 'b')
            elif board[i][j].typ == 'knight':
                ans.append(color + 'n')
            elif board[i][j].typ == 'rook':
                ans.append(color + 'r')
            elif board[i][j].typ == 'queen':
                ans.append(color + 'q')
            elif board[i][j].typ == 'king':
                ans.append(color + 'k')
    return ''.join(ans)

def quit_game(text):
    while 1:
        draw_text(screen, 64, text)
        p.display.update()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.quit()

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

    board_stack = []
    board_count = {}

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
    
    fifty_move_rule = 0
    num_pieces = 32
    has_any_pawn_moved = False

    while run:

        draw_board(screen, row, col, update)
        draw_pieces(screen, b.board)
        clock.tick(FPS)
        p.display.flip()

        player = white if white.is_turn_player else black
        if len(board_stack):
            if b.checkmate(player, board_stack[-1][0], b.board):
                color = 'White' if player.color == 'black' else 'Black'
                quit_game(color + ' wins by checkmate')

        if b.stalemate(player, b.board):
            quit_game('Stalemate')

        curr_piece_count = 0
        white_pieces, black_pieces = [], []
        for i in range(8):
            for j in range(8):
                if b.board[i][j] and b.board[i][j].color == 'white':
                    white_pieces.append(b.board[i][j])
                elif b.board[i][j] and b.board[i][j].color == 'black':
                    black_pieces.append(b.board[i][j])
        
        if b.insuficient_material(white_pieces, black_pieces):
            quit_game('Draw due to insuficient material')
        
        if fifty_move_rule == 100:
            quit_game('Draw due to no progress')

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    p.quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_z and p.key.get_mods() & p.KMOD_LCTRL:
                    if len(board_stack):
                        b.board, [fifty_move_rule, curr_piece_count, has_any_pawn_moved] = board_stack.pop()
                        print(fifty_move_rule, curr_piece_count, has_any_pawn_moved)
                    update = False
                    white.is_turn_player, black.is_turn_player = switch_players(white)

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
                            row, col = player_clicks[1][0], player_clicks[1][1]
                            if [row, col] in piece.get_possible_moves(b.board) and not b.is_pinned(piece, player, [row, col]):
                                board_stack.append([copy.deepcopy(b.board), [fifty_move_rule, curr_piece_count, has_any_pawn_moved]])
                                board_count[board_to_string(b.board)] = board_count.get(board_to_string(b.board), 0) + 1
                                
                                b.board = piece.move([row, col], b.board)

                                if board_count.get(board_to_string(b.board)) and board_count[board_to_string(b.board)] == 2:
                                    quit_game('Draw by repetition')
                                
                                if piece.typ == 'pawn':
                                    has_any_pawn_moved = True
                                    if (piece.color == 'white' and row == 0) or (piece.color == 'black' and row == 7):
                                        out = None
                                        while not out:
                                            draw_text(screen, 40, 'Choose promotion q: Queen  n: Knight  r: Rook  b: Bishop')
                                            p.display.update()
                                            for event in p.event.get():
                                                if event.type == p.KEYDOWN:
                                                    out = promote(b.board, [row, col], key_to_char(event.key))
                                                    if out:
                                                        b.board = out
                                                        break

                                curr_piece_count = 0
                                for i in range(8):
                                    for j in range(8):
                                        if b.board[i][j]:
                                            curr_piece_count += 1
                                if num_pieces == curr_piece_count and not has_any_pawn_moved:
                                    fifty_move_rule += 1

                                if has_any_pawn_moved or (num_pieces != curr_piece_count):
                                    fifty_move_rule = 0 # incremented if the same number of pieces remains
                                    has_any_pawn_moved = False # if a pawn moves it's set to true
                                    num_pieces = curr_piece_count # changes only if curr_piece_count is different
                                            
                                update = False
                                white.is_turn_player, black.is_turn_player = switch_players(white)

                            elif piece.typ == 'king':
                                
                                out = piece.castle(player, b, [row, col])
                                if out:
                                    board_stack.append([copy.deepcopy(b.board), [fifty_move_rule, curr_piece_count, has_any_pawn_moved]])
                                    board_count[board_to_string(b.board)] = board_count.get(board_to_string(b.board), 0) + 1
                                    
                                    b.board = out
                                    if board_count.get(board_to_string(b.board)) and board_count[board_to_string(b.board)] == 2:
                                        quit_game('Draw by repetition')
                                    
                                    curr_piece_count = 0
                                    for i in range(8):
                                        for j in range(8):
                                            if b.board[i][j]:
                                                curr_piece_count += 1
                                    if num_pieces == curr_piece_count and not has_any_pawn_moved:
                                        fifty_move_rule += 1

                                    if has_any_pawn_moved or (num_pieces != curr_piece_count):
                                        fifty_move_rule = 0 # incremented if the same number of pieces remains
                                        has_any_pawn_moved = False # if a pawn moves it's set to true
                                        num_pieces = curr_piece_count # changes only if curr_piece_count is different

                                    update = False
                                    white.is_turn_player, black.is_turn_player = switch_players(white)

                            elif piece.typ == 'pawn' and len(board_stack) > 0:
                                out = piece.en_passant(board_stack[-1][0], b.board, [row, col])
                                if out and not b.is_pinned(piece, player, [row, col]):
                                    has_any_pawn_moved = True 
                                    board_stack.append([copy.deepcopy(b.board), [fifty_move_rule, curr_piece_count, has_any_pawn_moved]])
                                    board_count[board_to_string(b.board)] = board_count.get(board_to_string(b.board), 0) + 1
                                    
                                    b.board = out
                                    if board_count.get(board_to_string(b.board)) and board_count[board_to_string(b.board)] == 2:
                                        quit_game('Draw by repetition')
                                    
                                    curr_piece_count = 0
                                    for i in range(8):
                                        for j in range(8):
                                            if b.board[i][j]:
                                                curr_piece_count += 1
                                    if num_pieces == curr_piece_count and not has_any_pawn_moved:
                                        fifty_move_rule += 1

                                    if has_any_pawn_moved or (num_pieces != curr_piece_count):
                                        fifty_move_rule = 0 # incremented if the same number of pieces remains
                                        has_any_pawn_moved = False # if a pawn moves it's set to true
                                        num_pieces = curr_piece_count # changes only if curr_piece_count is different

                                    update = False
                                    white.is_turn_player, black.is_turn_player = switch_players(white)

                        piece = None
                        sq_selected = [] # deselect
                        player_clicks = [] # clear player clicks
                        update = False