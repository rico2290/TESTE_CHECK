from random import sample
from copy import deepcopy
import time, os


class No:
    def __init__(self,tamanho,nivel,fval):
        ''' Inicializar o No com o tamanho, nivel do No e o fvalor calculado '''
        self.tamanho = tamanho
        self.nivel = nivel
        self.fval = fval
        #print(self.tamanho, type(self.tamanho[0][0]))
    def gerar_filho(self):
        ''' Gerar No filho a partir de um dado No, movendo o zero
            em 4 direções possiveis: {cima,baixo,esq,dir} '''
        x, y = self.posicao_zero(self.tamanho,0)
        #print('posicao do zero:[{}][{}]'.format(x,y))

        posicao_mover = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        ''' posicao_mover contém valores das posições para mover o zero em
            4 direções {cima,baixo,esq,dir} '''        
        #print('posicao a movimentar: ',posicao_mover)
        filhos = []
        for i in posicao_mover:
            filho = self.shuffle(self.tamanho,x,y,i[0],i[1])
            if filho is not None:
                filho_No = No(filho,self.nivel+1,0)
                filhos.append(filho_No)
        return filhos
        
    def shuffle(self,puz,x1,y1,x2,y2):
        ''' Mover zero para a posição dada. Caso a posição seja >= 3, retorna vazio '''
        if x2 >= 0 and x2 < len(self.tamanho) and y2 >= 0 and y2 < len(self.tamanho):
            lista_temp = []
            lista_temp = self.copiar(puz)
            temp = lista_temp[x2][y2]
            lista_temp[x2][y2] = lista_temp[x1][y1]
            lista_temp[x1][y1] = temp
            return lista_temp
        else:
            return None
    def copiar(self,lista):
        ''' Criar filho a partir do No lista'''
        #temp = []
        temp = deepcopy(lista)
        return temp    
            
    def posicao_zero(self,lista,zero=0):
        ''' Achar a posicao_zero  '''
        for i in range(0,len(self.tamanho)):
            for j in range(0,len(self.tamanho)):
                if lista[i][j] == zero:
                    return i,j
class Heuristica:
    def __init__(self,tamanho):
        ''' Inicializar o Heuristica com o tamanho fornecido '''
        self.n = tamanho
        self.visitados = []
        self.aux = []
    def gerar_matriz(self):
        ''' Gerar matriz randomicamente '''
        #lista = [[1,2,3],[0,4,6],[7,5,8]]
        lista = []
        # lista.append([0,1,2])
        # lista.append([4,5,3])
        # lista.append([7,8,6])    

        lista.append([2,0,4])
        lista.append([3,1,6])
        lista.append([7,5,8])        

        
        # ll = (sample(range(0,self.n*self.n),self.n*self.n))
        # lista = []
        # lista.append(ll[slice(3)])
        # lista.append(ll[slice(3,6,1)])
        # lista.append(ll[slice(6,9,1)])
    
        print('Matriz Gerada')
        [print(x) for x in lista] 
        
        return lista

    def configuracao_ideal(self):
        lista =  []
        lista.append([1,2,3])
        lista.append([4,5,6])
        lista.append([7,8,0])
        print("\nMatriz pretendida") 
        [print(x) for x in lista]
        return lista

    def f_x(self,tabuleiro_inicial,ideal):
        ''' Funçao heuristica para calcular  valor de  f(x) = h(x) + g(x) '''
        return self.h_x(tabuleiro_inicial.tamanho,ideal)+tabuleiro_inicial.nivel

    def h_x(self,tabuleiro_inicial,ideal):
        ''' Calcular numero de peças fora de lugar '''
        d = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if tabuleiro_inicial[i][j] != ideal[i][j] and tabuleiro_inicial[i][j] != 0:
                    d += 1
        return d

    def principal(self, passos = 10):
        #import timeit
        start = time.time()
        print(f'tabuleiro_inicial: {start}')
        c = passos
        ''' Função principal'''
        achou = False
    
        ideal = self.configuracao_ideal()

        tabuleiro_inicial = self.gerar_matriz()
               
        tabuleiro_inicial = No(tabuleiro_inicial,0,0)
        tabuleiro_inicial.fval = self.f_x(tabuleiro_inicial,ideal)
        ''' colocar No pai na propria lista'''
        if len(self.visitados) > 0:
            print('\nLista visitados: ',self.visitados[0].tamanho)
        self.visitados.append(tabuleiro_inicial)
        
        
        print("\n")

        print("------Iniciando descida na Árvore! ---------")
        
        while c > 0:
            atual = self.visitados[0]

            print('Nivel : {}'.format(atual.nivel))
            print("   || ")
            print("   \\/")
            time.sleep(1)
            [print(i) for i in self.visitados[0].tamanho]

            ''' Se a diferença dos Nos for  0 então achamos a configuração pretendida'''
            if(self.h_x(self.visitados[0].tamanho,ideal) == 0):
                print(f'\nAchou configuração ideal com {c} passos!!!')
                achou = True
                break
            
            del self.visitados[0]

            for i in atual.gerar_filho():

                ''' atribuir valor para fval (numero de peças fora de posição)'''
                i.fval = self.f_x(i,ideal)
                print(f'elemento da lista => {i.tamanho} ', f'| pecas fora de lugar => {i.fval}')
                self.visitados.append(i)
            self.aux.append(atual)
            
            ''' ordenar lista de forma crescente baseada no valor de fx '''
            self.visitados.sort(key = lambda x:x.fval,reverse=False)
            c -=1
        if not achou:
          pass
          print(f'Nao Achou a solucao com {passos}')
        print('Tempo de execucao {}s'.format((time.time()-start)))
      
        
h = Heuristica(3)
h.principal()
