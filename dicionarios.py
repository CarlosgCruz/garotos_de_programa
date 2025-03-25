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


# metodos da classe dict