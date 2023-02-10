import Board as b

"""
Chess program by:
    - Karen Llanos
    - Carlos Lopez
    - Daniel Martinez
    - Alejandra Valencia
"""


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
