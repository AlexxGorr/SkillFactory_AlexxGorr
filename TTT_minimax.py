

from copy import deepcopy
from random import randint
import time
import sys


class Board:
    turn_id = 0
    busy = []
    busy_user = []
    busy_ai = []
    available = {1: None,
                 2: None,
                 3: None,
                 4: None,
                 5: None,
                 6: None,
                 7: None,
                 8: None,
                 9: None}

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
        game = Game()
        for i in game.win_situation:
            if field[i[0]] == field[i[1]] == field[i[2]] == token_var:
                return True

    def not_win(self):
        brd = Board()
        if len(brd.busy) >= 9:
            return True

    def loop(self):
        board = Board()
        while True:
            Board.turn_id += 1

            print('busy: ', self.busy)
            print('busy_user: ', self.busy_user)
            print('busy_ai: ', self.busy_ai)
            print('available: ', self.available)
            print('field: ', board.field)

            if self.winner(self.token[0], board.field):
                print('User выиграл!')
                break

            if self.winner(self.token[1], board.field):
                print('AI выиграл!')
                break

            if Game.not_win(self.field):
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
                    self.available.update({num+1: i})
                if i == 'O':
                    self.available.update({num+1: i})

    def start(self):
        return self.loop()


class User:
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


class AI:
    # def ask_enter(self):
    #     board = Board()
    #     while True:
    #         enter = randint(1, 9)
    #         if enter not in board.busy:
    #             board.busy.append(enter)
    #             board.busy_ai.append(enter)
    #             return enter
    #         else:
    #             print(f'Ячейка занята: {enter}')
    #             continue

    def minimax(self, board, depth, is_maximizing=None):
        # sys.setrecursionlimit(50)
        game = Game()
        brd = Board()
        if game.winner(game.token[0], board):
            return 100
        if game.winner(game.token[1], board):
            return -100
        if Game.not_win(brd.field):
            return 0
        if is_maximizing:
            best_value = -sys.maxsize
            for key in range(1, 10):
                if key not in brd.busy:
                    board[key] = game.token[1]
                    intended_value = AI.minimax(board, depth + 1, False)
                    board[key] = ' '
                    best_value = max(best_value, intended_value)
        else:
            best_value = sys.maxsize
            for key in range(1, 10):
                if key not in brd.busy:
                    board[key] = game.token[0]
                    intended_value = AI.minimax(board, depth + 1, True)
                    board[key] = ' '
                    best_value = min(best_value, intended_value)
        return best_value

    def ask_enter(self):
        brd = Board()
        game = Game()
        enter = None
        best_value = -sys.maxsize
        board = [deepcopy(i) for i in brd.field]
        for key in range(1, 10):
            if key not in brd.busy:
                board[key] = game.token[1]
                intended_value = AI.minimax(board, 0, False)
                board[key] = ' '
                if intended_value > best_value:
                    best_value = intended_value
                    enter = key
                    brd.busy.append(enter)
                    brd.busy_ai.append(enter)
        return enter


g = Game()
g.start()































