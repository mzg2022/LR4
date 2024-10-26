class FibonacchiLst:
    """Итератор для списка с числами Фибоначчи"""
    
    def __init__(self, lst):
        self.lst = lst
        self.fib_set = self._generate_fib_set(max(lst))  # Определяем максимум для вычисления

    def _generate_fib_set(self, n):
        """Генератор множества чисел Фибоначчи до n"""
        a, b = 0, 1
        fib_set = {a}
        while a <= n:
            fib_set.add(a)
            a, b = b, a + b
        return fib_set

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        while self.idx < len(self.lst):
            res = self.lst[self.idx]
            self.idx += 1
            if res in self.fib_set:
                return res
        raise StopIteration

# Пример использования
if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iterator = FibonacchiLst(lst)
    print(list(fib_iterator))  # [0, 1, 2, 3, 5, 8, 1]
