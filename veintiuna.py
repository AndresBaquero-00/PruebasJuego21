from random import choice

_valores = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
_pintas = ['Picas', 'Corazones', 'Diamantes', 'Treboles']
_cartas = [(v, p) for v in _valores for p in _pintas]

class Repartidor:
    def __init__(self) -> None:
        self.mano = []
        self.valor_mano = 0

    def nueva_mano(self) -> None:
        self.mano = [choice(_cartas), choice(_cartas)]
    
    def sumar_mano(self) -> None:
        valor = 0
        for carta in self.mano:
            valor += self.valor_carta(carta)

        if self.tiene_as() and valor <= 11:
            valor += 10
        
        self.valor_mano = valor

    def valor_carta(self, carta: tuple) -> int:
        if carta[0] in ['J', 'Q', 'K']:
            return 10
        elif carta[0] == 'A':
            return 1
        else:
            return int(carta[0])

    def tiene_as(self) -> bool:
        for carta in self.mano:
            if carta[0] == 'A':
                return True
        return False

    def decidir_jugada(self, mano_jug: int) -> str:
        if mano_jug <= self.valor_mano or mano_jug > 21:
            return 'plantar'
        else:
            return 'jugar'