class Reserva:
    def __init__(self, hospede, quarto, diaria, valor_diaria):
        self.hospede = hospede
        self.quarto = quarto
        self.diaria = diaria
        self.valor_diaria = valor_diaria

    @property
    def valor_diaria(self):
        return self._valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, value):
        if value < 0:
            raise ValueError("O valor da diária não pode ser negativo")
        self._valor_diaria = value

    @property
    def diarias(self):
        return self.diaria

    @diarias.setter
    def diarias(self, value):
        if value <= 1:
            raise ValueError("O número de diárias não pode ser negativo")
        self._diaria = value

    @property
    def total(self):
        return self.diaria * self.valor_diaria