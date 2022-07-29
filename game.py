from piece import Piece
from bishop import Bishop
from king import King

if __name__ == "__main__":
    b = Bishop([4, 5], 'black', 'bishop')
    b2 = Bishop([2, 7], 'black', 'bishop')
    bw = Bishop([6, 3], 'white', 'bishop')
    board = [[None]*8 for i in range(8)]
    board[4][5] = b
    board[2][7] = b2
    board[6][3] = bw
    print(b.get_possible_moves(board))
    # b.get_possible_moves(board)