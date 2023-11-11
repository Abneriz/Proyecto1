import os
from readchar import readkey, key

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

    def bucle_principal(self):
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
                self.enseñar_mapa()
                if self.jugar():
                    print("¡Bien hecho! Has completado el laberinto")
                    return

            if k == 'n':
                self.borrar_terminal()
                print(f"Preciona n para sumar número: {self.numero}")
                self.numero += 1
                if self.numero > 50:
                    self.numero = 0
            else:
                print(k)

def main():
    cadena_mapa = """
P.###################
........#...#.#.#.#.#
#.#########.#.#.#.#.#
#.......#...........#
#.#########.#.###.###
#...#.#...#.#...#...#
#.###.#.#####.#####.#
#.#.#...........#...#
#.#.#.#.###.#.#.#####
#.....#...#.#.#...#.#
#.#######.#########.#
#.#.#.#.#.#.......#.#
###.#.#.#.#.#.###.#.#
#...#.....#.#.#...#.#
###.#.#####.#######.#
#.#.#.#...#...#.....#
#.#.#.###.###.###.###
#...#...#.#.........#
#.#.#.#.#.###.#####.#
#.#...#.......#......
###################..
    """
    posicion_inicial = (0, 0)
    posicion_final = (20, 20)

    print("Ingresa tu nombre para jugar:")
    nombre = input()
    print(f"Bienvenid@, {nombre}, comencemos esta aventura:")
    print("Presiona UP en cualquier momento para comenzar:")
    print("Presiona cualquier tecla para confirmar que todo está bien:")
    print("Presiona la letra N para sumar números en el bucle:")

    juego = Juego(cadena_mapa, posicion_inicial, posicion_final)
    juego.bucle_principal()

if __name__ == "__main__":
    main()
