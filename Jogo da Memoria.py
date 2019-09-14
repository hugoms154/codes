#######################################################################
###                                                                 ###
###              Universidade Federal do Rio de Janeiro             ###
###           Centro de Ciências Matemáticas e da Natureza          ###
###          Bacharelado em Ciências Matemáticas e da Terra         ###
###                                                                 ###
#######################################################################
###                                                                 ###
###     Desenvolvedor(es): Hugo Miranda e Souza                     ###
###     DRE: 118043403                                              ###
###                                                                 ###
###     Professora: Lenka Ptackova                                  ###
###     Disciplina: [MAB241] Computação II                          ###
###                                                                 ###
###     Descrição: Jogo da memória no console/IDLE Python           ###
###     Python Version: 3.7.3                                       ###
###     Data: 23/08/2019                                            ###
###                                                                 ###
#######################################################################

import random

## Function: criaMapa
## Descrição: Cria a matriz numerica no padrão (exemplo abaixo)
## .......... 4x4 do mapa do jogo
## Entrada: [-]
## Saida: [Matriz numerica 4x4]
## Padrão: [[3, 8, 5, 6], [7, 7, 5, 3], [2, 8, 6, 4], [1, 4, 2, 1]]
def criaMapa():
    possibilidades = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    mapa = []
    for i in range(4):
        linha = []
        for j in range(4):
            sorteia = random.sample(possibilidades, 1)
            possibilidades.remove(sorteia[0])
            linha.append(sorteia[0])
        mapa.append(linha)
    return mapa

## Function: orgMapa
## Descrição: Gera o mapa em um texto organizado para exibição. (exemplo abaixo)
## Entrada: [Matriz numerica]
## OBS.: Matriz numerica é o retorno da function criaMapa()
## Saida: [Texto para exibição da matriz 4x4]
## Exemplo:
## 6   8   3   4   
## 1   7   5   2   
## 7   3   4   5   
## 1   2   6   8
def orgMap(mapa):
    maptext = ""
    for l in range(len(mapa)):
        for c in range(len(mapa[l])):
            maptext += "{}\t".format(mapa[l][c]).expandtabs(4)
        maptext += "\n"
    return maptext


## Function: maskMap
## Descrição: Gera mascara do mapa em texto, com todos os pontos
## .......... como " * " para exibição. (exemplo abaixo)
## Entrada: [Matriz numerica]
## Saida: [Texto para exibição da mascara da matriz 4x4]
## Exemplo: 
## *   *   *   *   
## *   *   *   *   
## *   *   *   *   
## *   *   *   *
def maskMap(mapa):
    mapmask = ""
    for l in range(len(mapa)):
        for c in range(len(mapa[l])):
            mapmask += "*\t".expandtabs(4)
        mapmask += "\n"
    return mapmask

## Function: maskMatriz
## Descrição: Gera matriz da mascara do mapa. (exemplo abaixo)
## Entrada: [String da mascara da matriz numerica]
## OBS.: String de return da function maskMap()
## Saida: [Matriz da mascara]
## Exemplo: [['', '', '', ''], ['', '', '', ''],
## ........ ['', '', '', ''], ['', '', '', '']]
def maskMatriz(mask):
    tmp = mask.split("\n", 3)
    result = []
    for i in tmp:
        result.append(i.split())
    return result

## Function: mesclaMapaArray
## Descrição: Mescla o mapaArray + maskMap substituindo os pontos
## .......... selecionados pelo valor real. (exemplo abaixo)
## Entrada: [Matriz numerica], [Matriz mascara],
## ........ [Jogada: [x1, y1, x2, y2]]
## Saida: []
## Exemplo:
## 3   *   *   *   
## *   *   *   3   
## *   *   *   *   
## *   *   *   *
def mesclaMapaArray(mapaArray, maskArray, jogada):
    maptext = ""
    for l in range(len(maskArray)):
        for c in range(len(maskArray[l])):
            if (l == jogada[0] and c == jogada[1]):
                maptext += "{}\t".format(mapaArray[l][c]).expandtabs(4)
            elif(l == jogada[2] and c == jogada[3]):
                maptext += "{}\t".format(mapaArray[l][c]).expandtabs(4)
            else:
                maptext += "*\t".expandtabs(4)
        maptext += "\n"
    return maptext

## Function: acertou
## Descrição: Verifica se os valores selecionados são iguais
## Entrada: [Array numerica], [array de coordenadas da jogada]
## Saida: [True/False]
def acertou(mapaArray, jogada):
    return True if\
           mapaArray[jogada[0]][jogada[1]] == mapaArray[jogada[2]][jogada[3]]\
           else False

## Function: validaJogada
## Descriçao: Verifica se o valor jogado está dentro da matriz do jogo, se nao foram descobertos ou se sao iguais
## Entrada: [Matriz numerica], [Jogada: [x1, y1, x2, y2]], [Matriz Nºs descobertos]
## Saida: [True/False]
def validaJogada(mapaArray, jogada, descobertos):
    # Ordem das verificações:
        # Verifica x1 está dentro dos limites de 4x4
        # Verifica y1 está dentro dos limites de 4x4
        # Verifica x2 está dentro dos limites de 4x4
        # Verifica y2 está dentro dos limites de 4x4
        # Verifica se [x1, y1] nao foram descobertos ainda
        # Verifica se [x2, y2] nao foram descobertos ainda
        # Verifica se os valores de X, Y: 1 e 2 nao sao iguais
    return True if \
         jogada[0] in range(len(mapaArray))\
         and\
         jogada[1] in range(len(mapaArray[0]))\
         and\
         jogada[2] in range(len(mapaArray))\
         and\
         jogada[3] in range(len(mapaArray[0]))\
         and\
         jogada[0:2] not in descobertos\
         and\
         jogada[2:4] not in descobertos\
         and\
         not jogada[0:2] == jogada[2:4]\
         else False

## Function: efetivaJogada
## Descrição: Caso o jogador tenha acertado a jogada essa função a efetiva, ou seja, substitui os numeros na matriz mask
## Entrada: [Matriz numerica] [Matriz da mascara],
## ........ [Jogada: [x1, y1, x2, y2]], [Matriz Nºs descobertos]
def efetivaJogada(mapaArray, maskArray, jogada, descobertos):
    mescla = list(maskArray)
    if acertou(mapaArray, jogada) == True:
        descobertos.append(jogada[0:2])
        descobertos.append(jogada[2:4])
        for l in range(len(maskArray)):
            for c in range(len(maskArray[l])):
                if (l == jogada[0] and c == jogada[1]):
                    maskArray[l][c] = mapaArray[jogada[0]][jogada[1]]
                if(l == jogada[2] and c == jogada[3]):
                    maskArray[l][c] = mapaArray[jogada[2]][jogada[3]]
                    print("Parabéns! Você acertou!.")
        return maskArray
    else:
        print("Você errou, tente novamente.")
        return mescla
    return -1

## Function ganhei
## Descrição: Verifica se todos os numeros ja foram descobertos.
## .......... Retorna True caso sim, senão False
## Entrada: [Matriz mescla]
## Saida: [True/False]
def ganhei(mesclaArray):
    for l in range(len(mesclaArray)):
        for c in range(len(mesclaArray[l])):
            if mesclaArray[l][c] == '*':
                return False
    return True

## Function: main
## Descrição: Coordenada o jogo, inicializa as variaveis necessarias,chama as demais funções para seu funcionamento.
## Entrada: [-]
## Saida: [-]
def main():
    mapaArray = criaMapa()
    mapa = orgMap(mapaArray)
    mask = maskMap(mapaArray)
    maskArray = maskMatriz(mask)
    jogada = [-1, -1, -2, -2]
    ganhou = False
    jogadas = 0
    descobertos = []
    print("-->Esse é um jogo da memoria, voce deve achar todos os pares de \
numeros dentro deste quadrado.")
    print("-->Para selecionar o numero qual voce quer ver digite \
as coordenadas x e y de dois numeros")
    print("-->OBS.: A contagem, começa a partir do 0, para as linhas e \
colunas. Entao para um jogo 4x4 (como este), os valores variam entre 0 e 3")
    print("-->Ex.: Digite as coordenadas:\n-->x1 = 0\n-->y1 = 0\n-->x2 = 1\n-->y2 = 0")
    print(mask)
    mesclaArray = []
    while ganhou == False:  # Enquanto todos os numeros nao forem descobertos continua pedindo coordenadas
        while validaJogada(mapaArray, jogada, descobertos) == False:
            print("Digite as coordenadas:") # Recebe as coordenadas da jogada
            jogada[0] = int(input("x1 = "))
            jogada[1] = int(input("y1 = "))
            print ("Escolha o próximo par")
            jogada[2] = int(input("x2 = "))
            jogada[3] = int(input("y2 = "))
            if jogada[0:2] in descobertos or jogada[2:4] in descobertos:
                print("Voce nao pode selecionar um numero já descoberto")
            elif jogada[0:2] == jogada[2:4]:
                print("voce nao pode escolher as mesmas coordenadas!")
        else:
            print("VOCE ESCOLHEU: {} e {}".format(mapaArray[jogada[0]][jogada[1]], mapaArray[jogada[2]][jogada[3]]))
            print(mesclaMapaArray(mapaArray, maskArray, jogada)) if jogadas==0 else print(mesclaMapaArray(mapaArray, mesclaArray, jogada))
            mesclaArray = efetivaJogada(mapaArray, maskArray, jogada, descobertos)
            print(orgMap(mesclaArray))
        jogada = [-1, -1, -2, -2] # Reinicia valores para a proxima jogada
        ganhou = ganhei(mesclaArray) # Verifica se todos os numeros ja foram descobertos
        jogadas+=1
    else:
            print("PARABENS VOCÊ GANHOU!!!")
            print("Você levou {} jogadas para terminar.".format(jogadas))

            
main() ## Chama função principal, inicia o jogo.
