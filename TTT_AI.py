from random import randint
import time


class BoardException(Exception):
    pass


class CellUsedException(BoardException):
    def __str__(self):
        return 'Ячейка занята'


class Board:
    def __init__(self):
        self.field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def __str__(self):
        a = '  1  2  3'
        result = ''
        result += a
        for num, row in enumerate(self.field):
            result += f'\n{num + 1} ' + '  '.join(row)

        return result



class Player:
    def __init__(self,turn):
        self.turn = turn

    def get_binar(self):
        self.turn = randint(0, 1)
        return self.turn



class User(Player):
    def ask_enter(self):
        while True:
            enter = input('Enter: ')
            if len(enter) != 2:
                print('Нужно ввести две цифры')
                continue
            if not enter.isdigit():
                print('Нужны цифры, а не буквы')
                continue
            if int(enter[0]) not in range(4) or int(enter[1]) not in range(4):
                print('Введи от 1 до 3')
                continue
            coord = [i for i in enter]
            x_id = int(coord[0])-1
            y_id = int(coord[1])-1

            return x_id, y_id


class AI(Player):
    def ask_enter(self):
        while True:
            enter = randint(0, 2), randint(0, 2)
            return enter


class Game(Board):
    def loop(self):
        while True:
            board = Board()

            x, y = User.ask_enter(self.field)
            board.field[x][y] = 'X'
            print(board)

            print('-' * 20)

            h, n = AI.ask_enter(self.field)
            time.sleep(randint(1, 3))
            board.field[h][n] = '0'
            print(board)


    def start_game(self):
        self.loop()

start = Game()
start.start_game()




























