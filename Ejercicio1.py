import random

class BusquedaBinaria:
    def __init__(self):
        self.n = 10
        self.vector = [random.randint(1, 100) for _ in range(self.n)]
        
    def quicksort(self, izq, der):
        if izq < der:
            pivote = self.vector[der]
            i = izq - 1
            for j in range(izq, der):
                if self.vector[j] <= pivote:
                    i = i + 1
                    self.vector[i], self.vector[j] = self.vector[j], self.vector[i]
            self.vector[i + 1], self.vector[der] = self.vector[der], self.vector[i + 1]
            pi = i + 1
            
            self.quicksort(izq, pi - 1)
            self.quicksort(pi + 1, der)

    def algoritmo_busqueda_binaria(self, x):
        izq = 0
        der = self.n - 1
        while izq <= der:
            centro = (izq + der) // 2
            if self.vector[centro] == x:
                return centro
            elif self.vector[centro] < x:
                izq = centro + 1
            else:
                der = centro - 1
        return -1

    def buscarElemento(self):
        try:
            x = int(input("Ingrese el elemento a buscar en el arreglo: "))
            posicion = self.algoritmo_busqueda_binaria(x)
            if posicion != -1:
                print(f"El elemento {x} fue encontrado en el índice {posicion}.")
            else:
                print(f"El elemento {x} no se encuentra en el arreglo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    def salida(self):
        self.quicksort(0, self.n - 1)
        print("\nVector ordenado:", self.vector)
        self.buscarElemento()

obj = BusquedaBinaria()
obj.salida()