# ============================================================
# CALCULADORA SIMPLES EM PYTHON
# ============================================================

# 1. Definição das funções para cada operação matemática
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

# 2. Exibição do menu de opções para o utilizador
print("=== CALCULADORA SIMPLES ===")
print("Escolha a operação pretendida:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# 3. Entrada de dados: escolha da operação
opcao = input("Digite o número da operação (1/2/3/4): ")

# 4. Estrutura condicional para verificar a opção e realizar o cálculo
if opcao in ['1', '2', '3', '4']:
    # Entrada de dados: captura dos dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Identificação da operação escolhida e execução do cálculo
    if opcao == '1':
        resultado = somar(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {resultado}")
    elif opcao == '2':
        resultado = subtrair(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {resultado}")
    elif opcao == '3':
        resultado = multiplicar(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {resultado}")
    elif opcao == '4':
        resultado = dividir(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {resultado}")
else:
    print("Opção inválida! Por favor, escolha um número de 1 a 4.")