# a = [[1,2],[1,2]]
# b = [[1,1],[1,1]]

# c = []

# for i in range(len(a)):
#     for j in range(len(a[0])):
#         c[i][j] = a[i][j] + c[i][j]

# def pl(n):
#     for i in n:
#         print(i)
        
# print(c)

a = [[1, 2], [3, 4]]
b = [[4, 5], [6, 7]]
c = []



for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]
 

for row in c:
    for element in row:
        print(element, end=" ")
    print()