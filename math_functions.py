# Задание 1: Проверка четности числа
def is_even(number):
    return number % 2 == 0

# Задание 2: Вычисление площади прямоугольника
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами")
    return length * width

# Задание 3: Классификация треугольника по сторонам
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    
    if a == b == c:
        return 'equilateral'
    elif a == b or a == c or b == c:
        return 'isosceles'
    else:
        return 'scalene'