from colorama import init, Fore
from checkboard import Checkboard
import re


def ask_for_point(checkboard: Checkboard, prefix=''):
    while True:
        print(prefix + '下子(行 列)')
        if re_result := re.fullmatch(r'([1-9]\d*) ([1-9]\d*)', input(':')):
            (x, y) = (int(re_result[1]) - 1, int(re_result[2]) - 1)
            if x <= checkboard.scale[0] and y <= checkboard.scale[1] and checkboard.checkboard[x][y] == checkboard.CELLS['blank']:
                return (x, y)
        print(Fore.RED, '输入无效', Fore.RESET)


def team_switcher():
    while True:
        yield ('blue', Fore.BLUE + '蓝方' + Fore.RESET)
        yield ('red', Fore.RED + '红方' + Fore.RESET)


if __name__ == '__main__':
    init()
    game_count = 0
    teams = team_switcher()
    while True:
        game_count += 1
        checkboard = Checkboard(15, 15)
        print(f'第{game_count}局')
        round_count = 0
        while True:
            round_count += 1
            (piece_type, team_text) = teams.send(None)
            print(checkboard)
            (x, y) = ask_for_point(checkboard,
                                   f'>{str(round_count):>3} [{team_text}] ')
            if checkboard.put(x, y, piece_type):
                print(Fore.GREEN + f'{team_text}胜利\n\n\n' + Fore.RESET)
                input('按下Enter键以开始下一局')
                break
