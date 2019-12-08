import numpy as np
from random import randint
from random import sample
import copy

class Tabuleiro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabuleiro = []
        self.zero_position = [0]*2
    
    def preencher_tabuleiro(self):
        #while(True):
        #l = (sample(range(0,self.tamanho*self.tamanho),self.tamanho*self.tamanho))
        # count = 0
        # for x in range(0, len(l)-1):
        #     for y in range(x+1, len(l)):
        #         if(l[x]>l[y] and l[y]>0):
        #             count+=1
        # if(count % 2 == 0):
        #     break

        #self.tabuleiro.append([0,1,2])
        #self.tabuleiro.append([4,5,3])
        #self.tabuleiro.append([7,8,6])

        self.tabuleiro.append([2,0,4])
        self.tabuleiro.append([3,1,6])
        self.tabuleiro.append([7,5,8])        

        # self.tabuleiro.append(l[slice(3)])
        # self.tabuleiro.append(l[slice(3,6,1)])
        # self.tabuleiro.append(l[slice(6,9,1)])  
        print('Tabuleiro Gerado')
        [print(x) for x in self.tabuleiro]
        self.zero_position[0], self.zero_position[1] = self.posicao_zero()
        print('\n')  

    def verifica_solucao(self):
        num_inversoes = 0
        for x in range(0,len(self.tabuleiro)-1):
            for y in range(x+1,len(self.tabuleiro)):
                if self.tabuleiro[y] > self.tabuleiro[x]:
                    num_inversoes +=1
        if num_inversoes%2 == 1:
            print('Nao resolvivel')
            return False
        else:
            print('Resolvível')
            return True

    def configuracao_ideal(self):
        self.tabuleiro.append([1,2,3])
        self.tabuleiro.append([4,5,6])
        self.tabuleiro.append([7,8,0])
        print('Tabuleiro Ideal')
        [print(x) for x in self.tabuleiro]
        print('\n')

    def posicao_zero(self):
        for  x in range(0, len(self.tabuleiro)):
            for  y in range(0, len(self.tabuleiro)):
                if self.tabuleiro[x][y] == 0:
                    return x,y


    def __str__(self):
        return str(self.tabuleiro)

    def __eq__(self, obj):
        if self.tamanho != obj.tamanho:
            return False
        for x in range(0, self.tamanho):
            for y in range(0, self.tamanho):
                if self.tabuleiro[x][y] != obj.tabuleiro[x][y]:
                    return False
        return True


    def gerar_filhos_tabuleiro(self):
        ''' Gerar filhos movendo em quatro possiveis direçoes {cima, baixo, esq, dir} '''
        #print('Gerando filhos\n')
        x,y = self.posicao_zero()
        mover = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        filhos_gerados = []
        for i in mover:
            filho = self.movimentar(self.tabuleiro,x,y,i[0],i[1])
            if len(filho) > 1:
                filho_No = Tabuleiro(self.tamanho)
                [filho_No.tabuleiro.append(x) for x in filho]
                filho_No.zero_position[0], filho_No.zero_position[1] = self.posicao_zero()
                filhos_gerados.append(filho_No)
                #print(filho_No.tabuleiro)
        return filhos_gerados
                

    def movimentar(self,tabuleiro,x1,y1,x2,y2):
        ''' Mover zero para a posição dada. Caso a posição seja >= 3, retorna vazio '''
        if x2 >= 0 and x2 < self.tamanho and y2 >= 0 and y2 < self.tamanho:
            #lista_temp = []
            lista_temp = copy.deepcopy(self.tabuleiro)
            temp = lista_temp[x2][y2]
            lista_temp[x2][y2] = lista_temp[x1][y1]
            lista_temp[x1][y1] = temp
            return lista_temp
        else:
            return []


    def manhatan_distancia_ideal(self):
        d = 0
        for x in range(0, self.tamanho):
            for y in range(0, self.tamanho):
                if self.tabuleiro[x][y] != 0:
                    aux = self.tabuleiro[x][y] - 1
                    p_alvo = [aux // self.tamanho , aux % self.tamanho]
                    d += (abs(p_alvo[0] - x) + abs(p_alvo[1] - y))
        return d


# tab = Tabuleiro(3)
# tab.preencher_tabuleiro()
# tab.verifica_solucao()