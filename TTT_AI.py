from random import randint
import random
import time


class Board:
    busy_us = []
    busy_ai = []
    turn_id = 0
    win_situation = [[(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(2, 0), (1, 1), (0, 2)]]

    def __init__(self):
        self.field = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]

    def __str__(self):
        a = '  1  2  3'
        result = ''
        result += a
        for num, row in enumerate(self.field):
            result += f'\n{num + 1} ' + '  '.join(row)
        return result


class AI(Board):
    def ask_enter(self):
        hidden = [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)]
        ]
        a = hidden[0][0]
        b = hidden[1][0]
        c = hidden[2][0]
        d = hidden[0][1]
        e = hidden[1][1]
        f = hidden[2][1]
        g = hidden[0][2]
        h = hidden[1][2]
        i = hidden[2][2]
        if_center = random.choice((a, c, g, i))
        while True:
            enter = randint(0, 2), randint(0, 2)
            for line in Board.win_situation:
                for us, ai in zip(Board.busy_us, Board.busy_ai):
                    if us in line:
                        # if us == e:
                        #     enter = if_center
                        line.remove(us)
                        if len(line) == 1:
                            for j in line:
                                enter = j
                        if len(line) == 0:
                            print('AI проиграл...')
                            exit()
                    # if ai in line:
                    #     line.remove(ai)
                    #     if len(line) == 0:
                    #         print('AI выиграл!')
                    #         exit()
                    #     if len(line) == 1:
                    #         for i in line:
                    #             enter = i
            if enter in Board.busy_us or enter in Board.busy_ai:
                continue
            Board.busy_ai.append(enter)
            return enter


class User(Board):
    def ask_enter(self):
        while True:
            enter = input('Enter: ')
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
        if n == 9:
            return True

    def loop(self):
        print()
        print('КРЕСТИКИ-НОЛИКИ ИИ 0.0.1')
        print('-' * 35)
        print('Формат ввода координат - XY \n(без пробела)')
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
            Board.turn_id += 1

            # print('us: ', self.busy_us)
            # print('ai: ', self.busy_ai)

            if self.not_win():
                print('Ничья')
                break

            if self.winner(self.busy_us):
                print(name, 'выиграл!')
                break

            if self.winner(self.busy_ai):
                print('AI выиграл!')
                break

            if Board.turn_id % 2 == 0:
                print('-->', name)
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


start = Game()
start.start_game()





















