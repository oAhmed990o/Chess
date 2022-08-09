# from abc import ABC, abstractmethod
# class Piece(ABC):

class Piece():
    def __init__(self, pos, color, typ):
        self.pos = pos
        self.color = color
        self.typ = typ
    
    # def is_king(self):
    #     return True if self.typ == 'king' else False

    # def can_move(self):
    #     pass

    # @abstractmethod
    def get_possible_moves(self, board):
        pass

    def move(self, new_pos, board): # return board and don't modify a class board
        board[new_pos[0]][new_pos[1]] = board[self.pos[0]][self.pos[1]]
        board[self.pos[0]][self.pos[1]] = None
        self.pos = new_pos
        return board