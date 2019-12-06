
'''
    otimização por colonia de formiga aplicado ao problema de caixeiro viajante
'''

import random, math

# Classe que representa uma formiga
class formiga:
    def __init__(self, cidade):
        self.cidade = cidade
        self.solucao = []
        self.custo = None
        #super().__init__()

    @property
    def cidade(self):
        return self.cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.cidade = cidade

    @property
    def solucao(self):
        return self.solucao
    
    @solucao.setter 
    def solucao(self, solucao, custo):
        if not self.custo:
            elf.solucao = solucao[:]
            self.custo = custo
        else:
            if custo < self.custo:
                self.custo = custo
    @property
    def custo(self):
        return self.custo

# classe que representa uma aresta
class Aresta:
    def __init__(self, origem, destino, custo):
        #super().__init__()
        self.origem, self.destino, self.custo, self.feromonio = origem,destino,custo,None
    
    @property
    def origem(self):
        return self.origem

    @property
    def destino(self):
        return self.destino  

    @property
    def custo(self):
        return self.custo

    @property
    def feromonio(self):
        return self.feromonio 

    @feromonio.setter
    def feromonio(self, feromonio):
        self.feromonio = feromonio

# classe qu representa um grafo        
    


    


    
        