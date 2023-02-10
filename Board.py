import PieceType as pt


class Board:

    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]

        piece = pt.King()
        piece.team = 'white'
        piece.x = 4
        piece.y = 0
        self.board[0][4] = piece

        piece = pt.King()
        piece.team = 'black'
        piece.x = 4
        piece.y = 7
        self.board[7][4] = piece

        piece = pt.Queen()
        piece.team = 'white'
        piece.x = 3
        piece.y = 0
        self.board[0][3] = piece

        piece = pt.Queen()
        piece.team = 'black'
        piece.x = 3
        piece.y = 7
        self.board[7][3] = piece

        piece = pt.Rook()
        piece.team = 'white'
        piece.x = 0
        piece.y = 0
        self.board[0][0] = piece

        piece = pt.Rook()
        piece.team = 'white'
        piece.x = 7
        piece.y = 0
        self.board[0][7] = piece

        piece = pt.Rook()
        piece.team = 'black'
        piece.x = 0
        piece.y = 7
        self.board[7][0] = piece

        piece = pt.Rook()
        piece.team = 'black'
        piece.x = 7
        piece.y = 7
        self.board[7][7] = piece

        piece = pt.Bishop()
        piece.team = 'white'
        piece.x = 2
        piece.y = 0
        self.board[0][2] = piece

        piece = pt.Bishop()
        piece.team = 'white'
        piece.x = 5
        piece.y = 0
        self.board[0][5] = piece

        piece = pt.Bishop()
        piece.team = 'black'
        piece.x = 2
        piece.y = 7
        self.board[7][2] = piece

        piece = pt.Bishop()
        piece.team = 'black'
        piece.x = 5
        piece.y = 7
        self.board[7][5] = piece

        piece = pt.Knight()
        piece.team = 'white'
        piece.x = 1
        piece.y = 0
        self.board[0][1] = piece

        piece = pt.Knight()
        piece.team = 'white'
        piece.x = 6
        piece.y = 0
        self.board[0][6] = piece

        piece = pt.Knight()
        piece.team = 'black'
        piece.x = 1
        piece.y = 7
        self.board[7][1] = piece

        piece = pt.Knight()
        piece.team = 'black'
        piece.x = 6
        piece.y = 7
        self.board[7][6] = piece

        for i in range(8):
            piece = pt.Pawn()
            piece.team = 'white'
            piece.x = i
            piece.y = 1
            self.board[1][i] = piece

            piece = pt.Pawn()
            piece.team = 'black'
            piece.x = i
            piece.y = 6
            self.board[6][i] = piece

    def get_board(self):
        return self.board
