from random import randint
import time

# Внутренняя логика
# 1 класс точек -
#       метод сравнения точек +
#       метод вывода точек ( __eq__ , __repr__) +
# 2 классы исключений -
#       общий класс +
#       выстрел за доску +
#       выстрел в ту же клетку +
#       размещение кораблей +
# 3 класс корабля -
#       метод размера и ориентации +
#       метод выстрела +
# 4 класс игровое поле -
#       счетчик убитых кораблей +
#       состояние клеток +
#       список кораблей +
#       метод пределов доски +
#       контур корабля +
#       размещение корабля +
#       метод выстрела +
#       метод начала игры +
#
# Внешняя логика
# 1 класс игрока -
#       доска противника +
#       метод ask +
#       метод выстрел +
# 2 класс AI -
#       генератор точки +
# 3 класс игрок -
#       запрос координаты +
# 4 класс игры -
#       конструктор поля +
#       два игрока (AI, User) +
#       генерация кораблей на доске +
#       генерация доски +
#       стартовый интерфейс +
#       игровой цикл +
#       метод старт +

# Вывод досок в одну строку
# AI не должен стрелять в использованные клетки
# AI добивает корабли
# Выбор размера игрового поля
# Задержка по времени для AI +


# Основные исключения
class BoardException(Exception):
    pass

class OutBoardException(BoardException):
    def __str__(self):
        return 'Улетела за периметр'

class CellUsedException(BoardException):
    def __str__(self):
        return 'Ячейка уже использовалась'

class PlaceException(BoardException):
    pass


# Сравнение точек по координатам
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot: ({self.x}, {self.y})'


# конструктор корабля (нос (начало), длинна, ориентация), жизнь - длинна.
# Возвращаем писок точек. Свойство корабля. Метод попадания по кораблю (сравнение точек).
class Ship:
    def __init__(self, nos, orient, ln):
        self.nos = nos
        self.orient = orient
        self.ln = ln
        self.live = ln

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.ln):
            coor_x = self.nos.x
            coor_y = self.nos.y
            if self.orient == 0:
                coor_x += i

            if self.orient == 1:
                coor_y += i

            ship_dots.append(Dot(coor_x, coor_y))

        return ship_dots


    def shooten(self, shot):
        return shot in self.dots

    

# Конструктор игрового поля - размер по умолчанию, видимость. Счетчик попаданий.
# Список занятых точек, список с расположенными кораблямми. Возращается переменнная
# со сторокой из клеток (метод __str__).
# Метод проверки диапазона по ориентации.
class Board:
    def __init__(self, hid = False, size = 6):
        self.hid = hid
        self.size = size

        self.cnt = 0
        self.field = [['0'] * size for i in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        result = ''
        result += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            result += f'\n{i + 1} | ' + ' | '.join(row) + ' |'

        if self.hid:
            result = result.replace("■", '0')

        return result

    def out(self, dis):
        return not ((0 <= dis.x < self.size) and (0 <= dis.y < self.size))





# Контур корабля - список с точками вокруг точки.
    def countour(self, ship, verb = False):
        cntr = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 0), (0, 1),
                (1, -1), (1, 0), (1, 1)
               ]
        for i in ship.dots:
            for dx, dy in cntr:
                coor = Dot(i.x + dx, i.y + dy)
                if not(self.out(coor)) and coor not in self.busy:
                    if verb:
                        self.field[coor.x][coor.y] = '.'
                    self.busy.append(coor)

# Добавлеи корабля на доску - проверка списка занятых точек и точек в диапозоне,
# если не в диапозоне - вызов исключения.
    def add_ship(self, ship):
        for i in ship.dots:
            if self.out(i) or i in self.busy:
                raise PlaceException()
        for i in ship.dots:
            self.field[i.x][i.y] = "■️"
            self.busy.append(i)
        self.ships.append(ship)
        self.countour(ship)



    def shot(self, d):
        if self.out(d):
            raise OutBoardException()

        if d in self.busy:
            raise CellUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.live -= 1
                self.field[d.x][d.y] = 'X'
                if ship.live == 0:
                    self.cnt += 1
                    self.countour(ship, verb = True)
                    print('Убит')
                    return False
                else:
                    print('Зацепил')
                    return True

        self.field[d.x][d.y] = '.'
        print('Не попал!')
        return False

    def start(self):
        self.busy = []

    def defeat(self):
        return self.cnt == len(self.ships)



# Игрок - две доски. Возвращается повтор хода, если ход неудачный.
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise PlaceException()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat                        
            except BoardException as e:
                print(e)


# Конструкция AI - рандомный ход (генерация точки)
class AI(Player):
    def ask(self):
        a = Dot(randint(0, 5), randint(0, 5))
        
        print(f'Ходит AI: {a.x + 1} {a.y + 1}')
        return a

# Конструкция игрока - запрос координат. Проверки: длинна, цыфры. Возвращает два int-а.
class User(Player):
    def ask(self):
        while True:
            enter = input('Введите координаты: ')

            if len(enter) != 2:
                print('Координаты должно быть 2')
                continue

            if not enter.isdigit():
                print('Не корректный ввод')
                continue

            coord = [i for i in enter]
            y, x = int(coord[0]) - 1, int(coord[1]) - 1

            return Dot(x, y)


    
# Конструктор игры - размер доски. Две доски.
# Генерация досок - список кораблей: 3 2 2 1 1 1 1.
# Счетчик попыток генерации ограниченный. Добавление корабля (4 аргумента).
# Возвращает доску.
# Приветствие. Инструкция.
# Игровой цикл. Счетчик ходов
class Game:
    def __init__(self, size = 6):
        self.lng = [3, 2, 2, 1, 1, 1, 1]
        self.size = size
        plr = self.rand_board()
        cmp = self.rand_board()
        cmp.hid = True

        self.ai = AI(cmp, plr)
        self.us = User(plr, cmp)
    
    def build_board(self):
        board = Board(size = self.size)
        tr = 0
        for i in self.lng:
            while True:
                tr += 1
                if tr > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), randint(0, 1), i)
                try:
                    board.add_ship(ship)
                    break
                except PlaceException:
                    pass

        board.start()
        return board

    def rand_board(self):
        board = None
        while board is None:
            board = self.build_board()

        return board
    

    def greet(self):
        print('МОРСКОЙ БОЙ')
        print('-' * 45)
        print(f'Вводить координаты сначала по X потом по Y')
        print('-' * 45)


    
    def sel_board(self):
        
        print('Игрок')
        print('-' * 27)
        print(self.us.board)
        print('AI')
        print('-' * 27)
        print(self.ai.board)


    def loop(self):
        n = 0
        while True:
            self.sel_board()
            
            if n % 2 == 0:
                print('Ход игрока')
                print('-' * 27)
                repeat = self.us.move()
            else:
                print('Ход AI')
                print('-' * 27)
                time.sleep(randint(1, 3))
                repeat = self.ai.move()
            if repeat:
                n -= 1

            if self.ai.board.defeat():
                self.sel_board()
                print('-' * 27)
                print('Игрок выиграл')
                break
            if self.us.board.defeat():
                self.sel_board()
                print('-' * 27)
                print('Комп выиграл')
                break
            n += 1


    def start_game(self):
        self.greet()
        self.loop()

g = Game()
g.start_game()














