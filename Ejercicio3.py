class Hanoi:
    def __init__(self):
        try:
            self.n = int(input("Ingrese la cantidad de discos para la Torre de Hanoi: "))
        except ValueError:
            print("Entrada inválida. Se asignarán 3 discos por defecto.")
            self.n = 3

    def hanoi(self, n, A, B, C):
        if n == 1:
            print(f"Mover disco 1 de la torre {A} a la torre {C}")
            return
        
        self.hanoi(n - 1, A, C, B)
        print(f"Mover disco {n} de la torre {A} a la torre {C}")
        self.hanoi(n - 1, B, A, C)

    def potencia(self, b, n):
        if n == 0:
            return 1
        return b * self.potencia(b, n - 1)

    def mostrarMovimientos(self):
        if self.n <= 0:
            print("El número de discos debe ser mayor a 0.")
            return
            
        print(f"\nResolviendo Torres de Hanoi para {self.n} discos:")
        self.hanoi(self.n, 'A', 'B', 'C')
        
        movimientos_minimos = self.potencia(2, self.n) - 1
        print(f"\nLa cantidad total de movimientos requeridos es: {movimientos_minimos}")

obj = Hanoi()
obj.mostrarMovimientos()