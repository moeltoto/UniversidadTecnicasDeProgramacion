class SerieFibonacci:
    def __init__(self):
        self.n = int(input("Ingrese la cantidad de términos para la serie de Fibonacci: "))

    def fibonacciIterativa(self, n):
        serie = []
        a, b = 0, 1
        for _ in range(n):
            serie.append(a)
            a, b = b, a + b
        return serie

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def serie(self):
        serie_recursiva = []
        for i in range(self.n):
            serie_recursiva.append(self.fibonacci(i))
        return serie_recursiva

    def imprimir(self):
        print(f"Serie de Fibonacci de {self.n} términos (Iterativo): {self.fibonacciIterativa(self.n)}")
        print(f"Serie de Fibonacci de {self.n} términos (Recursivo): {self.serie()}")

obj = SerieFibonacci()
obj.imprimir()