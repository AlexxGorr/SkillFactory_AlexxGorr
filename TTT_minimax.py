# http://ptsj.ru/articles/482/482.pdf
# https://github.com/maulerant/learn_python/blob/master/tasks_for_beginners/tic_tac_toe.py

from copy import deepcopy
from random import randint
import time
import sys


class Board:
    turn_id = 0
    busy = []
    busy_user = []
    busy_ai = []
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
        # self.field = list(range(1, 10))
        # self.field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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

    def winner(self, token_var, field):
        win = Game()
        for i in win.win_situation:
            if field[i[0]] == field[i[1]] == field[i[2]] == token_var:
                return True

    def minimax(self, board, depth, is_maximizing=None):
        #sys.setrecursionlimit(50)
        win = Game()
        if win.winner(win.token[0], board):
            return 100
        if win.winner(win.token[1], board):
            return -100
        if len(Board.busy) == 9:
            return 0
        if is_maximizing:
            best_value = -sys.maxsize
            for key, val in self.available.items():
                if val is None:
                    board[key] = win.token[1]
                    intended_value = Game.minimax(board, depth + 1, False)
                    board[key] = None
                    best_value = max(best_value, intended_value)
        else:
            best_value = sys.maxsize
            for key, val in self.available.items():
                if val is None:
                    board[key] = win.token[0]
                    intended_value = Game.minimax(board, depth + 1, True)
                    board[key] = None
                    best_value = min(best_value, intended_value)
        return best_value

    def loop(self):
        board = Board()
        while True:
            Board.turn_id += 1

            #print('busy: ', self.busy)
            print('busy_user: ', self.busy_user)
            print('busy_ai: ', self.busy_ai)
            print('available: ', self.available)

            if self.winner(self.token[0], self.available):
                print('User выиграл!')
                break

            if self.winner(self.token[1], self.available):
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
            Board.busy_user.append(enter_id+1)
            return enter_id


class AI(Board):
    def ask_enter(self):
        while True:
            enter = randint(2, 10)
            if enter-1 not in Board.busy:
                Board.busy.append(enter-1)
                Board.busy_ai.append(enter-1)
                return enter-1
            else:
                print(f'Ячейка занята: {enter-1}')
                continue

    # def ask_enter(self):
    #     game = Game()
    #     enter = None
    #     best_value = -sys.maxsize
    #     #board = deepcopy(Board.available)
    #     board = {}
    #     for k, v in Board.available.items():
    #         board.update({deepcopy(k): deepcopy(v)})
    #     for key, val in Board.available.items():
    #         if val is None:
    #             board[key] = game.token[1]
    #             intended_value = game.minimax(board, 0, False)
    #             board[key] = None
    #             if intended_value > best_value:
    #                 best_value = intended_value
    #                 enter = key
    #                 Board.busy.append(enter)
    #                 Board.busy_ai.append(enter)
    #     return enter



g = Game()
g.start()































