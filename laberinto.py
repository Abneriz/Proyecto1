import random
import os
from readchar import readkey, key
from functools import reduce

class Juego:
    def __init__(self, cadena_mapa, posicion_inicial, posicion_final):
        self.matriz_laberinto = self.mapa(cadena_mapa)
        self.px, self.py = posicion_inicial
        self.posicion_final = posicion_final
        self.matriz_laberinto[self.px][self.py] = 'P'
        self.numero = 0

    def borrar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mapa(self, cadena_mapa):
        filas = cadena_mapa.strip().split('\n')
        laberinto = []
    
        for fila in filas:
            caracteres_fila = list(fila)
            laberinto.append(caracteres_fila)

        return laberinto   

    def mover_personaje(self, direccion):
        nueva_px, nueva_py = self.px, self.py

        if direccion == key.DOWN:
            nueva_px += 1
        elif direccion == key.LEFT:
            nueva_py -= 1
        elif direccion == key.RIGHT:
            nueva_py += 1
        elif direccion == key.UP:
            nueva_px -= 1

        if (
            0 <= nueva_px < len(self.matriz_laberinto) and
            0 <= nueva_py < len(self.matriz_laberinto[0]) and
            self.matriz_laberinto[nueva_px][nueva_py] != '#'
        ):
            self.matriz_laberinto[self.px][self.py] = '.'
            self.px, self.py = nueva_px, nueva_py
            self.matriz_laberinto[self.px][self.py] = 'P'

    def jugar(self):
        while (self.px, self.py) != self.posicion_final:
            self.enseñar_mapa()
            direccion = readkey()

            if direccion in [key.DOWN, key.LEFT, key.RIGHT, key.UP]:
                self.mover_personaje(direccion)

        return (self.px, self.py) == self.posicion_final

    def enseñar_mapa(self):
        self.borrar_terminal()
        for fila in self.matriz_laberinto:
            print("".join(fila))

    def convertir_a_matriz(self, laberinto_str):
        return list(map(list, laberinto_str("\n")))        

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas

    def leer_mapa(self, nombre_archivo):
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)
       

        try:
            with open(path_completo, 'r') as file:
                contenido = file.read()

            print("Contenido del archivo:")
            print(contenido)

            # Separar las líneas del archivo
            lineas = contenido.strip().splitlines()
            print("Líneas:")
            print(lineas)  

            mapa = reduce(lambda x,y:x + y,lineas[2], "").strip()

            # Verificar que las coordenadas tengan el formato correcto
            if len(lineas) < 3 or ',' not in lineas[0] or ',' not in lineas[1]:
                raise ValueError("El archivo de mapa no tiene el formato esperado.")

            # Separar las dimensiones y posiciones inicial y final
            dimensiones = tuple(map(int, lineas[0].replace(',', ' ').split()))
            if len(dimensiones) != 4:
                raise ValueError("Las dimensiones y posiciones iniciales/finales del laberinto no son válidas.")

            filas, columnas, px, py = dimensiones
            posicion_inicial = (px, py)

            # Separar las coordenadas finales
            posicion_final = tuple(map(int, lineas[1].replace(',', ' ').split()))

            # Obtener el contenido del mapa sin las primeras tres líneas
            mapa = '\n'.join(lineas[2:])

            # Ajustar la dimensión del laberinto si es necesario
            while len(mapa.split('\n')) < filas:
                mapa += '\n' + ' ' * columnas

            return dimensiones, posicion_inicial, posicion_final, mapa.strip()

        except Exception as e:
            print(f"Error al leer el mapa: {e}")
            raise

    def obtener_mapa_aleatorio(self):
        archivos_mapas = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        return self.leer_mapa(nombre_archivo)

    def iniciar_juego(self, dimensiones, posicion_inicial, posicion_final, mapa):
        filas, columnas, _, _ = dimensiones
        super().__init__(mapa, posicion_inicial, posicion_final)
        self.jugar()

def main():
    path_a_mapas = "carpeta_mapas"  
    juego_archivo = JuegoArchivo(path_a_mapas)
    
    Jugador = input("Ingresa tu Nombre oara jugar: ")
    print(f"Bienvenido@, {Jugador},Comencemos está aventura")
    print("Presiona cualquier tecla para confirmar que todo está bien")
    print("Presiona UP en cualquier momento para comenzar")
    print("Presiona la letra N para sumar números en el bucle")

    numero = 0

    while True:
        k = readkey()

        if k == key.DOWN:
            print("Abajo")

        elif k == key.LEFT:
            print("Izquierda")

        elif k == key.RIGHT:
            print("Derecha")

        elif k == key.UP:
            print("Arriba")
            try:
                dimensiones, posicion_inicial, posicion_final, mapa = juego_archivo.obtener_mapa_aleatorio()
                juego_archivo.iniciar_juego(dimensiones, posicion_inicial, posicion_final, mapa)
            except ValueError as e:
                print(f"Error al leer el mapa: {e}")
                continue

            if (juego_archivo.px, juego_archivo.py) == juego_archivo.posicion_final:
                print("¡Bien Hecho!, Has completado el laberinto")
                break

        elif k == 'n':
            juego_archivo.borrar_terminal()
            print(f"Manten precionado N: {numero}")
            numero += 1
            if numero > 50:
                numero = 0
        else:
            print(k)

if __name__ == "__main__":
    main()

