import random

# Definición de la baraja sin comodines
SUITS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
RANKS = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']

#Metodo principal juego
def blackjack():
    print("¡Bienvenido al Blackjack! \n")
    mazo = crearBaraja()
    random.shuffle(mazo)
    mano_jugador = [repartirCarta(mazo), repartirCarta(mazo)]
    mano_casa = [repartirCarta(mazo), repartirCarta(mazo)]

    if verificarDobleAs(mano_jugador) and verificarDobleAs(mano_casa):
        print("¡Ambos tienen doble A! Es un empate.")
        return
    elif verificarDobleAs(mano_jugador):
        print("¡Jugador tiene doble A! ¡Gana automáticamente!")
        return
    elif verificarDobleAs(mano_casa):
        print("¡La casa tiene doble A! ¡Pierdes!")
        return
    ronda = 1
    mostrarMano("Jugador", mano_jugador)
    mostrarMano("Casa", mano_casa)

    turno_jugador(mazo, mano_jugador)
    turno_casa(mazo, mano_casa)
    mostrarMano("Jugador", mano_jugador)
    mostrarMano("Casa", mano_casa)

    determinar_ganador(mano_jugador, mano_casa)

def valor_carta(carta):
    rango, _ = carta
    if rango in ['J', 'Q', 'K']:
        return 10
    elif rango == 'A':
        return 1
    else:
        return int(rango)
    

def crearBaraja():
    return [(rango, palo) for palo in SUITS for rango in RANKS]

def repartirCarta(mazo):
    return mazo.pop(random.randint(0, len(mazo) - 1))

def verificarDobleAs(mano):
    return sum(1 for rango, _ in mano if rango == 'A') == 2

def calcularPuntaje(mano):
    return sum(valor_carta(carta) for carta in mano)

def mostrarMano(jugador, mano):
    cartas = ', '.join([f"{rango} de {palo}" for rango, palo in mano])
    print(f"{jugador} tiene: {cartas} (Puntaje: {calcularPuntaje(mano)})")
    if jugador == "casa":
        print()

def turno_jugador(mazo, mano):
    if calcularPuntaje(mano) > 21:
        print("Te has pasado de 21. ¡Pierdes!")
        return False
    opcion = input("¿Quieres pedir otra carta (P) o plantarte (S)? ").upper()
    if opcion == 'P':
        mano.append(repartirCarta(mazo))
        return True
    elif opcion == 'S':
        return False
    else:
        print("Opción inválida. Escribe 'P' para pedir o 'S' para plantarte.")
        return turno_jugador(mazo, mano)

def turno_casa(mazo, mano):
    if calcularPuntaje(mano) <= 16:
        mano.append(repartirCarta(mazo))
        if calcularPuntaje(mano) > 21:
            print("La casa se ha pasado de 21. ¡Ganas!")
            return False
        return True
    else:
        return False

def determinar_ganador(mano_jugador, mano_casa):
    puntaje_jugador = calcularPuntaje(mano_jugador)
    puntaje_casa = calcularPuntaje(mano_casa)
    print(f"Puntaje final - Jugador: {puntaje_jugador}, Casa: {puntaje_casa}")
    if puntaje_jugador > 21:
        print("La casa gana.")
    elif puntaje_casa > 21 or puntaje_jugador > puntaje_casa:
        print("¡El jugador gana!")
    elif puntaje_jugador < puntaje_casa:
        print("La casa gana.")
    else:
        print("Empate.")

if __name__ == "__main__":
    blackjack()
