#Lista com todas as unidaddes de armazenamento
lista=['bit', 'byte', 'kb', 'mb', 'gb', 'tb', 'pb']
unidade1=input(f"Digite o numero da unidade de medida a ser convertida: :{lista} ")
while not unidade1 in lista:
    unidade1=input(f"Digite o numero da unidade de medida a ser convertida: :{lista} ")
unidade2=input(f"Digite o numero da unidade em que será convertida: {lista}: ")
while not unidade2 in lista:
    unidade2=input(f"Digite o numero da unidade em que será convertida: {lista}: ")

numero=int(input("Agora digite a quantidade de memoria: "))

if unidade1 == 'bit':
    numero /= 8
    unidade1 = "byte"

posicao1 =lista.index(unidade1)
posicao2 =lista.index(unidade2)
distancia = posicao2 - posicao1

def calculo(numero):
    numero /= 1024**distancia
    return numero

if unidade2 == 'bit':
    numero = (numero/1024)*8
print(calculo(numero))