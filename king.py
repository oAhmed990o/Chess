from piece import Piece

class King(Piece):
    def __init__(self, pos, color, typ):
        super().__init__(pos, color, typ)
    
    has_moved = False

    def can_castle(self):
        pass

    # def castle(self):
    #     pass

    def get_possible_moves(self, board):
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