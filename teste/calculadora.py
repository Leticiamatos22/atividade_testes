import math

class Calculadora:
    """Uma calculadora simples com operações básicas."""

    def somar(self, a, b):
        self._validar_parametros(a, b)
        return a + b

    def subtrair(self, a, b):
        self._validar_parametros(a, b)
        return a - b

    def multiplicar(self, a, b):
        self._validar_parametros(a, b)
        return a * b

    def dividir(self, a, b):
        self._validar_parametros(a, b)
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return a / b

    def potencia(self, base, expoente):
        self._validar_parametros(base, expoente)
        return base ** expoente

    def raiz_quadrada(self, a):
        self._validar_parametro_unico(a)
        if a < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        return math.sqrt(a)

    def modulo(self, a, b):
        self._validar_parametros(a, b)
        return a % b

    def _validar_parametros(self, a, b):
        """Valida se os dois parâmetros são números."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Os parâmetros devem ser números.")

    def _validar_parametro_unico(self, a):
        """Valida se um único parâmetro é um número."""
        if not isinstance(a, (int, float)):
            raise ValueError("O parâmetro deve ser um número.")

def main():
    calc = Calculadora()
    print("Bem-vindo à Calculadora!")
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potência")
        print("6. Raiz Quadrada")
        print("7. Módulo")
        print("8. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "8":
            print("Encerrando a calculadora. Até mais!")
            break

        try:
            if escolha in ["1", "2", "3", "4", "5", "7"]:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))

                if escolha == "1":
                    print(f"Resultado: {calc.somar(a, b)}")
                elif escolha == "2":
                    print(f"Resultado: {calc.subtrair(a, b)}")
                elif escolha == "3":
                    print(f"Resultado: {calc.multiplicar(a, b)}")
                elif escolha == "4":
                    print(f"Resultado: {calc.dividir(a, b)}")
                elif escolha == "5":
                    print(f"Resultado: {calc.potencia(a, b)}")
                elif escolha == "7":
                    print(f"Resultado: {calc.modulo(a, b)}")
            elif escolha == "6":
                a = float(input("Digite o número: "))
                print(f"Resultado: {calc.raiz_quadrada(a)}")
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}")

if __name__ == "__main__":
    main()
