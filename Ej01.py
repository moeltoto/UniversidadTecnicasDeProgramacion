class Seleccion:
    def __init__(self):
        self.vector = [64, 25, 12, 22, 11]
        self.n = len(self.vector)

    def ordenamiento_seleccion(self):
        for i in range(self.n - 1):
            min_idx = i
            for j in range(i + 1, self.n):
                if self.vector[j] < self.vector[min_idx]:
                    min_idx = j
            self.vector[i], self.vector[min_idx] = self.vector[min_idx], self.vector[i]

    def salida(self):
        print("\nOrdenamiento por Selección")
        self.ordenamiento_seleccion()
        print("\n", self.vector)

obj = Seleccion()
obj.salida()