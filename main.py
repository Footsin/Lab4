import math
import numpy
import os

def print_man():
    os.system('cls')
    print('\033[92m{}\033[0m'.format('РУКОВОДСТВО ПО ИСПОЛЬЗОВАНИЮ\n\n') + 
        'Программа реализует метод анализа иерархий Томаса Саати для одного уровня.\n' +
        'Пользователь вводит целочисленные данные для заполнения единичной матрицы с \n' +
        'одной стороны от диагонали, другая сторона зеркалится в виде 1 / x.\n' +
        'x — число введенное пользователем.\n' +
        'На основании введенных данных выводятся весовые коэффициенты для каждого критерия.\n')

def print_results(coeffs):
    os.system('cls')
    print('\033[92m{}\033[0m'.format('ВЕСОВЫЕ КОЭФФИЦИЕНТЫ ДЛЯ КАЖДОГО КРИТЕРИЯ\n'))
    for i in range(len(coeffs)):
        print(f'Весовой коэффициент для {i + 1}-го критерия: {coeffs[i]}')

def input_num(msg, min=None):
    while True:
        try:
            num = int(input(msg + ': '))
        except:
            print('\033[31m{}\033[0m'.format('Invalid value. Try again...'))
            continue

        if min != None and num < min:
            print('\033[31m{}\033[0m'.format(f'Value must be greater than {min}! Try again...'))
            continue
        return num

print_man()
count = input_num('Введите количество критериев', min=2)

matrix = numpy.eye(count)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i, j] == 1:
            break
        matrix[i, j] = input_num(f'Введите числовое значение критерия {i + 1} строки {j + 1} столбца в матрице')
        matrix[j, i] = matrix[0, 0] / matrix[i, j]

mults = []
for vector in matrix:
    multiLine = vector.prod()
    mults.append(math.pow(multiLine, 1 / count))

sumAllMult = numpy.array(mults).sum()

coeffs = [round(mults[i] / sumAllMult, 2) for i in range(len(mults))]

print_results(coeffs)

