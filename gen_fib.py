import functools

def fib_elem_gen(n):
    """Генератор элементов ряда Фибоначчи"""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def my_genn():
    """Сопрограмма для генерации ряда Фибоначчи"""
    while True:
        n = yield  # Получаем значение через .send()
        yield fib_elem_gen(n)  # Генерируем и возвращаем список первых n чисел Фибоначчи

def fib_coroutine(g):
    """Функция для работы с сопрограммой"""
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)  # Активируем сопрограмму
        return gen
    return inner

my_genn = fib_coroutine(my_genn)

# Пример использования
if __name__ == "__main__":
    gen = my_genn()
    print(gen.send(3))  # [0, 1, 1]
    print(gen.send(5))  # [0, 1, 1, 2, 3]
    print(gen.send(8))  # [0, 1, 1, 2, 3, 5, 8, 13]
