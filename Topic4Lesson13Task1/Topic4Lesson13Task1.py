import random

x = int(input("Введите колличество числе по горизонтали: ")) # колличество значений по горизонтали
y = int(input("Введите колличество числе по вертикали: ")) # колличество значений по вертикали

matrix_1 = [[random.randint(0,1) for i in range(x)] for i in range(y)] # матрица 1 # можно указать любой диапазон randint()
matrix_2 = [[random.randint(0,1) for i in range(x)] for i in range(y)] # матрица 2 # можно указать любой диапазон randint()
matrix_3 = [[0 for i in range(x)] for i in range(y)] # сумма матриц 1 и 2

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        matrix_3[i][j] = matrix_1[i][j]+matrix_2[i][j]

def pl(n):
    for i in n:
        print(i)
        
print("matrix_1:")    
pl(matrix_1)
print("matrix_2:")    
pl(matrix_2)
print("Сумма матрица matrix_1 и matrix_2:")   
pl(matrix_3)

