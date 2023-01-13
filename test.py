import random

field = [['X', 'X', '_'],
         ['_', 'X', '_'],
         ['X', 'O', 'O']]

busy_us = [(0, 0), (1, 0), (0, 2), (1, 1)]
busy_ai = [(2, 2), (1, 2)]

win_situation = [[(0, 0), (1, 0), (2, 0)],
                 [(0, 1), (1, 1), (2, 1)],
                 [(0, 2), (1, 2), (2, 2)],
                 [(0, 0), (0, 1), (0, 2)],
                 [(1, 0), (1, 1), (1, 2)],
                 [(2, 0), (2, 1), (2, 2)],
                 [(0, 0), (1, 1), (2, 2)],
                 [(2, 0), (1, 1), (0, 2)]]

a = win_situation[0][0]
b = win_situation[1][0]
c = win_situation[2][0]
d = win_situation[0][1]
e = win_situation[1][1]
f = win_situation[2][1]
g = win_situation[0][2]
h = win_situation[1][2]
i = win_situation[2][2]

coor_us = {}
coor_ai = {}
for num, line in enumerate(win_situation):
    for us in busy_us:
        if us in line:
            key = num
            coor_us.setdefault(key, [])
            coor_us[key].append(us)
    for ai in busy_ai:
        if ai in line:
            key = num
            coor_ai.setdefault(key, [])
            coor_ai[key].append(ai)

print('us: ', coor_us)
print('ai: ', coor_ai)

print('-' * 20)

# помешать противнику выиграть (не дать поставить третий)
intercept = []
for line in win_situation:
    for key, val in coor_us.items():
        if len(val) == 2:
            for i in win_situation[key]:
                if i not in val:
                    intercept.append(i)

print(set(intercept))
print(random.choice((intercept)))

print('-' * 20)

# завершить игру (закрыть линию)
final = []
for line in win_situation:
    for key, val in coor_ai.items():
        if len(val) == 2:
            for i in win_situation[key]:
                if i not in val:
                    final.append(i)

print(list(set(final))[0])
print(random.choice((final)))

print('-' * 20)

# начать строить линию (добавить второй)
build = []
for line in win_situation:
    for key, val in coor_ai.items():
        if len(val) == 1:
            for i in win_situation[key]:
                if i not in val:
                    build.append(i)

print(set(build))
print(random.choice((build)))


























