from gen_fib import my_genn
from fibonacci_iterator import FibonacchiLst

# Тесты для сопрограммы
def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_edge():
    gen = my_genn()
    assert gen.send(1) == [0], "Один элемент ряда Фибоначчи"

# Тесты для итератора
def test_fib_lst():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == [0, 1, 2, 3, 5, 8, 1], "Проверка списка с числами Фибоначчи"

if __name__ == "__main__":
    test_fib_1()
    test_fib_2()
    test_fib_edge()
    test_fib_lst()
    print("Все тесты пройдены успешно.")
