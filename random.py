import string  
import time    
import matplotlib.pyplot as plt  

class random:
    a = 1664525     # Multiplicador en el algoritmo LCG
    c = 1013904223  # Incremento en el algoritmo LCG
    m = 2**32       # Módulo en el algoritmo LCG

    # Método para obtener la semilla utilizando el tiempo actual en nanosegundos
    def getSeed(self):
        return time.clock_gettime_ns(time.CLOCK_BOOTTIME)

    # Método para obtener un elemento aleatorio de una lista dada
    def getRandomListItem(self, list):
        return list[self.nextRandInRange(0, len(list) - 1)]

    # Método para generar el siguiente número aleatorio en la secuencia
    def nextRand(self):
        seed = self.getSeed()  # Obtiene la semilla actual
        return (self.a * seed + self.c) % self.m  # Aplica el algoritmo LCG

    # Método para generar un número aleatorio dentro de un rango dado
    def nextRandInRange(self, inicio, fin):
        return inicio + (self.nextRand() % (fin - inicio + 1))

    # Método para generar un carácter aleatorio
    def nextRandChar(self):
        return str(self.getRandomListItem(string.ascii_letters))

    # Método para generar un número decimal aleatorio en el rango [0,1)
    def nextRandFloat(self):
        return self.nextRand() / self.m

    # Método para generar un número decimal aleatorio dentro de un rango dado
    def nextRandFloatInRange(self, inicio, fin):
        return inicio + (fin - inicio) * self.nextRandFloat()

    # Método para graficar puntos dispersos
    def graficar(self):
        valoresX = []  # Lista para almacenar valores de coordenada x
        valoresY = []  # Lista para almacenar valores de coordenada y

        # Genera puntos aleatorios con una probabilidad del 10%
        for y in range(600):
            for x in range(550):
                if self.nextRandFloat() < 0.1:
                    valoresX.append(x)  # Agrega la coordenada x
                    valoresY.append(y)  # Agrega la coordenada y

        # Grafica los puntos dispersos
        plt.scatter(valoresX, valoresY, color='black', s=0.1)
        plt.show()

# Crea una instancia de la clase Aleatorio
aleatorio = random()
# Llama al método graficar para generar y mostrar el gráfico de dispersión
aleatorio.graficar()
