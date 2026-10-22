class Factorial:
    def __init__(self):
        self.n = int(input("Ingrese un número para calcular su factorial: "))

    def factorialIterativa(self):
        resultado = 1
        for i in range(1, self.n + 1):
            resultado *= i
        return resultado

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def imprimir(self):
        print(f"El factorial de {self.n} (Iterativo) es: {self.factorialIterativa()}")
        print(f"El factorial de {self.n} (Recursivo) es: {self.factorial(self.n)}")

obj = Factorial()
obj.imprimir()