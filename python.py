print("hello world") 
# são os tipos de dados em python

# textos são str
# numericos são int, float, complex
# sequencia são list, tuple, range
# mapa são dict
# coleção são set, fronzenset
# booleano são bool
# binario são bytes, bytearray, memoryview

# variaveis

age = 21
name = 'gilmar'
print(f'meu nome é {name} e eu tenho {age} anos')

#constante

NOME = "gilmar"

# convertendo tipos
# inteiro para float

preco = 10
print(preco)

#convertendo de int para float

preco = float(preco)
print(preco)

#mais um exemplo

preco = 10/2
print(preco)

# de float para int

preco = 10.30
print(preco)

preco = int(preco)
print(preco)

# conversão por divisão

preco = 10 
print(preco)

print(preco / 2)

print(preco // 2)

#numerico para string

preco = 10.50
idade = 28

print(str(preco , idade))

texto = f"idade {idade} {preco}"
print(texto)

# de string para número

preco = "10.50"
idade = "28"

print(float(preco))

print(int(idade))

# funções de entrada e saida python

# ex
nome = input("informe seu nome")
