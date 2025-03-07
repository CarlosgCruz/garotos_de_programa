# ESTRUTURAS DE REPETIÇÃO

# exemplo sem repetição

a = int(input("informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

# outro exemplo

# receba um número do teclado e exiba os 2 número seguintes

# exemplo com repetição

"""a = int(input("informe um número inteiro: "))
print(a)

repita 2 vezes:
    a += 1
    print(a)"""

# COMANDO FOR

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# for/else

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()

# função range

# range(stop) -> range objet
# range(start, stop[, step]) -> range object

list(range(4))

# utilizando range com for

for numero in range(0, 11):
    print(numero, end=" ")
    
for numero in range(0, 51, 5):
    print(numero, end=" ")

# comando while

opcao = 1 

while opcao != 0:
    opcao = int(input("[1]sacar [2] extrato [0] sair :"))

    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("exibindo o extrato")

