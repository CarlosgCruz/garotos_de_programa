# criação e acesso aos dados

"""
criando dicionarios 

um dicionario é um conjunto não ordenado de pares chave:valor, onde as chaves são unicas
em uma dada instancia do dicionario. dicionarios sao delimitados por chaves: {}, e contem
uma lista de pares chave:valor separada por virgulas.
"""

# exemplo

pessoa = {"nome": "gilmar", "idade": 21}

pessoa = dict(nome="gilmar", idade=28)

pessoa["telefone"] = "3333-1235"

print(pessoa)

# acesso aos dados
# os dados são acessados e modificados atraves da chave

dados = {"nome": "gilmar", "idade": 21, "telefone": "3333-1234"}

print(dados["nome"])  # "gilmar"
print(dados["idade"])  # 21
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

# dicionarios aninhados
"""
dicionarios pode armazenar qualquer tipo de objeto pyhton como valor, desde que a 
chave para esse valor seja um objeto imutavel como (strings e numeros)
"""

contatos = {
    "joao@gmail.com": {"nome": "joao", "telefone": "3333-2221"},
    "jorge@gmail.com": {"nome": "jorge", "telefone": "3443-2121"},
    "carlos@gmail.com": {"nome": "carlos", "telefone": "3344-9871"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "3333-7766"},
}

telefone = contatos["giovana@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

# iterar dicionarios
# a forma mais comum para percorrer os dados de um dicionario é utilizando o comando for 

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)


# metodos da classe dict