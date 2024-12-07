from calculadora import Calculadora
import pytest
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def log_test(func):
    """Decorador para logar o início e o fim de cada teste."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Iniciando teste: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Teste concluído: {func.__name__}")
        return result
    return wrapper

@pytest.fixture
def calc():
    """Fixture para criar uma instância da calculadora."""
    return Calculadora()

# Testes para soma
@log_test
def test_soma_sucesso(calc):
    assert calc.somar(5, 3) == 8
    assert calc.somar(-1, 1) == 0
    assert calc.somar(2.5, 1.5) == 4.0

@log_test
def test_soma_erro_parametros_invalidos(calc):
    with pytest.raises(ValueError):
        calc.somar("cinco", 3)
    with pytest.raises(ValueError):
        calc.somar(5, None)

# Testes para subtração
@log_test
def test_subtracao_sucesso(calc):
    assert calc.subtrair(10, 5) == 5
    assert calc.subtrair(-3, -3) == 0
    assert calc.subtrair(3.5, 1.5) == 2.0

@log_test
def test_subtracao_erro_parametros_invalidos(calc):
    with pytest.raises(ValueError):
        calc.subtrair(10, "cinco")
    with pytest.raises(ValueError):
        calc.subtrair(None, 5)

# Testes para multiplicação
@log_test
def test_multiplicacao_sucesso(calc):
    assert calc.multiplicar(4, 3) == 12
    assert calc.multiplicar(-2, 3) == -6
    assert calc.multiplicar(2.5, 4) == 10.0

@log_test
def test_multiplicacao_erro_parametros_invalidos(calc):
    with pytest.raises(ValueError):
        calc.multiplicar("quatro", 3)
    with pytest.raises(ValueError):
        calc.multiplicar(4, [])

# Testes para divisão
@log_test
def test_divisao_sucesso(calc):
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(-9, 3) == -3
    assert pytest.approx(calc.dividir(7, 3), 0.0001) == 2.3333

@log_test
def test_divisao_erro_divisao_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)

@log_test
def test_divisao_erro_parametros_invalidos(calc):
    with pytest.raises(ValueError):
        calc.dividir("dez", 2)
    with pytest.raises(ValueError):
        calc.dividir(10, {})

# Testes para potência
@log_test
def test_potencia_sucesso(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(-2, 3) == -8

@log_test
def test_potencia_erro_parametros_invalidos(calc):
    with pytest.raises(ValueError):
        calc.potencia("dois", 3)
    with pytest.raises(ValueError):
        calc.potencia(2, None)

# Testes para raiz quadrada
@log_test
def test_raiz_quadrada_sucesso(calc):
    assert calc.raiz_quadrada(16) == 4
    assert calc.raiz_quadrada(0) == 0
    assert pytest.approx(calc.raiz_quadrada(2), 0.0001) == 1.4142

@log_test
def test_raiz_quadrada_erro_numero_negativo(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-4)

@log_test
def test_raiz_quadrada_erro_parametro_invalido(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada("dez")
    with pytest.raises(ValueError):
        calc.raiz_quadrada([])

# Testes para módulo
@log_test
def test_modulo_sucesso(calc):
    assert calc.modulo(10, 3) == 1
    assert calc.modulo(15, 5) == 0
    assert calc.modulo(-10, 3) == 2

@log_test
def test_modulo_erro_parametros_invalidos(calc):
    with pytest.raises(ValueError):
        calc.modulo(10, "três")
    with pytest.raises(ValueError):
        calc.modulo(10, [])
