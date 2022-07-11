m_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m_2 = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join('\t'.join([f"{i:3}" for i in line]) for line in self.lists)

    def __add__(self, other):
        m = [[int(self.lists[line][i]) + int(other.lists[line][i]) for i in range (len(self.lists[line]))]
            for line in range(len(self.lists))]
        return Matrix(m)
mat_1 = Matrix(m_1)

print(f'Matrix 1\n{mat_1}')

mat_2 = Matrix(m_2)
print(f'Matrix 2\n{mat_1}')

print(f'Matrix 1 + Matrix 2\n{mat_1 + mat_2}')





