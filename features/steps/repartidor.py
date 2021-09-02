from behave import *
from veintiuna import *

# Escenario que reparte dos cartas al repartidor
@Given('un repartidor')
def step_imp(context) -> None:
    context.repartidor = Repartidor()

@When('el juego inicia')
def step_imp(context) -> None:
    context.repartidor.nueva_mano()

@Then('el repartidor toma dos cartas')
def step_imp(context) -> None:
    assert len(context.repartidor.mano) == 2

# Escenario que determina el valor de la mano del repartidor
@Given('una mano {mano}')
def step_imp(context, mano: str) -> None:
    context.repartidor = Repartidor()
    context.repartidor.mano = [(x, 'Picas') for x in mano.split(', ')]

@When('el repartidor sume las cartas')
def step_imp(context) -> None:
    context.repartidor.sumar_mano()
    context.valor_mano = context.repartidor.valor_mano

@Then('el resultado {valor:d} sea correcto')
def step_imp(context, valor: int) -> None:
    assert context.valor_mano == valor

# Escenario que determina la jugada del repartidor a partir de la jugada del jugador
@Given('el valor de la mano {jugador:d} del jugador y el valor de la mano {repartidor:d} del repartidor')
def step_imp(context, jugador: int, repartidor: int) -> None:
    context.repartidor = Repartidor()
    context.repartidor.valor_mano = repartidor
    context.valor_mano_jugador = jugador

@When('el repartidor determina la jugada')
def step_imp(context) -> None:
    context.jugada = context.repartidor.decidir_jugada(context.valor_mano_jugador)

@Then('la jugada {jugada} es correcta')
def step_imp(context, jugada: str) -> None:
    assert context.jugada == jugada
