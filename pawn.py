from piece import Piece

class Pawn:
    def __init__(self, pos, color, typ):
        super().__init__(pos, color, typ)

    has_moved = False
    # has_moved_two_squares = False

    def can_en_passant(self, board):
        pass

    def en_passant(self, board):
        pass

    def get_possible_moves(self, board):
        moves = []
        x, y = self.pos[0], self.pos[1]

        step = -1 if self.color == 'white' else 1
        
        # two squares forward
        if not self.has_moved:
            if board[x+step][y] is None and board[x+step*2][y] is None:
                moves.append([x+step*2, y])

        # if can en-passant
        if self.can_en_passant(board):
            moves.append(self.en_passant, board)

        # if can take
        if x+step >= 0 and y-1 >= 0 and x+step < 8 and y-1 < 8:
            if board[x+step][y-1] and self.color != board[x+step][y-1].color:
                moves.append([x+step, y-1])
        
        if x+step >= 0 and y+1 >= 0 and x+step < 8 and y+1 < 8:
            if board[x+step][y+1] and self.color != board[x+step][y+1].color:
                moves.append([x+step, y+1])

        # one step forward
        if x+step >= 0 and y >= 0 and x+step < 8 and y < 8:
            if board[x+step][y] is None:
                moves.append([x+step, y])

        return moves