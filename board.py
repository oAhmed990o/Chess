class Board:
    def __init__(self):
        self.board = [[None]*8 for i in range(8)]
        self.white_king = [7, 4]
        self.black_king = [0, 4]

    # TODO
    def promote(self, player):
        i = 0 if player.color == 'white' else 7
        for j in range(8):
            if self.board[i][j]:
                if self.board[i][j].typ == 'pawn':
                    # choose promotion
                    # self.board[i][j] =
                    pass
    
    # TODO
    def can_king_be_protected(self, player, board):
        king = self.white_king if player.color == 'white' else self.black_king
        return False


    def checkmate(self, player, board):
        if self.under_check(player, board) and not self.can_king_be_protected(player, board):
            return True
        return False

    # TODO
    def stalemate(self, player, board):
        if not self.under_check(player, board):
            pass
        return True

    def end_game(self, player, board):
        if self.checkmate(player, board):
            pass
        elif self.stalemate(player, board):
            pass

    # def en_passant(self):
    #     pass

    def under_check(self, player, board):
        if player.color == 'white':
            x, y = self.white_king[0], self.white_king[1]
        else:
            x, y = self.black_king[0], self.black_king[1]

        b = board
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