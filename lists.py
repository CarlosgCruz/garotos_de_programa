"""""
listas em python podem armazenar de maneira sequencial qualquer tipo de objeto
podemos criar listas utilizando o construtor "list" a função range ou colocando
valores separados por virgulas dentro de colchetes. listas são objetos mutaveis 
portanto podemos alterar seus valores após a criação.
"""

frutas = ["laranja", "maçã", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["ferrari", "f8", 420000, 2020, 2900, "sao paulo", True,]

"""
metodo de acessar os valores na lista

acesso direto

a lista é uma sequencia portanto podemos acessar seus dados utililzando indices
contamos o indice de determinada sequencia a partir do zero.
"""

frutas = ["laranja", "maçã", "uva"]
frutas = [0] # laranja
frutas = [2] # uva

"""
indices negativos

sequencias suportam indexação negativa. a contagem começa em -1

"""

frutas = ["laranja", "maçã", "uva"]
frutas = [-1] # uva
frutas = [-3] # laranja

"""
listas aninhadas

listas podem armazenar todos os tipos de objetos python, portanto podemos
ter listas que armazenam outras listas. com isso podemos criar estruturas
bidimensionais (tabelas) e acessar informando os indices de linha e coluna.

"""

matriz = [
    [1,"a",2]
    ["b",3,4]
    [6,5,"c"]
]

matriz[0] # [1,"a",2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

"""
fatiamento

alem de acessar elementos diretamente, podemos extrair um conjunto de valores
de uma sequencia. para isso basta passar o indice inicial e/ou final para acessar
o conjunto. podemos ainda informar quantas posiçoes o cursor deve "pular" no acesso

"""

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]
""
"""
iterar listas

a forma maos comum para percorrer os dados de uma lista é utilizando o comando for

"""

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

"""
funcao enumerate

as vezes é necessario saber qual o indice do objeto dentro do laço for. para isso
podemos usar a funcao enumerate.

"""

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")

"""
compreensão de listas

a compreensão de listas oferece uma sintaxe mais curta quando você deseja: criar
uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma
nova lista aplicando alguma modificação nos elementos de uma lista existente.

"""

# filtro versao 1

numeros = [1, 30, 21, 2, 9, 60, 24]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# filtro versao 2

numeros = [1, 30, 21, 2, 9, 60, 24]
pares = [numero for numero in numeros if numero % 2 == 0]

# modificando valores versao 1

numeros = [1, 30, 21, 2, 9, 60, 24]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# modificando valores versao 2

numeros = [1, 30, 21, 2, 9, 60, 24]
quadrado = [numero ** 2 for numero in numeros]

# metodos da classe list

# [].append

lista = []

lista.append(1)
lista.append("python")
lista.append([40, 30, 20])

print(lista) # [1, "pyhton", [40, 30, 20]]

# [].clear

lista = [1, "pyhton", [40, 30, 20]]

print(lista) # [1, "pyhton", [40, 30, 20]]

lista.clear()

print(lista) # []

# [].copy

lista = [1, "pyhton", [40, 30, 20]]

lista.copy()

print(lista)

# count
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelha") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# extend
linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) # ["python", "js", "c", "java", "csharp"]

# index
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3
linguagens.index("python") # 0

# pop
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

# remove
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) #["python", "js", "java", "csharp"]

# reverse
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) # ["csharp", "java", "c", "js", "python"]

# sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["pyhon", "js", "java", "csharp", "c"]


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]

# len
linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) # 5

# sorted
linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]

