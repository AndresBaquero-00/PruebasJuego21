from veintiuna import *

repartidor = Repartidor()

# Prueba para el inicio del juego con el repartidor
# El resultado esperado es dos cartas en una mano
def test_nueva_mano() -> None:
    repartidor.nueva_mano()
    assert len(repartidor.mano) == 2

# Prueba para determinar si hay un as en la mano
# El resultado esperado es verdadero
def test_tiene_as_true() -> None:
    repartidor.mano = [('A', 'Treboles'), ('A', 'Picas'), ('3', 'Picas')]
    assert repartidor.tiene_as() == True

# Prueba para determinar si hay un as en la mano
# El resultado esperado es falso
def test_tiene_as_false() -> None:
    repartidor.mano = [('Q', 'Treboles'), ('8', 'Picas'), ('3', 'Diamantes')]
    assert repartidor.tiene_as() == False

# Prueba para determinar el valor de la carta si es una letra
# El resultado esperado es 10 en este caso
def test_valor_carta_letra() -> None:
    carta = ('J', 'Picas')
    assert repartidor.valor_carta(carta) == 10

# Prueba para determinar el valor de la carta si esta es un numero
# El resultado esperado es 8 en este caso
def test_valor_carta_numero() -> None:
    carta = ('8', 'Picas')
    assert repartidor.valor_carta(carta) == 8

# Prueba para determinar el valor total de la mano
# El resultado esperado es 21 en este caso
def test_valor_mano() -> None:
    repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
    repartidor.sumar_mano()
    assert repartidor.valor_mano == 21

# Prueba para determinar la jugada del repartidor a partir de la jugada del jugador
# El resultado esperado es que el repartidor siga jugando
def test_jugada_jugar() -> None:
    repartidor.valor_mano = 15
    valor_mano_jugador = 16
    assert repartidor.decidir_jugada(valor_mano_jugador) == 'jugar'

# Prueba para determinar la jugada del repartidor a partir de la jugada del jugador
# El resultado esperado es que el repartidor siga jugando
def test_jugada_plantar() -> None:
    repartidor.valor_mano = 17
    valor_mano_jugador = 15
    assert repartidor.decidir_jugada(valor_mano_jugador) == 'plantar'