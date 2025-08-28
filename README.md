
# Calculadora Avançada Interativa em Python

Esta é uma versão avançada da **mini-calculadora interativa** em Python. Ela permite que o usuário digite **expressões matemáticas completas**, como `5 + 3 * 2`, e calcula o resultado respeitando a **ordem de precedência das operações**.

---

## Funcionalidades

A calculadora suporta:

| Operação | Símbolo | Exemplo |
|----------|---------|---------|
| Soma | `+` | `5 + 3` |
| Subtração | `-` | `10 - 4` |
| Multiplicação | `*` | `2 * 3` |
| Divisão | `/` | `8 / 2` |
| Potência | `**` | `2 ** 3` |
| Módulo | `%` | `10 % 3` |
| Parênteses | `( )` | `(5 + 3) * 2` |
| Encerrar | `sair` | Encerra a calculadora |

---

## Explicação linha por linha

```python
while True:
````

* Cria um **loop infinito**, permitindo que o usuário faça várias operações sem reiniciar o programa.
* O loop só termina se o usuário digitar `"sair"`.

```python
    print("\nDigite uma expressão matemática completa (ex: 5 + 3 * 2)")
    print("Operações suportadas: +, -, *, /, ** (potência), % (módulo)")
    print("Para encerrar, digite 'sair'.")
```

* Exibe instruções e exemplos de como usar a calculadora.

```python
    expressao = input("Digite a expressão: ").lower()
```

* Solicita que o usuário digite a expressão.
* `.lower()` transforma a entrada em minúsculas para facilitar o controle (por exemplo, para o comando `"SAIR"`).

```python
    if expressao == "sair":
        print("Encerrando a calculadora avançada. Até mais!")
        break
```

* Verifica se o usuário digitou `"sair"`.
* Se sim, encerra o loop e finaliza o programa.

```python
    try:
        resultado = eval(expressao, {"__builtins__": None}, {})
        print("Resultado:", resultado)
```

* Usa a função `eval()` para **avaliar a expressão matemática digitada pelo usuário**.
* O segundo argumento `{"__builtins__": None}` impede o acesso a funções ou objetos Python potencialmente perigosos, tornando o uso do `eval` **mais seguro**.
* O terceiro argumento `{}` define um **escopo vazio**, garantindo que apenas operações matemáticas sejam avaliadas.
* Mostra o resultado da expressão.

```python
    except ZeroDivisionError:
        print("Erro: divisão por zero")
```

* Trata especificamente o caso de divisão por zero.

```python
    except Exception as e:
        print("Erro: expressão inválida")
```

* Captura qualquer outro erro (como erro de sintaxe) e exibe uma mensagem amigável.

---

## Como executar

1. Certifique-se de ter **Python 3** instalado.
   Verifique com:

   ```bash
   python --version
   ```

2. Salve o código em um arquivo chamado, por exemplo, `calculadora_avancada.py`.

3. Abra o terminal e navegue até o diretório do arquivo.

4. Execute o programa:

   ```bash
   python calculadora_avancada.py
   ```

5. Siga as instruções:

   * Digite a expressão completa que deseja calcular.
   * Para encerrar, digite `"sair"`.

---

## Exemplos de execução

```
Digite a expressão: 5 + 3 * 2
Resultado: 11

Digite a expressão: (10 - 2) / 4
Resultado: 2.0

Digite a expressão: 2 ** 3 + 1
Resultado: 9

Digite a expressão: sair
Encerrando a calculadora avançada. Até mais!
```

---

## Observações

* A calculadora **respeita a ordem de precedência das operações**.
* Permite o uso de **parênteses** para alterar a ordem.
* Valida erros comuns como **divisão por zero** e **expressões inválidas**.
* Pode ser expandida facilmente para incluir novas funções matemáticas, como seno, cosseno, logaritmo, etc., usando a biblioteca `math`.

---

Esta calculadora é ideal para **estudantes de Python** ou quem deseja aprender a criar **interfaces de linha de comando interativas** e **avaliar expressões matemáticas** de forma segura.

```

