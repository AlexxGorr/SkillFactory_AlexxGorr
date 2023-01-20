# https://github.com/maulerant/learn_python/blob/89a268f8520072d1e6cde066cb220a08c37a94a1/tasks_for_beginners/tic_tac_toe.py#L34
# http://ptsj.ru/articles/482/482.pdf

from copy import deepcopy
from random import randint
import time
import sys


class Board:
    turn_id = 0
    busy = []
    available = {0: None,
                 1: None,
                 2: None,
                 3: None,
                 4: None,
                 5: None,
                 6: None,
                 7: None,
                 8: None}

    def __init__(self):
        #self.field = list(range(1, 10))
        #self.field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):
        res = ''
        a = '-' * 17
        b = '|'
        res += f'{b}{a[:-12]}{b}{a[:-12]}{b}{a[:-12]}{b}'
        for i in range(3):
            res += f'\n{b}  {self.field[0+3*i]}  |  {self.field[1+3*i]}  |  {self.field[2+3*i]}  {b}'
            res += f'\n{b}{a[:-12]}{b}{a[:-12]}{b}{a[:-12]}{b}'
        return res


class Game(Board):
    turn = randint(1, 5)
    Board.turn_id = turn
    token = 'XO'
    win_situation = ((0, 1, 2),
                     (3, 4, 5),
                     (6, 7, 8),
                     (0, 3, 6),
                     (1, 4, 7),
                     (2, 5, 8),
                     (0, 4, 8),
                     (2, 4, 6))

    def winner(self, token_var):
        for i in self.win_situation:
            if self.available[i[0]] == self.available[i[1]] == self.available[i[2]] == token_var:
                return True

    def evaluate(self):
        if self.winner(self.token[0]):
            return 1
        if self.winner(self.token[1]):
            return -1
        else:
            return 0

    def minimax(self, maximizing):
        # терминальный случай
        if len(self.busy) == 9:
            return self.evaluate()
        # инициализация ячейки
        best_turn = 0
        # случай максимизирующий
        if maximizing == True:
            best_score = - sys.maxsize
        # случай минимизирующий
        else:
            best_score = sys.maxsize
        # цикл с рекурсивным вызовом
        new_field = deepcopy(self.field)

        pass


    def loop(self):
        board = Board()
        while True:
            Board.turn_id += 1

            print('busy: ', self.busy)
            print('available: ', self.available)

            if self.winner(self.token[0]):
                print('User выиграл!')
                break

            if self.winner(self.token[1]):
                print('AI выиграл!')
                break

            if len(Board.busy) >= 9:
                print('Ничья')
                break

            if Board.turn_id % 2 == 0:
                print('Ходит User')
                turn_user = User.ask_enter(self.field)
                board.field[turn_user] = self.token[0]
                print(board)
                print()

            if Board.turn_id % 2 == 1:
                print('Ходит AI')
                time.sleep(randint(1, 3))
                turn_ai = AI.ask_enter(self.field)
                board.field[turn_ai-1] = self.token[1]
                print(board)
                print()

            for num, i in enumerate(board.field):
                if i == 'X':
                    self.available.update({num: i})
                if i == 'O':
                    self.available.update({num: i})

    def start(self):
        return self.loop()


class User(Board):
    def ask_enter(self):
        while True:
            enter = input('Enter: ')
            if ' ' in enter:
                print('Не корректный ввод')
                continue
            if enter.isalpha():
                print('Нужна цифра')
                continue
            if len(enter) > 1:
                print('Нужна одна цифра')
                continue
            if int(enter) < 1:
                print('Диапозон ввода от 1 до 9')
                continue
            if int(enter) in Board.busy:
                print('Ячейка занята')
                continue
            enter_id = int(enter) - 1
            Board.busy.append(enter_id+1)
            return enter_id


class AI(Board):
    def ask_enter(self):
        while True:
            enter = randint(2, 10)
            if enter-1 not in Board.busy:
                Board.busy.append(enter-1)
                return enter-1
            else:
                print(f'Ячейка занята: {enter-1}')
                continue


g = Game()
g.start()







































