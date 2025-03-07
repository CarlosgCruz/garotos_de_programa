# Estruturas condicionais e de repetição

# if/ if-else/ elif

# exemplo

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
if saldo < saque:
    print("Saldo insuficiente!")

# exemplo

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# exemplo

opcao = int(input("informe uma opção: [1] sacar ou [2] extrato: "))

if opcao == 1:
    valor = float(input("informe a quantia para o saque: "))
    # ...
elif opcao == 2:
    print("exibindo extrato")
else: 
    SystemError.exit("opcao inválida")

# exemplo
"""
if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado!")
    else:
        print("saldo insuficiente")"""

# ESTRUTURAS DE REPETIÇÃO