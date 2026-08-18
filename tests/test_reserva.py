import pytest 
from reserva import Reserva

def test_cria_reserva():
    r = Reserva("Ana", 101, 3, 250)
    assert r.valor_diaria == 250

def test_valor_negativo_da_erro():
    r = Reserva("Ana", 101, 3, 250)
    with pytest.raises(ValueError):
        r.valor_diaria = -100

def test_valor_zero_da_erro():
    r = Reserva("Ana", 101, 3, 250)
    with pytest.raises(ValueError):
        r.diarias = 0

def test_total_calcula():
    r = Reserva("Ana", 101, 4, 200)
    assert r.total == 800

def test_total_acompanha_mudanca():
    r = Reserva("Ana", 101, 4, 200)
    assert r.total == 800
    r.diaria = 5
    assert r.total == 1000
    r.valor_diaria = 250
    assert r.total == 1250