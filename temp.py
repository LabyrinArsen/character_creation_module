from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления '\
          'квадратного корня из заданного числа'

print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def Calc(your_number):
    """Проверяет валидность введенного числа."""
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа.' +
          f'Это будет: {CalculateSquareRoot(your_number)}')


print(message)
Calc(25.5)
