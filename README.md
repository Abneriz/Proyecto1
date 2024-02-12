# README - Juego de Laberinto

Este proyecto consiste en un juego de laberinto desarrollado en Python, donde el jugador debe mover un personaje (representado por 'P') desde una posición inicial hasta una posición final ('F') evitando obstáculos ('#'). El jugador puede mover al personaje utilizando las teclas de dirección.

## Funcionalidades

- **Movimiento del Personaje:** El jugador puede mover el personaje hacia arriba, abajo, izquierda o derecha utilizando las teclas de dirección.
- **Generación Aleatoria de Laberintos:** El juego puede cargar laberintos aleatorios desde archivos de mapa en una carpeta específica.
- **Jugabilidad Interactiva:** El juego proporciona una interfaz interactiva donde el jugador puede moverse por el laberinto y completarlo.
- **Contador de Números:** Presionando la tecla 'N', se activa un contador que suma números mientras la tecla esté presionada.
- **Mensajes de Estado:** El juego proporciona mensajes de estado al jugador, como bienvenida, indicaciones para comenzar y felicitaciones al completar el laberinto.

## Requisitos

- Python 3.x
- Librería `readchar`
- Sistema Operativo: Windows o Unix (Linux/macOS)

## Instrucciones de Uso

1. **Clonar el Repositorio:** Clona el repositorio en tu máquina local.

```bash
git clone https://github.com/Abneriz/Proyecto1.git
```

1 **Instalar Dependencias:** Instala las dependencias requeridas ejecutando el siguiente comando en la terminal:

```bash
pip install readchar
```

1. **Ejecutar el Juego:** Ejecuta el script principal `laberinto.py` para iniciar el juego.

```bash
python laberinto.py
```

1. **Jugar:** Sigue las instrucciones en pantalla para mover al personaje por el laberinto y completarlo.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **laberinto.py:** Contiene el código principal del juego.
- **carpeta_mapas/:** Carpeta que contiene archivos de mapas de laberintos.
- **README.md:** Este archivo que proporciona información sobre el juego y cómo usarlo.

## Notas Adicionales

- Asegúrate de tener los permisos necesarios para ejecutar scripts en tu sistema operativo.
- Puedes agregar tus propios mapas de laberinto en la carpeta `carpeta_mapas/` siguiendo el formato especificado en el código.

¡Disfruta del juego y buena suerte en la aventura del laberinto! 🎮🔍.
