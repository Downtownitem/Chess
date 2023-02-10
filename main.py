import Board as b

board = b.Board()

for row in board.get_board():
    text = '['
    first = True

    for piece in row:
        if first:
            first = False
        else:
            text += ', '
        text += str(piece)

    text += ']'
    print(text)
