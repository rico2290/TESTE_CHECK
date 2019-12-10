import numpy as np
from random import randint
from random import sample
from copy import deepcopy

class Tabuleiro:
    def __init__(self, data,pai=None):
        self.data = data
        #self.tabuleiro = []
        self.pai = pai
        self.filhos = list()
        
  

    def verifica_solucao(self):
        num_inversoes = 0
        for x in range(0,len(self.data)-1):
            for y in range(x+1,len(self.data)):
                if self.data[y] > self.data[x]:
                    num_inversoes +=1
        if num_inversoes%2 == 1:
            print('Nao resolvivel')
            return False
        else:
            print('Resolvível')
            return True

    def posicao_do_zero(self, data, zero=0):
        for  x in range(0, len(data)):
            for  y in range(0, len(data)):
                if data[x][y] == zero:
                    return x,y


    def gera_filhos(self):
        ''' Gerar filhos movendo em quatro possiveis direçoes {cima, baixo, esq, dir} '''
        x, y = self.posicao_do_zero(self.data)

        if x!= 0:
            lista_temp = deepcopy(self.data)
            temp = lista_temp[x-1][y]
            lista_temp[x-1][y] = 0
            lista_temp[x][y] = temp   
            if self.pai is not None:
                if lista_temp != self.pai.data:
                    novo = Tabuleiro(lista_temp,pai=Tabuleiro(self.data,self.pai))         
                    self.filhos.append(novo)

        if x!= 2:
            lista_temp = deepcopy(self.data)
            temp = lista_temp[x+1][y]
            lista_temp[x+1][y] = 0
            lista_temp[x][y] = temp   
            if self.pai is not None:
                if lista_temp != self.pai.data:
                    novo = Tabuleiro(lista_temp,pai=Tabuleiro(self.data,self.pai))         
                    self.filhos.append(novo)   

        if y!= 2:
            lista_temp = deepcopy(self.data)
            temp = lista_temp[x][y+1]
            lista_temp[x][y+1] = 0
            lista_temp[x][y] = temp   
            if self.pai is not None:
                if lista_temp != self.pai.data:
                    novo = Tabuleiro(lista_temp,pai=Tabuleiro(self.data,self.pai))         
                    self.filhos.append(novo)

        if y!= 0:
            lista_temp = deepcopy(self.data)
            temp = lista_temp[x][y-1]
            lista_temp[x][y-1] = 0
            lista_temp[x][y] = temp   
            if self.pai is not None:
                if lista_temp != self.pai.data:
                    novo = Tabuleiro(lista_temp,pai=Tabuleiro(self.data,self.pai))         
                    self.filhos.append(novo)  

        return self.filhos                                                       

    def manhatan_distancia_ideal(self):
        d = 0
        for x in range(0, self.data):
            for y in range(0, self.data):
                if self.data[x][y] != 0:
                    aux = self.data[x][y] - 1
                    p_alvo = [aux // self.data , aux % self.data]
                    d += (abs(p_alvo[0] - x) + abs(p_alvo[1] - y))
        return d
import time



def BFS_Dummy(inicial):
    global ideal

    passos = 10
    gerado = Tabuleiro(inicial)
    print('Raiz')
    [print(x) for x in gerado.data]
   
    achou = False
    lista_pai = list()
    lista_filhos = list()

    if gerado.data == ideal:
        print('Tabuleiro gerado eh a propria solucao')
        return gerado
    #Caso nao, coloca os filhos a gerar na lista de pai
    lista_pai += gerado.gera_filhos()

    # verique cada filho gerado se eh o tabuleiro q vc quer
    for filho in lista_pai:
        if  filho.data == ideal:
            [print(x) for x in filho.data]
            return filho

    while passos > 0:
        # gera filhos  enquanto nao achar a solução
        while not achou:
            print('entrando')
            #gera filhos a apartir da lista pai
            for filho in lista_pai:
                #if filho not in lista_filhos:
                lista_filhos += filho.gera_filhos()
            
            # verfique se algum filho gerado eh a solucao antes q precisar gerar mais
            for filho in lista_filhos: 
                time.sleep(1)
                print(filho.data, '?', ideal)
                if filho.data == ideal:
                    print('Achou a solucao')
                    [print(x) for x in filho.data]
                    achou = True
                    return filho
            passos -=1
            # print(passos)

            # Fase de otimização
            lista_pai.clear()
            lista_pai = deepcopy(lista_filhos)
            lista_filhos.clear()

        if  passos == 0:
            break            

def imprimir_percurso(partida):
    print('Caminho inverso')
    lista_caminho = list()

    #subindo na arvore
    while partida.pai != None:
        lista_caminho.append(partida)
        partida = partida.pai
    
    lista_caminho.append(partida)
    #inverter para imprimir a partir da raiz
    lista_caminho.reverse()

    #imprimindo a lista ja pronta
    for elemento in lista_caminho:
        [print(x) for x in elemento.data]

ideal = [[1,2,3],[4,5,6],[7,8,0]]

temp = (sample(range(0,3*3),3*3))
aleatorio = []
aleatorio.append(temp[slice(3)])
aleatorio.append(temp[slice(3,6,1)])
aleatorio.append(temp[slice(6,9,1)]) 
print(aleatorio)

s = BFS_Dummy(aleatorio)
imprimir_percurso(s)



