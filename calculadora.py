def calculadora():
    while True:
        print("\n--- CALCULADORA PYTHON ---")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == '5':
            print("Encerrando a calculadora. Até logo!")
            break
            
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos.")
                continue
                
            if opcao == '1':
                resultado = num1 + num2
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"\nResultado: {num1} * {num2} = {resultado}")
            elif opcao == '4':
                if num2 == 0:
                    print("\nErro: Não é possível dividir por zero!")
                else:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("Opção inválida! Tente novamente.")

# Executa a calculadora
calculadora()
