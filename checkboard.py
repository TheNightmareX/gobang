from typing import Literal


Derections = Literal['left', 'right', 'above', 'below',
                     'upperleft', 'upperright', 'lowerleft', 'lowerright']


class Checkboard:
    CELLS = {'white': '■', 'black': '□', 'blank': '+'}

    def __init__(self, rows: int, cols: int):
        assert rows < 100 and cols < 100, 'The max scale is (99,99)'
        self.checkboard = [[Checkboard.CELLS['blank']
                            for i_ in range(cols)] for i in range(rows)]
        self.scale = (rows, cols)

    def __repr__(self):
        # init text with col numbers
        to_print = f"   {''.join([f'{str(i):2}' for i in range(self.scale[1])])}\n"
        for (row_i, row) in enumerate(self.checkboard):
            to_print += f'{str(row_i):>2} '  # row number
            for piece in row:
                to_print += f'{piece} '
            to_print += '\n'
        return to_print

    def put(self, x: int, y: int, piece: str):
        self.checkboard[x][y] = Checkboard.CELLS[piece]
        if (
            self.get_connected_pieces(x, y, 'left') +
            self.get_connected_pieces(x, y, 'right') >= 4
            or self.get_connected_pieces(x, y, 'above') +
            self.get_connected_pieces(x, y, 'below') >= 4
            or self.get_connected_pieces(x, y, 'upperleft') +
            self.get_connected_pieces(x, y, 'lowerright') >= 4
            or self.get_connected_pieces(x, y, 'upperright') +
            self.get_connected_pieces(x, y, 'lowerleft') >= 4
        ):
            return True
        return False

    def get_connected_pieces(self, x: int, y: int, derection: Derections):
        count = 0
        while self.is_same_piece(x, y, derection):
            count += 1
            if derection in ['left', 'upperleft', 'lowerleft']:
                y -= 1
            elif derection in ['right', 'upperright', 'lowerright']:
                y += 1
            if derection in ['above', 'upperleft', 'upperright']:
                x -= 1
            elif derection in ['below', 'lowerleft', 'lowerright']:
                x += 1
        return count

    def is_same_piece(self, x: int, y: int, derection: Derections):
        try:
            piece = self.checkboard[x][y]
            if (
                derection == 'left' and self.checkboard[x][y - 1] == piece
                or derection == 'right' and self.checkboard[x][y + 1] == piece
                or derection == 'above' and self.checkboard[x - 1][y] == piece
                or derection == 'below' and self.checkboard[x + 1][y] == piece
                or derection == 'upperleft' and self.checkboard[x - 1][y - 1] == piece
                or derection == 'upperright' and self.checkboard[x - 1][y + 1] == piece
                or derection == 'lowerleft' and self.checkboard[x + 1][y - 1] == piece
                or derection == 'lowerright' and self.checkboard[x + 1][y + 1] == piece
            ):
                return True
        except:
            pass
        return False
