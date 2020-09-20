class Matrix:

    def __init__(self,matrix_repr):
        self.matrix = matrix_repr

    def __str__(self):
        __string = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                __string += str(self.matrix[i][j])
                if (j!= len(self.matrix[i])-1):  __string += ' '
                else: __string += '\n'
        return __string

    def __add__(self, other):
        if(len(self.matrix) != len(other.matrix)):
            print("размерность матриц не совпадает")
            return None
        __new_matrix = []
        for i in range(len(self.matrix)):
            if (len(self.matrix[i]) != len(other.matrix[i])):
                print("размерность матриц не совпадает")
                return None
            __new_row = []
            for j in range(len(self.matrix[i])):
                __new_row.append(self.matrix[i][j]+other.matrix[i][j])
            __new_matrix.append(__new_row)
        return Matrix(__new_matrix)

matrix_1 =  Matrix([[31,22],[37,43],[51,86]])
matrix_4 =  Matrix([[1,2],[1,2],[1,2]])
matrix_2 =  Matrix([[3,5,32],[2,4,6],[-1,64,-8]])
matrix_3 =  Matrix([[3,5,8,3],[8,3,7,1]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1 + matrix_4)
print(matrix_1 + matrix_2)