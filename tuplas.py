# criando tuplas

"""
tuplas são estruturas de dados muito parecidas com as listas, a principal diferença
é que tuplas são imutaveis enquanto listas são mutaveis. podemos criar tuplas atraves
da classe tuple, ou colocando valores separados por virgula de parenteses.
"""

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("brasil",)

frutas = ("maçã", "laranja", "uva", "pera",)

frutas[0]
frutas[2]

frutas = ("maçã", "laranja", "uva", "pera",)

frutas[-1]
frutas[-3]

# tuplas aninhadas

"""
tuplas podem armazenar todos os tipos de objetos python,portanto podemos ter tuplas
que armazenam outras tuplas. com isso podemos criar estruturas bidimensionais(tabelas)
e acessar informando os indices de linha e coluna.
"""

matriz = (
    (1,"a",2),
    ("b",3,4),
    (6,5,"c"),
)

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

lista = ["p", "y", "t", "h", "o", "n",]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

# count
cores = ["vermelho", "azul", "verde", "azul",]

cores.count("vermelha") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# len
linguagens = ["python", "js", "c", "java", "csharp",]

len(linguagens) # 5
