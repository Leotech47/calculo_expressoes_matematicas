while True:
    print("\nDigite uma expressão matemática completa (ex: 5 + 3 * 2)")
    print("Operações suportadas: +, -, *, /, ** (potência), % (módulo)")
    print("Para encerrar, digite 'sair'.")

    expressao = input("Digite a expressão: ").lower()

    if expressao == "sair":
        print("Encerrando a calculadora avançada. Até mais!")
        break

    try:
        # Avalia a expressão digitada pelo usuário
        resultado = eval(expressao, {"__builtins__": None}, {})
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero")
    except Exception as e:
        print("Erro: expressão inválida")
