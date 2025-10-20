import pytest
from math_functions import is_even, calculate_area, classify_triangle

# ==================== ТЕСТЫ ДЛЯ ЗАДАНИЯ 1: is_even ====================
@pytest.mark.parametrize("number,expected", [
    (2, True),      
    (4, True),       
    (0, True),     
    (1, False),     
    (3, False),     
    (-2, True),     
    (-1, False),    
    (100, True),    
    (101, False),   
])
def test_is_even(number, expected):
    assert is_even(number) == expected

# ==================== ТЕСТЫ ДЛЯ ЗАДАНИЯ 2: calculate_area ====================
@pytest.mark.parametrize("length,width,expected", [
    (5, 4, 20),         
    (10, 3, 30),        
    (1, 1, 1),          
    (7, 7, 49),        
    (2.5, 4, 10.0),    
    (100, 50, 5000),    
])
def test_calculate_area_valid(length, width, expected):
    assert calculate_area(length, width) == expected

# Тесты для некорректных входных данных
@pytest.mark.parametrize("length,width", [
    (0, 5),     
    (5, 0),     
    (-1, 5),    
    (5, -1),    
    (0, 0),     
])
def test_calculate_area_invalid_input(length, width):
    with pytest.raises(ValueError):
        calculate_area(length, width)

# ==================== ТЕСТЫ ДЛЯ ЗАДАНИЯ 3: classify_triangle ====================
@pytest.mark.parametrize("a,b,c,expected", [
    # Равносторонние треугольники
    (3, 3, 3, 'equilateral'),
    (5, 5, 5, 'equilateral'),
    (10, 10, 10, 'equilateral'),
    
    # Равнобедренные треугольники
    (3, 3, 2, 'isosceles'),
    (5, 3, 3, 'isosceles'),
    (4, 6, 4, 'isosceles'),
    (7, 5, 7, 'isosceles'),
    
    # Разносторонние треугольники
    (3, 4, 5, 'scalene'),
    (5, 6, 7, 'scalene'),
    (8, 15, 17, 'scalene'),
    (7, 8, 9, 'scalene'),
    
    # Треугольники с дробными сторонами
    (2.5, 2.5, 3.0, 'isosceles'),
    (3.1, 4.2, 5.3, 'scalene'),
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected

# Тесты для некорректных треугольников
@pytest.mark.parametrize("a,b,c", [
    (0, 3, 4),      
    (3, 0, 4),      
    (3, 4, 0),      
    (-1, 3, 4),     
    (1, 2, 10),     
    (5, 1, 1),      
    (10, 1, 2),     
])
def test_classify_triangle_invalid_input(a, b, c):
    with pytest.raises(ValueError):
        classify_triangle(a, b, c)