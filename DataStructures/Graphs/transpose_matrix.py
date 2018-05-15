def transpose_matrix(matrix):
    """Takes a square matrix and transposes
    the values in place"""
    iter = 0
    for row in range(len(matrix)):
        for col in range(iter,len(matrix[row])):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
        iter+=1