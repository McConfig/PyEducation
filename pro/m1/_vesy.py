class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0
    def add_right(self, weight):
        self.right += weight
    def add_left(self, weight):
        self.left += weight
    def result(self):
        if self.left == self.right:
            return '='
        elif self.left > self.right:
            return 'L'
        else:
            return 'R'

balance = Balance()
balance.add_right(5)
balance.add_left(3)
print(balance.result())  # Вывод: 'L'
balance.add_left(2)
print(balance.result())  # Вывод: '='
balance.add_right(3)
print(balance.result())  # Вывод: 'R'
