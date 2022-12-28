rand_matrix = [[4, 8, 3, 5, 1, 4, 8, 3, 4, 1],
               [9, 4, 6, 0, 4, 0, 6, 4, 7, 2],
               [2, 5, 7, 4, 2, 1, 5, 2, 8, 8],
               [8, 4, 6, 2, 4, 2, 7, 1, 7, 0],
               [3, 1, 5, 3, 8, 5, 1, 9, 5, 0],
               [7, 3, 8, 2, 4, 4, 9, 7, 3, 9]]
n = 6
m = 10
for i in range(n):
    for j in range(m):
        print(rand_matrix[i][j], end='')
    print()

min_val_row = []
min_ind_row = []
max_val_row = []
max_ind_row = []

for row in rand_matrix:
    min_ind = 0
    min_val = row[min_ind]
    max_ind = 0
    max_val = row[max_ind]

    for ind_col in range(len(row)):
        if row[ind_col] < min_val:
            min_val = row[ind_col]
            min_ind = ind_col
        if row[ind_col] > max_val:
            max_val = row[ind_col]
            max_ind = ind_col

    min_val_row.append(min_val)
    min_ind_row.append(min_ind)
    max_val_row.append(max_val)
    max_ind_row.append(max_ind)

print('минимальные элементы: ', min_val_row)
print('минимальные индексы: ', min_ind_row)
print('максимальные элементы: ', max_val_row)
print('максимальные индексы: ', max_ind_row)