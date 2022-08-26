import copy

class Board:
    def __init__(self):
        self.board = [[None]*8 for i in range(8)]
        self.white_king = [7, 4]
        self.black_king = [0, 4]

    def check_for_knights(self, player, b, x, y):
        for curr_x, curr_y in [[x-2, y-1], [x-2, y+1], [x-1, y-2], [x-1, y+2], [x+1, y-2], [x+1, y+2], [x+2, y-1], [x+2, y+1]]:
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ == 'knight':
                        return True
        return False

    def check_for_bishops_queens_up_right(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_x -= 1
            curr_y += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'bishop' and b[curr_x][curr_y].typ != 'queen':
                        break 
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_bishops_queens_down_left(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_x += 1
            curr_y -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'bishop' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False
    
    def check_for_bishops_queens_up_left(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_x -= 1
            curr_y -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'bishop' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_bishops_queens_down_right(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_x += 1
            curr_y += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'bishop' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_rooks_queens_up(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_x -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'rook' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_rooks_queens_down(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_x += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'rook' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_rooks_queens_left(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_y -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'rook' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_rooks_queens_right(self, player, b, curr_x, curr_y):
        for i in range(8):
            curr_y += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color == b[curr_x][curr_y].color:
                        break
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ != 'rook' and b[curr_x][curr_y].typ != 'queen':
                        break
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        return False

    def check_for_pawns(self, player, b, x, y):
        if player.color == 'white':
            if x-1 >=0 and x-1 <8:
                if y-1 >=0 and y-1 < 8 and b[x-1][y-1]:
                    if player.color != b[x-1][y-1].color and b[x-1][y-1].typ == 'pawn':
                        return True
                if y+1 >=0 and y+1 < 8 and b[x-1][y+1]:
                    if player.color != b[x-1][y+1].color and b[x-1][y+1].typ == 'pawn':
                        return True
        else:
            if x+1 >=0 and x+1 <8:
                if y-1 >=0 and y-1 < 8 and b[x+1][y-1]:
                    if player.color != b[x+1][y-1].color and b[x+1][y-1].typ == 'pawn':
                        return True
                if y+1 >=0 and y+1 < 8 and b[x+1][y+1]:
                    if player.color != b[x+1][y+1].color and b[x+1][y+1].typ == 'pawn':
                        return True
        return False

    def check_for_king(self, player, b, x, y):
        positions = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y],  [x+1, y+1]]
        for curr_x, curr_y in positions:
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ == 'king':
                        return True
        return False

    def threat_exists(self, player, b, x, y):
        # check for pawns
        if self.check_for_pawns(player, b, x, y):
            return True

        # check for knights
        if self.check_for_knights(player, b, x, y):
            return True

        # up_right, check for bishops and queens
        if self.check_for_bishops_queens_up_right(player, b, x, y):
            return True

        # down_left, check for bishops and queens
        if self.check_for_bishops_queens_down_left(player, b, x, y):
            return True

        # up_left, check for bishops and queens
        if self.check_for_bishops_queens_up_left(player, b, x, y):
            return True

        # down_right, check for bishops and queens
        if self.check_for_bishops_queens_down_right(player, b, x, y):
            return True
        
        # up, check for rooks and queens
        if self.check_for_rooks_queens_up(player, b, x, y):
            return True

        # down, check for rooks and queens
        if self.check_for_rooks_queens_down(player, b, x, y):
            return True
        
        # left, check for rooks and queens
        if self.check_for_rooks_queens_left(player, b, x, y):
            return True
        
        # right, check for rooks and queens
        if self.check_for_rooks_queens_right(player, b, x, y):
            return True
        
        # check for a king
        if self.check_for_king(player, b, x, y):
            return True
        
        return False

    def can_king_be_protected(self, player, flashback, board):
        # king = self.white_king if player.color == 'white' else self.black_king
        color = player.color
        player_pieces = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] and board[i][j].color == color:
                    player_pieces.append(board[i][j])
                    
        for piece in player_pieces: # is possible to call piece functions without passing it a parameter?
            moves = piece.get_possible_moves(board)
            
            for new_pos in moves:
                b = copy.deepcopy(board)
                p = copy.deepcopy(piece)
                if not self.under_check(player, p.move(new_pos, b)):
                    return True

                # add casling and en-passant to the move options
                if p.typ == 'king':
                    out = p.castle(player, board, new_pos)
                    if out and not self.under_check(player, p.castle(player, board, new_pos)):
                        return True

                if p.typ == 'pawn':
                    out = p.en_passant(flashback, board, new_pos)
                    if out and not self.under_check(player, p.en_passant(flashback, board, new_pos)):
                        return True
        return False


    def checkmate(self, player, flashback, board): 
        if self.under_check(player, board) and not self.can_king_be_protected(player, flashback, board):
            return True
        return False

    # to be tested
    def stalemate(self, player, board):
        board = self.board
        if not self.under_check(player, board):
            color = player.color
            player_pieces = []
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] and board[i][j].color == color:
                        player_pieces.append(board[i][j])
                        
            for piece in player_pieces: # is possible to call piece functions without passing it a parameter?
                if piece.get_possible_moves(board):
                    return False
            return True
        return False

    def is_square_unsafe(self, player, pos):
        x, y = pos
        b = self.board

        if self.threat_exists(player, b, x, y):
            return True
    
        return False

    def under_check(self, player, board):
        # if player.color == 'white': # as I use a temporary board, king position might change, so using the saved pos is incorrect, pass it as parameter if you can
        #     x, y = self.white_king[0], self.white_king[1]
        # else:
        #     x, y = self.black_king[0], self.black_king[1]

        for i in range(8):
            for j in range(8):
                if board[i][j] and board[i][j].typ == 'king' and board[i][j].color == player.color:
                    x, y = board[i][j].pos[0], board[i][j].pos[1]
                    break
                    
        b = board
        
        if self.threat_exists(player, b, x, y):
            return True

        return False

    def is_pinned(self, piece, player, new_pos):
        temp_board = copy.deepcopy(self.board)
        temp_board[new_pos[0]][new_pos[1]] = piece
        temp_board[piece.pos[0]][piece.pos[1]] = None
        old_pos = piece.pos
        piece.pos = new_pos
        if self.under_check(player, temp_board):
            piece.pos = old_pos
            return True
        else:
            piece.pos = old_pos
            return False