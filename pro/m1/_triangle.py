class TriangleChecker:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("введите числа больше нуля")
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(isinstance(i, int) for i in [self.a, self.b, self.c]):
            return "Нужно вводить только числа!"
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "С такими параметрами можно построить треугольник!"
        else:
            return "Трегуольник не выйдет ("

triangle = TriangleChecker(3, 4, 5)
print(triangle.is_triangle())  # Вывод: 'С такими параметрами можно построить треугольник!'

