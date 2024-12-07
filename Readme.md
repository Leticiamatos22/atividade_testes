# Calculadora Simples

Este é um projeto de uma **calculadora simples** implementada em Python, que inclui operações básicas como soma, subtração, multiplicação, divisão, potência, raiz quadrada e módulo. O projeto também inclui testes automatizados utilizando o framework **pytest** para garantir o correto funcionamento de cada operação.

## Requisitos

- Python 3.x
- pytest (para execução dos testes)

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .env
   source .env/bin/activate  # No Linux ou macOS
   .env\Scripts\activate  # No Windows
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do Projeto

- **calculadora.py**: Implementação da classe `Calculadora` com as funções de operações matemáticas.
- **teste_calculadora.py**: Arquivo de testes utilizando pytest para testar as funcionalidades da calculadora.
- **README.md**: Este arquivo com as informações sobre o projeto.

## Funcionalidades

A classe `Calculadora` implementa as seguintes operações:

- **somar(a, b)**: Retorna a soma de `a` e `b`.
- **subtrair(a, b)**: Retorna a diferença de `a` e `b`.
- **multiplicar(a, b)**: Retorna o produto de `a` e `b`.
- **dividir(a, b)**: Retorna a divisão de `a` por `b`, levantando erro em caso de divisão por zero.
- **potencia(base, expoente)**: Retorna o resultado de `base` elevado à potência de `expoente`.
- **raiz_quadrada(a)**: Retorna a raiz quadrada de `a`, levantando erro em caso de número negativo.
- **modulo(a, b)**: Retorna o módulo de `a` e `b`.

## Testes

Os testes são realizados utilizando o framework **pytest**. Eles cobrem todos os casos possíveis de cada operação, incluindo:

- Testes de sucesso para valores válidos.
- Testes de erro para valores inválidos, como strings ou `None`.
- Testes para operações como divisão por zero e raiz quadrada de números negativos.

### Comando para Rodar os Testes

Para rodar os testes, utilize o seguinte comando no terminal:

```bash
pytest teste_calculadora.py
```

Ou, para rodar todos os testes do projeto:

```bash
pytest
```

## Exemplo de Execução

### Usando a calculadora

Você pode executar a calculadora a partir do arquivo `calculadora.py`. Ao rodá-lo, será solicitado que o usuário escolha uma operação e forneça dois números (ou apenas um número, no caso da raiz quadrada).

```bash
python calculadora.py
```

Isso iniciará um menu interativo onde você pode escolher a operação desejada.

## Autoria

- **Letícia Cristina de Matos**
- **Trabalho apresentado como requisitos para aprovação da disciplina de Engenharia de Software**.
- **2024**

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Se você tiver algum outro ponto que gostaria de adicionar ou modificar, posso ajudar a personalizar ainda mais!