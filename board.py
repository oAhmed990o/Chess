from numpy import choose


class Board:
    def __init__(self):
        self.board = [[None]*8 for i in range(8)]
        self.white_king = [7, 4]
        self.black_king = [0, 4]

    def choose_promotion(self, color):
        # make palyer choose promotion through pygame then return the selected promotion
        pass

    def promote(self, player):
        board = self.board
        color = player.color
        i = 0 if color == 'white' else 7
        for j in range(8):
            if board[i][j]:
                if board[i][j].typ == 'pawn':
                    self.board[i][j] = self.choose_promotion(color)
    
    # To be tested
    def can_king_be_protected(self, player):
        # king = self.white_king if player.color == 'white' else self.black_king
        color = player.color
        board = self.board
        player_pieces = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] and board[i][j].color == color:
                    player_pieces.append(board[i][j])
                    
        for piece in player_pieces: # is possible to call piece functions without passing it a parameter?
            moves = piece.get_possible_moves(board)
            for new_pos in moves:
                if piece.move(new_pos).under_check(player):
                    return False
        return True


    def checkmate(self, player):
        board = self.board
        if self.under_check(player, board) and not self.can_king_be_protected(player, board):
            return True
        return False

    # to be tested
    def stalemate(self, player):
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

    # TODO
    def end_game(self, player):
        board = self.board
        if self.checkmate(player, board):
            # end pygame session and display msg that it's a checkmate
            pass
        elif self.stalemate(player, board):
            # end pygame session and display msg that it's a stalemate
            pass

    # TODO
    def can_en_passant(self):
        pass

    def under_check(self, player):
        if player.color == 'white':
            x, y = self.white_king[0], self.white_king[1]
        else:
            x, y = self.black_king[0], self.black_king[1]

        b = self.board
        # check for pawns
        if player.color == 'white':
            if x-1 >=0 and x-1 <8:
                if y-1 >=0 and y-1 < 8:
                    if player.color != b[x-1][y-1].color and b[x-1][y-1].typ == 'pawn':
                        return True
                if y+1 >=0 and y+1 < 8:
                    if player.color != b[x-1][y+1].color and b[x-1][y+1].typ == 'pawn':
                        return True
        else:
            if x+1 >=0 and x+1 <8:
                if y-1 >=0 and y-1 < 8:
                    if player.color != b[x+1][y-1].color and b[x+1][y-1].typ == 'pawn':
                        return True
                if y+1 >=0 and y+1 < 8:
                    if player.color != b[x+1][y+1].color and b[x+1][y+1].typ == 'pawn':
                        return True

        # check for knights
        for curr_x, curr_y in [[x-2, y-1], [x-2, y+1], [x-1, y-2], [x-1, y+2], [x+1, y-2], [x+1, y+2], [x+2, y-1], [x+2, y+1]]:
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and b[curr_x][curr_y].typ == 'knight':
                        return True

        # up_right, check for bishops and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_x -= 1
            curr_y += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        # down_left, check for bishops and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_x += 1
            curr_y -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        # up_left, check for bishops and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_x -= 1
            curr_y -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        # down_right, check for bishops and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_x += 1
            curr_y += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'bishop' or b[curr_x][curr_y].typ == 'queen'):
                        return True
        
        # up, check for rooks and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_x -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        # down, check for rooks and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_x += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        # left, check for rooks and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_y -= 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        # right, check for rooks and queens
        curr_x, curr_y = x, y
        for i in range(8):
            curr_y += 1
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if b[curr_x][curr_y]:
                    if player.color != b[curr_x][curr_y].color and (b[curr_x][curr_y].typ == 'rook' or b[curr_x][curr_y].typ == 'queen'):
                        return True

        return False

    def is_pinned(self, piece, player):
        temp_board = self.board
        temp_board[piece.pos[0]][piece.pos[1]] = None
        return True if self.under_check(player, temp_board) else False