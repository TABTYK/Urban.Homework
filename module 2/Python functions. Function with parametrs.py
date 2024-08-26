def get_matrix(n,m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
    for j in range(len(matrix)):
        for k in range(m):
            matrix[j].append(value)
    print(matrix)
get_matrix(4,4,10)
get_matrix(2,2,2)
get_matrix(10,1,7)
