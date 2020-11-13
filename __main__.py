from checkboard import Checkboard
import re


def ask_for_point(checkboard: Checkboard, prefix=''):
    while True:
        if re_result := re.fullmatch(r'(\d*) (\d*)', input(prefix + '下子(行 列)：')):
            (x, y) = (int(re_result[1]), int(re_result[2]))
            if x < checkboard.scale[0] and y < checkboard.scale[1] and checkboard.checkboard[x][y] == checkboard.CELLS['blank']:
                return (x, y)
        print('输入无效')


def team_switcher():
    while True:
        yield ('white', '白方')
        yield ('black', '黑方')


if __name__ == '__main__':
    game_count = 0
    teams = team_switcher()
    while True:
        game_count += 1
        checkboard = Checkboard(10, 10)
        print(f'第{game_count}局')
        round_count = 0
        while True:
            round_count += 1
            (piece_type, team_text) = teams.send(None)
            print(checkboard)
            (x, y) = ask_for_point(checkboard,
                                   f'>{str(round_count):>3} [{team_text}] ')
            if checkboard.put(x, y, piece_type):
                print(f'{team_text}胜利\n\n\n')
                break
