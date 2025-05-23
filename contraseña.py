import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña debe ser 8 caracteres.")

    # Caracteres disponibles
    numeros = string.digits
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    especiales = "¿¡?=)(/¨*+-%&$#!"

    # Todos los caracteres posibles sin repetir
    todos = list(set(numeros + mayusculas + minusculas + especiales))
    if longitud > len(todos):
        raise ValueError(f"No se puede generar una contraseña de {longitud} caracteres sin repetir. El máximo posible es {len(todos)}.")

    # Elegimos uno de cada tipo obligatorio
    obligatorio = [
        random.choice(numeros),
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(especiales)
    ]

    # Eliminamos los ya elegidos para no repetir
    for c in obligatorio:
        todos.remove(c)

    # Elegimos el resto aleatoriamente sin repetir
    restantes = random.sample(todos, longitud - 4)

    # Unimos todo y lo mezclamos
    contraseña = obligatorio + restantes
    random.shuffle(contraseña)

    return ''.join(contraseña)

# Ejemplo de uso
try:
    longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
    contraseña = generar_contraseña(longitud)
    print("Contraseña generada:", contraseña)
except ValueError as e:
    print("Error:", e)
