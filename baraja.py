class Carta:
    def __init__(self, valor, simbolo, palo):
        self.validar_carta()
        self.valor = valor
        self.simbolo = simbolo
        self.palo = palo

    def validar_carta(self):
        if not isinstance(self.valor, int):
            raise ValueError('El valor debe la carta debe ser un entero')
        if not isinstance(self.simbolo, str):
            raise ValueError('El símbolo debe la carta debe ser una string')
        if isinstance(self.palo, str):
            raise ValueError('El palo debe la carta debe ser un string')

    def __str__(self) -> str:
        return f"{self.valor} {self.simbolo}{self.palo}"

    def __repr__(self) -> str:
        return self.__str__

    def __eq__(self, otro: object) -> bool:
        return self.valor == otro.valor

    def __ne__(self, otro: object) -> bool:
        return self.valor != otro.valor

    def __gt__(self, otro):
        return self.valor > otro.valor

    def __ge__(self, otro):
        return self.valor >= otro.valor

    def __lt__(self, otro):
        return self.valor < otro.valor

    def __le__(self, otro):
        return self.valor <= otro.valor


class Baraja:
    pass
