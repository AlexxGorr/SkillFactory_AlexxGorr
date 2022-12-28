import json
import string
import random

simbols = string.ascii_letters + string.digits + '!_?'
g = 'aeoiuy'
s = 'qtvxnzwfcjpdlbsgrkhm'

def load_db(filename):
    with open(filename) as file:
        db = json.load(file)
    return db

def save_db(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file, indent = 2)

def add_pass(db):
    site = input('Введите имя сайта: ')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    db.append(
        {
            "login": login,
            "password": password,
            "site": site
        }
    )

def change(subject, prev):
    t = input(f'Введите {subject} ({prev})')
    if t == '':
        return prev
    else:
        return t

def change_pass(info):
    info['site'] = change('название сайта', info['site'])
    info['login'] = change('логин', info['login'])
    info['password'] = change('пароль', info['password'])

def compare(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    inter = s1_set.intersection(s2_set)
    return len(inter) > 0

def gen_pass(l):
    while True:
        res = ''
        for i in range(l):
            res += random.choice(simbols)
        if compare(res, string.ascii_lowercase) \
            and compare(res, string.ascii_uppercase) \
            and compare(res, string.digits) \
            and compare(res, '!_?') \
            and res[0] not in string.ascii_uppercase:
            return res

def gen_ease_pass(l):
    res = ''
    for i in range(l-3):
        if i % 2 == 0:
            res += random.choice(g)
        else:
            res += random.choice(s)
    for j in range(3):
        res += random.choice(string.digits)
    return res

def add_and_gen(db):
    site = input('Введите имя сайта: ')
    login = input('Введите логин: ')
    l = int(input('Введите длинну пароля: '))
    t = input('Генерировать сложный пароль (y/n)? ')
    if 'y' in t.lower():
        password = gen_pass(l)
    else:
        password = gen_ease_pass(l)
    db.append(
        {
            "login": login,
            "password": password,
            "site": site
        }
    )

def show(info, num):
    print(f'{num:3} | {info["site"]} | {info["login"]} | {info["password"]}')

def search(db):
    site = input('Введите имя сайта: ')
    results = []
    for info in db:
        if site in info['site']:
            results.append(info)
    for num, info in enumerate(results):
        show(info, num)
    m = pass_mode()
    if m == '2':
        num = int(input('Введите номер: '))
        db.remove(results[num])
    elif m == '3':
        num = int(input('Введите номер: '))
        info = results[num]
        change_pass(info)

def pass_mode():
    print('Список действий:')
    print('1. Выйти из поиска')
    print('2. Удалить пароль')
    print('3. Изменить пароль')
    m = input('Введите номер действия:')
    return m

def check(db):
    cnt = {}
    for info in db:
        if info['password'] in cnt:
            cnt[info['password']] += 1
        else:
            cnt[info['password']] = 1
    for password, num in cnt.items():
        if num > 1:
            print(f'Пароль "{password}" не безопасен! Он используется на сайтах: ')
            for info in db:
                if info['password'] == password:
                    print(f'сайт: {info["site"]:15} логин: {info["login"]:15}')

def mode():
    print('Список режимов:')
    print('1. Добавить пароль')
    print('2. Сгенерировать пароль')
    print('3. Найти пароль')
    print('4. Найти уязвимости')
    print('5. Выйти из программы')
    m = input('Введите номер режима: ')
    return m

def loop(filename):
    db = load_db(filename)
    while True:
        m = mode()
        if m == '1':
            add_pass(db)
        elif m == '2':
            add_and_gen(db)
        elif m == '3':
            search(db)
        elif m == '4':
            check(db)
        elif m == '5':
            break
        else:
            print('Нет такого режима')

    save_db(filename, db)

loop('user.json')



















