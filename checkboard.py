from colorama import Fore
from typing import Literal


Derections = Literal['left', 'right', 'above', 'below',
                     'upperleft', 'upperright', 'lowerleft', 'lowerright']


class Checkboard:
    CELLS = {'blue': Fore.BLUE + '+' + Fore.RESET, 'red': Fore.RED + '+' + Fore.RESET, 'blank': '+'}

    def __init__(self, rows: int, cols: int):
        assert rows < 100 and cols < 100, 'The max scale is (99,99)'
        self.checkboard = [[Checkboard.CELLS['blank']
                            for i_ in range(cols)] for i in range(rows)]
        self.scale = (rows, cols)

    def __repr__(self):
        to_print = ''
        col_num_max_len = len(str(self.scale[1]))
        col_nums = [f'{num:>{col_num_max_len}}' for num in range(1, self.scale[1] + 1)]
        row_num_max_len = len(str(self.scale[0]))
        row_nums = [f'{num:>{row_num_max_len}}' for num in range(1, self.scale[0] + 1)]
        for i in range(0, col_num_max_len):
            to_print += ' ' * (row_num_max_len + 1)
            for col_num in col_nums:
                to_print += col_num[i]
                to_print += ' '
            to_print += '\n'
        for i, row in enumerate(self.checkboard):
            to_print += row_nums[i] + ' '
            for piece in row:
                to_print += piece
                to_print += ' '
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
