"""
criar um sistema bancário com as operações: sacar, depositar e visualizar texto

desafio

fomos contratados por um grande banco para desenvolver o seu novo sistema.
esse banco deseja modernizar suas operações e para isso escolheu a linguagem python
para a primeira versão do sitema devemos implementar apenas 3 operações: depósito, saque e extrato.

operação de depósito

deve ser possível deppositar valores positivos para a minha conta bamcária. a v1 do projeto trabalha
apenas com 1 usario, desse forma nao precisamos nos preocupar em identificar qual é o numero da agencia 
e conta bancaria. todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato.

operação de saque

o sistema deve permitir realizar 3 saques diarios com limite máximo de 500 reais por saque
caso o usario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possivel
sacar o dinheiro por falta de saldo. todos os saques devem ser armazenados em uma variavel
e exibidos na operação extrato.

operação de extrato

essa operação deve listar todos os depositos e saques realizados na conta. no fim da listagem
deve ser exibido o saldo atual da conta

os valores devem ser exibidos utilizando o formato R$ xxx.xx
exemplo:

1500.45 = R$ 1500.45
"""

menu ="""
[d] depositar
[s] sacar
[e] extrato
[q] sair

"""

saldo = 0 
limite = 500 
extrato = ""
numero_saque = 0 
LIMITE_SAQUES = 3 

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

        else:
            print("operacao falhou! o valor informado é invalido.")
    
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operaçao falhou! voceê nao tem saldo suficiente.")
        
        elif excedeu_limite:
            print("operaçao falhou! o valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("operação falhou! numero máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque : R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("operaçao falhou! o valor informado pe invalido")

    elif opcao == "e":
        print("\n================= EXTRATO ===================")
        print("NAO FORAM REALIZADAS MOVIMENTAÇÕES ." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================================")

    elif opcao == "q":
        break

    else:
        print("operação invalida, por favor selecione novamente a operação desejada.")
