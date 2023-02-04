import Piece as pc


class King(pc.Piece):

    def __init__(self):
        self.name = 'king'

    """
    direction:
    - "left-up"
    - "right-up"
    - "left-down"
    - "right-down"
    - "left"
    - "right"
    - "up"
    - "down"
    """

    def move(self, direction):
        if direction == 'up':
            self.y += 1
        elif direction == 'right-up':
            self.y += 1
            self.x += 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'right-down':
            self.y -= 1
            self.x += 1
        elif direction == 'down':
            self.y -= 1
        elif direction == 'left-down':
            self.y -= 1
            self.x -= 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'left-up':
            self.y += 1
            self.x -= 1


class Queen(pc.Piece):

    def __init__(self):
        self.name = 'queen'

    """
    direction:
    - "left-up"
    - "right-up"
    - "left-down"
    - "right-down"
    - "left"
    - "right"
    - "up"
    - "down"
    """

    def move(self, movement, direction):
        if movement > 7:
            return False

        if direction == 'left-up':
            self.x -= movement
            self.y += movement
        elif direction == 'right-up':
            self.x += movement
            self.y += movement
        elif direction == 'left-down':
            self.x -= movement
            self.y -= movement
        elif direction == 'right-down':
            self.x += movement
            self.y -= movement
        elif direction == 'left':
            self.x -= movement
        elif direction == 'right':
            self.x += movement
        elif direction == 'up':
            self.y += movement
        elif direction == 'down':
            self.y -= movement


class Bishop(pc.Piece):

    def __init__(self):
        self.name = 'bishop'

    """
    direction:
    - "left-up"
    - "right-up"
    - "left-down"
    - "right-down"
    """

    def move(self, movement, direction):
        if movement > 7:
            return False

        if direction == 'left-up':
            self.x -= movement
            self.y += movement
        elif direction == 'right-up':
            self.x += movement
            self.y += movement
        elif direction == 'left-down':
            self.x -= movement
            self.y -= movement
        elif direction == 'right-down':
            self.x += movement
            self.y -= movement


class Pawn(pc.Piece):

    def __init__(self):
        self.name = 'pawn'
        self.first_movement = True

    def move(self, movement):
        if (self.first_movement and movement == 2) or movement == 1:
            self.first_movement = False

            if self.team == 'white':
                self.y += movement
            else:
                self.y -= movement
            return True

        else:
            return False


class Knight(pc.Piece):

    def __init__(self):
        self.name = 'knight'

    """
    first_direction:
    - "left"
    - "right"
    - "up"
    - "down"
    
    second_direction:
    - 1
    - 2
    """

    def move(self, first_direction, second_direction):
        if (
                first_direction == 'up' or first_direction == 'down' or first_direction == 'left' or first_direction == 'right') and (
                second_direction == 1 or second_direction == 2):

            if first_direction == 'up':
                if second_direction == 1:
                    self.y += 2
                    self.x -= 1
                else:
                    self.y += 2
                    self.x += 1

            elif first_direction == 'right':
                if second_direction == 1:
                    self.x += 2
                    self.y += 1
                else:
                    self.x += 2
                    self.y -= 1

            elif first_direction == 'down':
                if second_direction == 1:
                    self.y -= 2
                    self.x += 1
                else:
                    self.y -= 2
                    self.x -= 1

            elif first_direction == 'left':
                if second_direction == 1:
                    self.x -= 2
                    self.y -= 1
                else:
                    self.x -= 2
                    self.y += 1

        else:
            return False


class Rook(pc.Piece):

    def __init__(self):
        self.name = 'rook'

    """
    direction:
    - "left"
    - "right"
    - "up"
    - "down"
    """

    def move(self, movement, direction):
        if movement > 7:
            return False

        if direction == 'left':
            self.x -= movement
        elif direction == 'right':
            self.x += movement
        elif direction == 'up':
            self.y += movement
        elif direction == 'down':
            self.y -= movement
