# calculadora

operacao = input("escolha uma operação matemática(+-*/): ")
a = int(input("escolha um número de 1 a 1000: "))
b = int(input("escolha um número de 1 a 1000: "))
resutado_soma = a + b
resultado_sub = a - b
resultado_multi = a * b
resultado_div = a / b

if operacao == "+" :
    print(f"p resultado é: {resutado_soma}")

elif operacao == "-":
    print(f"p resultado é: {resultado_sub}")

elif operacao == "*":
    print(f"p resultado é: {resultado_multi}")

elif operacao == "/":
    print(f"p resultado é: {resultado_div}")