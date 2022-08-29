from piece import Piece

class King(Piece):
    def __init__(self, pos, color, typ):
        super().__init__(pos, color, typ)

    def castle(self, player, board, position):
        if abs(self.pos[1] - position[1]) != 2 or self.has_moved:
            return
        b = board.board
        x, y = position

        if position[1] < self.pos[1]: # long castling
            if b[x][y-2] and b[x][y-2].typ == 'rook' and (not b[x][y-2].has_moved) and b[x][y-2].color == self.color:
                for i in range(self.pos[1]-1, 0, -1):
                    if board.is_square_unsafe(player, [x , i]):
                        return
                if board.under_check(player, b):
                    return
                else:
                    # do the castling
                    # change the saved king pos int he board constructor later*
                    b[x][y] = self
                    b[self.pos[0]][self.pos[1]] = None
                    self.pos = [x, y]
                    self.has_moved = True
                    b[x][y+1] = b[x][y-2] # move the rook
                    b[x][y-2] = None
                    b[x][y+1].pos = [x, y+1]
                    b[x][y+1].has_moved = True
                    return b
            else:
                return
        else: # short castling
            if b[x][y+1] and b[x][y+1].typ == 'rook' and (not b[x][y+1].has_moved) and b[x][y+1].color == self.color:
                for i in range(self.pos[1]+1, 7):
                    if board.is_square_unsafe(player, [x , i]):
                        return
                if board.under_check(player, b):
                    return
                else:
                    # do the castling
                    # change the saved king pos int he board constructor later*
                    b[x][y] = self
                    b[self.pos[0]][self.pos[1]] = None
                    self.pos = [x, y]
                    self.has_moved = True
                    b[x][y-1] = b[x][y+1] # move the rook
                    b[x][y+1] = None
                    b[x][y-1].pos = [x, y-1]
                    b[x][y-1].has_moved = True
                    return b
            else:
                return


    def get_possible_moves(self, board, reverse):
        moves = []
        x, y = self.pos[0], self.pos[1]
        for curr_x, curr_y in [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]:
            if curr_x >= 0 and curr_y >= 0 and curr_x < 8 and curr_y < 8:
                if board[curr_x][curr_y] is None:
                    moves.append([curr_x, curr_y])
                else:
                    if self.color != board[curr_x][curr_y].color:
                        moves.append([curr_x, curr_y])
                    # should I specify that I can take?
        return moves