### Desenvolvedore(s):
###                 NOME      -    DRE
###     Hugo Miranda e Souza  - 118043403
### Professora: Lenka Ptackova
### Disciplina: [MAB241] Computação II
### Data:   07/09/2019


## Classe (objeto) Pilha
class Pilha:
    ## Metodo construtor da classe
    def __init__(self, elementos = []):
        if type(elementos) == list:
            self.elementos = elementos
            print ('Sucesso')
        else:
            self.elementos = []
            print ('Formato inadequado')

    ## Metodo para adicionar elementos na Pilha
    def empilhar(self, numero):
        self.numero = numero
        self.elementos.append(self.numero)

    ## Metodo para remover um elemento da Pilha
    def desempilhar(self):
        while len(self.elementos) > 0:
            return self.elementos.pop(-1)
        else:
            return 'Pilha vazia'

    ## Função que retorna os elementos contidos na Pilha
    def getPilha(self):
        return self.elementos

    ## Função que retorna a quantidade de elementos que a Pilha possui
    def lenPilha(self):
        return len(self.elementos)

    ## Metodo que redefine o operador de soma (+) que concatena (agrupa)
    ## duas Pilhas (p1, p2) e a retorna em uma nova Pilha (p3)
    def __add__(self, other):
        p1 = self.getPilha()
        p2 = other.getPilha()
        if type(p1) and type(p2) == list:
            print(type(p1) == list and type(p2) == list)
            p3 = Pilha(p1 + p2)
            return p3
        else:
            return 'erro'

