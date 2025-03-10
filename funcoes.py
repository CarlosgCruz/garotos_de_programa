# exemplo de funcao

def exibir_mensagem():
    print("ola mundo!")

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}!")

def exibir_mensagem_3(nome="anonimo"):
    print(f"seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="chappie")

# retornando valores

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = - 1
    sucessor = + 1

    return antecessor, sucessor

calcular_total([10, 20, 34]) # 64
retorna_antecessor_e_sucessor(10) #(9, 11)

# argumentos nomeados

# exemplo

def salvar_carro(marca, modelo, ano, placa):
    # salvar carro no banco de dados...
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# args e kwargs
# *args **kwargs

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}]: {valor}"for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("zen of python", "beautiful is better than ugly.", autor="tim peters", ano = 1999)

# parametros especiais

"""def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        ............    ...........     .........
            |             |                 |
            |        Positional or keyword  |
            |                               - Keyword only
             -- Positional only
"""

# position only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("palio", 1999, "ABC-1234", marca="fiat", motor=1.0, combustivel="gasolina") #valido

criar_carro(modelo="palio", ano=1999, placa="ABC-1234", marca="fiat", motor=1.0, combustivel="gasolina") #invalido

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("palio", 1999, "ABC-1234", marca="fiat", motor=1.0, combustivel="gasolina") #valido

criar_carro(modelo="palio", ano=1999, placa="ABC-1234", marca="fiat", motor=1.0, combustivel="gasolina") #invalido

# objetos de primereira classe 

# exemplo

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o resultado {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # o resultado da operação 10 + 10 = 20 

