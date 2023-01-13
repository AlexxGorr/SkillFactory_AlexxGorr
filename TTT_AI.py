from random import randint
import random
import time


class Board:
    busy_us = []
    busy_ai = []
    turn_id = 0
    turn_ai = 0
    coor_us = {}
    coor_ai = {}
    intercept = []
    finality = []
    build = []
    win_situation = [[(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(2, 0), (1, 1), (0, 2)]]

    def __init__(self):
        self.field = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]

    def __str__(self):
        a = '  1  2  3'
        result = ''
        result += a
        for num, row in enumerate(self.field):
            result += f'\n{num + 1} ' + '| '.join(row) + '|'
        return result


class Game(Board):
    def winner(self, inputter):
        for i in Board.win_situation:
            n = 0
            for j in inputter:
                if j in i:
                    n += 1
            if n == 3:
                return True

    def not_win(self):
        n = 0
        for i in self.busy_us:
            n += 1
        for i in self.busy_ai:
            n += 1
        if n >= 9:
            return True

    def loop(self):
        print()
        print('КРЕСТИКИ-НОЛИКИ ИИ 0.0.1')
        print('-' * 35)
        print('Формат ввода координат - XY')
        board = Board()
        print(board)
        print('-' * 35)
        name = input('Имя игрока: ')
        print('-' * 35)
        print('Определяем первый ход...')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        turn = randint(0, 5)
        Board.turn_id = turn
        print('Первый ходит --')

        while True:
            # проверка позиции
            for num, line in enumerate(Board.win_situation):
                for us in Board.busy_us:
                    if us in line:
                        key = num
                        Board.coor_us.setdefault(key, [])
                        Board.coor_us[key].append(us)
                for ai in Board.busy_ai:
                    if ai in line:
                        key = num
                        Board.coor_ai.setdefault(key, [])
                        Board.coor_ai[key].append(ai)

            for line in Board.win_situation:
                for key, val in Board.coor_us.items():
                    if len(set(val)) == 2:
                        for i in Board.win_situation[key]:
                            if i not in val and i not in Board.intercept:
                                Board.intercept.append(i)

            for line in Board.win_situation:
                for key, val in Board.coor_ai.items():
                    if len(set(val)) == 1:
                        for i in Board.win_situation[key]:
                            if i not in val and i not in Board.build:
                                for j in Board.busy_us:
                                    if j not in Board.win_situation[key]:
                                        Board.build.append(i)

            for line in Board.win_situation:
                for key, val in Board.coor_ai.items():
                    if len(set(val)) == 2:
                        for i in Board.win_situation[key]:
                            if i not in val and i not in Board.finality:
                                Board.finality.append(i)

            Board.turn_id += 1
            Board.turn_ai += 1

            # принты для текстов
            # print('us: ', self.busy_us)
            # print('ai: ', self.busy_ai)
            # print('coor_us: ', Board.coor_us)
            # print('coor_ai: ', Board.coor_ai)

            if self.not_win():
                print('Ничья')
                break

            if self.winner(self.busy_us):
                print(name.capitalize(), 'выиграл!')
                break

            if self.winner(self.busy_ai):
                print('AI выиграл!')
                break

            if Board.turn_id % 2 == 0:
                print('-->', name.capitalize())
                x, y = User.ask_enter(self.field)
                board.field[y][x] = 'X'
                print(board)
                print('-' * 35)

            if Board.turn_id % 2 == 1:
                print('--> AI')
                n, h = AI.ask_enter(self.field)
                time.sleep(randint(1, 3))
                board.field[h][n] = '0'
                print(board)
                print('-' * 35)

    def start_game(self):
        self.loop()


class AI(Board):
    def ask_enter(self):

        # принты для текстов
        # print('turn_ai: ', Board.turn_ai)
        # print('intercept: ', Board.intercept)
        # print('finality: ', Board.finality)
        # print('build: ', Board.build)

        finality_turn = set(Board.finality)
        intercept_turn = set(Board.intercept)
        build_turn = set(Board.build)

        while True:
            enter = 0

            # завершить игру (закрыть линию)
            if Board.turn_ai > 0:
                if len(finality_turn) > 1:
                    enter = random.choice((Board.finality))
                if len(finality_turn) == 1:
                    enter = list(finality_turn)[0]

            # помешать противнику выиграть (не дать поставить третий)
            if Board.turn_ai > 0:
                if len(intercept_turn) > 1:
                    enter = random.choice((Board.intercept))
                if len(intercept_turn) == 1:
                    enter = list(intercept_turn)[0]

            # начать строить линию (добавить второй)
            if Board.turn_ai < 5:
                if len(build_turn) > 1:
                    enter = random.choice((Board.build))
                if len(build_turn) == 1:
                    enter = list(build_turn)[0]

            if Board.turn_ai < 3:
                # если центр пуст
                if (1, 1) not in Board.busy_us or (1, 1) not in Board.busy_ai:
                    cntr = (1, 1)
                    enter = cntr
                # если центр занят
                if (1, 1) in Board.busy_us or (1, 1) in Board.busy_ai:
                    rnd_cnt = random.choice(((0, 0), (2, 0), (0, 2), (2, 2)))
                    enter = rnd_cnt

            if Board.turn_ai > 5:
                # рандомный ход
                if Board.turn_ai > 0:
                    enter = randint(0, 2), randint(0, 2)

            if enter in Board.busy_us or enter in Board.busy_ai:
                continue

            Board.busy_ai.append(enter)
            return enter


class User(Board):
    def ask_enter(self):
        while True:
            enter = input('Enter: ')
            if ' ' in enter:
                print('Пробел не нужен')
                continue
            if not enter.isdigit():
                print('Нужны цифры, а не буквы')
                continue
            if len(enter) != 2:
                print('Нужно ввести две цифры')
                continue
            if int(enter[0]) not in range(4) or int(enter[1]) not in range(4):
                print('Введи от 1 до 3')
                continue
            coord = [i for i in enter]
            x_id = int(coord[0])-1
            y_id = int(coord[1])-1
            check_id = x_id, y_id
            if check_id in Board.busy_us or check_id in Board.busy_ai:
                print('Ячейка занята')
                continue
            Board.busy_us.append((x_id, y_id))
            return x_id, y_id


start = Game()
start.start_game()















