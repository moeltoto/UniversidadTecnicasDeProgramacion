class Fibonacci:
    def __init__(self):
        self.n = int(input("Ingrese la posición en la serie de Fibonacci: "))

    def fibonacciIterativa(self):
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, self.n + 1):
            a, b = b, a + b
        return b

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def imprimir(self):
        print(f"Fibonacci en la posición {self.n} (Iterativo): {self.fibonacciIterativa()}")
        print(f"Fibonacci en la posición {self.n} (Recursivo): {self.fibonacci(self.n)}")

obj = Fibonacci()
obj.imprimir()