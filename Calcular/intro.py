#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tres en Raya (Tic‑Tac‑Toe) con excepciones
Archivo completo y funcional.
"""

# ── Datos del estudiante ─────────────────────────────────────────────────────

ESTUDIANTE_NOMBRE = "Nuñez, Job"   
ESTUDIANTE_GRUPO  = "31"   

print(f"Estudiante: {ESTUDIANTE_NOMBRE} — Grupo: {ESTUDIANTE_GRUPO}")

# ── Clase de excepción ───────────────────────────────────────────────────────
class JuegoTerminacion(Exception):
    """Excepción para indicar que el juego debe terminar."""
    pass

# ── Función para imprimir el tablero ─────────────────────────────────────────
def imprimir_tablero(tablero):  
    """Imprime el tablero de 3×3."""
    for i in range(3):
        fila = tablero[3*i : 3*i+3]
        print(" | ".join(fila))
        if i < 2:
            print("---------")
    print()

# ── Comprobar victoria y empate ──────────────────────────────────────────────
def comprobar_victoria(tablero, jugador):
    """Devuelve True si el jugador ha conseguido tres en raya."""
    combos = [
        (0,1,2), (3,4,5), (6,7,8),   # filas
        (0,3,6), (1,4,7), (2,5,8),   # columnas
        (0,4,8), (2,4,6)             # diagonales
    ]
    return any(tablero[a] == tablero[b] == tablero[c] == jugador for a, b, c in combos)

def tablero_lleno(tablero):
    """True si no quedan espacios vacíos."""
    return ' ' not in tablero 

# ── Pedir movimiento al jugador ─────────────────────────────────────────────
def pedir_movimiento(tablero, jugador):
    """
    Pide al jugador una posición del 1 al 9 y valida la elección.
    Controla ValueError y KeyboardInterrupt.
    """
    while True:
        try:
            entrada = input(f"Jugador {jugador}, elija casilla (1-9): ").strip().lower()

            # Si el jugador escribe 'salir' o 'exit', se termina el juego
            if entrada in ('salir', 'exit'):
                raise JuegoTerminacion()

            pos = int(entrada) - 1  # Convertimos de 1–9 a índice 0–8

            # Validamos que la posición esté en el rango correcto
            if pos < 0 or pos > 8:
                print("Número fuera de rango. Debe estar entre 1 y 9.")
                continue

            # Verificamos que la casilla esté libre
            if tablero[pos] != ' ':
                print("Esa casilla ya está ocupada. Intenta otra.")
                continue

            return pos  # Movimiento válido

        except ValueError:
            print("Entrada inválida. Ingrese un número del 1 al 9 o 'salir'.")
        except KeyboardInterrupt:
            print("\nInterrupción con Ctrl+C. Terminando el juego...")
            raise JuegoTerminacion()

# ── Lógica de una partida ───────────────────────────────────────────────────
def partida():
    tablero = [" "] * 9
    turno = "X"
    
    imprimir_tablero(tablero)  # Mostrar el tablero vacío al inicio

    try:
        while True:
            # Pedir movimiento
            pos = pedir_movimiento(tablero, turno)
            
            # Actualizar el tablero
            tablero[pos] = turno
            
            # Imprimir el tablero actualizado
            imprimir_tablero(tablero)
            
            # Comprobar si hay victoria
            if comprobar_victoria(tablero, turno):
                print(f"¡Jugador {turno} gana!")
                break
            
            # Comprobar si hay empate
            if tablero_lleno(tablero):
                print("¡Empate!")
                break
            
            # Cambiar de turno
            turno = "O" if turno == "X" else "X"

    except JuegoTerminacion:
        print("\nPartida cancelada por el usuario.")

# ── Función principal ───────────────────────────────────────────────────────
def main():
    # Mensaje de bienvenida
    print("¡Bienvenido a Tres en Raya!")
    print("Escribe 'salir' en cualquier momento para terminar la partida.")

    try:
        while True:
            partida()
            respuesta = input("¿Jugar otra partida? (s/n): ").strip().lower()
            if respuesta != 's':
                print("Gracias por jugar. ¡Hasta luego!")
                break

    except JuegoTerminacion:
        print("\nEl juego fue cancelado por el usuario.")

    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

    finally:
        print("Programa terminado.")

# Inicia el juego
if __name__ == "__main__":
    main()
