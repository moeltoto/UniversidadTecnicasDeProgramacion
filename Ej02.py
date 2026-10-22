class Quicksort:
    def __init__(self):
        self.vector = [10, 7, 8, 9, 1, 5]
        self.n = len(self.vector)

    def quicksort(self, izq, der):
        if izq < der:
            pivot = self.vector[der]
            i = izq - 1
            for j in range(izq, der):
                if self.vector[j] <= pivot:
                    i = i + 1
                    # Intercambio
                    self.vector[i], self.vector[j] = self.vector[j], self.vector[i]
            self.vector[i + 1], self.vector[der] = self.vector[der], self.vector[i + 1]
            pi = i + 1

            self.quicksort(izq, pi - 1)
            self.quicksort(pi + 1, der)

    def salida(self):
        print("\nOrdenamiento por QuickSort")
        self.quicksort(0, self.n - 1)
        print("\n", self.vector)

obj = Quicksort()
obj.salida()