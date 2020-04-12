from random import randint


def print_matrix(matrix, length=3):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print("{:{}}".format(matrix[row][col], length), end=" ")
        print()


N = 5
M = 5
correct_matrix = [[(M * i) + j for j in range(M)] for i in range(N)]
print(correct_matrix)
print_matrix(correct_matrix)






# Домашнее задание
#
print("Выполнить обработку элементов квадратной матрицы")

#     Выполнить обработку элементов квадратной матрицы A, имеющей N строк и N столбцов.
#     Определить произведение элементов, расположенных параллельно побочной диагонали
#     (ближайшие к побочной). Элементы побочной диагонали имеют индексы от [N,0] до [0,N].


def summ_el(matrix):
    n = (len(matrix[0]))
    summ = 0
    for i in range(1, n):
        summ += matrix[i][-i] # правая побочная
        summ += matrix[i-1][-i-1] # левая побочная
    return summ


print(summ_el(correct_matrix))


print("Создайте матрицу целых чисел")
#     Дано число n. Создайте матрицу целых чисел A[n][n], и заполните его по следующему правилу:
#     числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1; числа, стоящие
#     выше этой диагонали, равны 0; числа, стоящие ниже этой диагонали, равны 2.
#     0 0 0 1
#     0 0 1 2
#     0 1 2 2
#     1 2 2 2

def matrix_foll(n):
    n = int(n)
    p = [[0 for _ in range(n)] for _ in range(n)]
    sum_x_y = 0
    for x in range(n):
        for y in range(n):
            p[y][-y-1] = 1
            sum_x_y = x + y
            if sum_x_y < n - 1:
                p[x][y] = 0
            else:
                p[x][y] = 2
    return p

print(print_matrix(matrix_foll(9)))




print('Дано число n и квадратный массив')

#     Дано число n и квадратный массив int A[n][n]. Проверьте, является ли массив симметричным
#     относительно главной диагонали матрицы.
#     0 1 2
#     1 2 3
#     2 3 4
def proverka(l):
    n = len(l)
    for x in range(n):
        for y in range(n):
            if l[x][y] != l[y][x]:
                return [False, l[x][y], l[y][x]]
    return True

list_True = [[0, 5, 10, 15, 20],
             [5, 0, 11, 16, 21],
             [10, 11, 0, 17, 22],
             [15, 16, 17, 0, 19],
             [20, 21, 22, 19, 0]]

list_False = [[0, 5, 10, 15, 20],
             [5, 0, 11, 16, 21],
             [10, 11, 0, 17, 22],
             [15, 16, 17, 0, 0],
             [20, 21, 22, 19, 0]]

print(proverka(list_True))
print(proverka(list_False))