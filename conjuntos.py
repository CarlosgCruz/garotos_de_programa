# objetivo geral 

# entender o funcionamento da estrutura de dados set.

"""
criando sets

um set é uma coleçao que nao possui objetos repetidos, usamos sets para representar
conjuntos matemáticos ou eliminar itens de um iterável.

"""

# exemplo

"""set = set([1,2,3,1,3,4]) # {1,2,3,4}

print(set)

"""
nomes = set(["gilmar", "carlos", "sousa", "gilmar"])

print(nomes)

# acessando os dados 

"""
conjuntos em python não suportam indexação e nem fatiamento, caso queira os seus valores
é necessario converter o conjunto para lista

"""

numeros = {1,2,3,2}

numeros = list(numeros)

print(numeros[0])

# iterar conjuntos

# a forma mais comum para percorrer os dados de um conjunto é utilizando o comando for.

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# funcao enumerate

# as vezes é necessario saber qual o indice do objeto dentro do laço for. para isso podemos usar a função enumerate.

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# metodos da classe set

# {}.union

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))

# {}.intersection

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))

# {}.difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# {}.symmetric_difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.symmetric_difference(conjunto_b))

# {}.issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# {}.issuperset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# {}.isdisjoint

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

# {}.add

sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

# {}.clear

sorteio = {1,23}

sorteio.clear()

print(sorteio)

# {}.discard

numeros1 = {1,2,3,1,2,4,5,6,7,8,9,0}

print(numeros1)
numeros1.discard(1)
numeros1.discard(45)
print(numeros1)

# {}.remove

numeros1 = {1,2,3,1,2,4,5,6,7,8,9,0}

print(numeros1)

numeros1.remove(0)

print(numeros1)

#len

numeros1 = {1,2,3,1,2,4,5,6,7,8,9,0}

print(len(numeros1))

# in

numeros1 = {1,2,3,1,2,4,5,6,7,8,9,0}

print(1 in numeros1)
print(10 in numeros1)