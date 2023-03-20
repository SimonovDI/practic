# Создайте класс, который будет представлять матрицу (например, класс Matrix).
# Реализуйте методы __add__, __sub__, __mul__, __rmul__, __eq__, __ne__, __str__ и __repr__.

class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __sub__(self, other):
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __mul__(self, other):
        result_data = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __rmul__(self, other):
        result_data = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __eq__(self, other):
        result_data = [[self.data[i][j] == other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __ne__(self, other):
        result_data = [[self.data[i][j] != other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __repr__(self):
        return f'{self.__class__}: {self.__dict__} '

    def __str__(self):
        res = ""
        for row in self.data:
            res += " ".join([str(element) for element in row]) + "\n"
        return res


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[7, 8, 9], [10, 11, 12]])
print(a + b)
