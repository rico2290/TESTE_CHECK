import time
from copy import deepcopy
from random import sample





# Classe do Tabuleiro
class Tab:
	def __init__(self, data, pai=None, nivel=0):
		self.data = data
		self.pai = pai
		self.filhos = list()
		self.nivel = nivel # g(x)
		self.heuristica = self.peca_fora_lugar() # h(x)
		self.f_x = self.nivel + self.heuristica # f(x) = g(x) + h(x)
	
	def gera_filhos(self):
		# Se os filhos já tiverem sido gerados
		if self.filhos:
			return self.filhos

		x, y = self.posicao_do_zero(self.data, 0)

		# Mover para cima
		if (x != 2):
			
			novo_filho = deepcopy(self.data)
			aux = novo_filho[x+1][y]
			novo_filho[x+1][y] = 0
			novo_filho[x][y] = aux
			
			# Verifica se o pai eh nao nulo
			if self.pai is not None:
				# Verifica se o noh gerado nao eh igual o noh pai para evitar loops
				if novo_filho != self.pai.data:
					# Cria noh filho, com referência ao noh pai
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)
			else:
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)
		
		# Mover para baixo
		if (x != 0):
			
			novo_filho = deepcopy(self.data)
			aux = novo_filho[x-1][y]
			novo_filho[x-1][y] = 0
			novo_filho[x][y] = aux
			
			# Verifica se o pai eh nao nulo
			if self.pai is not None:
				# Verifica se o noh gerado nao eh igual o noh pai para evitar loops
				if novo_filho != self.pai.data:
					# Cria noh filho, com referência ao noh pai
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)
			else:
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)

		# Mover para esquerda
		if (y != 2):
			
			novo_filho = deepcopy(self.data)
			aux = novo_filho[x][y+1]
			novo_filho[x][y+1] = 0
			novo_filho[x][y] = aux
			
			# Verifica se o pai eh nao nulo
			if self.pai is not None:
				# Verifica se o noh gerado nao eh igual o noh pai para evitar loops
				if novo_filho != self.pai.data:
					# Cria noh filho, com referência ao noh pai
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)
			else:
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)

		# Mover para direita
		if (y != 0):
			
			novo_filho = deepcopy(self.data)
			aux = novo_filho[x][y-1]
			novo_filho[x][y-1] = 0
			novo_filho[x][y] = aux
			
			# Verifica se o pai eh nao nulo
			if self.pai is not None:
				# Verifica se o noh gerado nao eh igual o noh pai para evitar loops
				if novo_filho != self.pai.data:
					# Cria noh filho, com referência ao noh pai
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)
			else:
					novo = Tab(novo_filho, Tab(self.data, self.pai, self.nivel), self.nivel+1)
					self.filhos.append(novo)

		return self.filhos

	# Número de peças fora do canto
	def peca_fora_lugar(self):
		global ideal
		d = 0
		
		for i in range(0,len(ideal)):
			for j in range(0,len(ideal)):
				if self.data[i][j] != ideal[i][j]:
					d += 1
		return d

	# Distância das peças até o local do objetivo (Distância Manhattan)
	def calculate_heuristics2(self):
		global ideal
		value = 0

		# Calcular valor para cada número menos para o zero
		for i in range(1,9):
			x_goal,y_goal = self.posicao_do_zero(ideal, i)
			x_data,y_data = self.posicao_do_zero(self.data, i)
			value += abs(x_goal-x_data) + abs(y_goal-y_data)
		
		return value

	def posicao_do_zero(self, data, zero=0):
		for i in range(0,len(data)):
			for j in range(0,len(data)):
				if data[i][j] == zero:
					return i,j

	def imprime_tabuleiro(self):
		[print(x) for x in self.data]
		print('\n')
			

def verifica_solucao(raiz):
	inversions = 0
	aux = list()

	# Transformando matriz em uma lista
	for i in range(0,len(raiz)):
		for j in range(0,len(raiz)):
			aux.append(raiz[i][j])

	# Calculando o numero de inversoes
	for i in range(0,(len(raiz)*len(raiz)-1)):
		for j in range(i+1,(len(raiz)*len(raiz))):
			if (aux[j] > 0 and aux[i] > 0 and aux[i] > aux[j]):
				inversions += 1

	return (inversions%2 == 0)

# BFS
def bfs_Dummy(tab):
	global ideal
	inicio = time.time()

	# Verifica se a configuração tem solução
	if not verifica_solucao(tab):
		print('A configuração nao tem solução')
		return 1
	
	
	raiz = Tab(tab)
	achou = False
	lista_pai = list()
	lista_filho = list()

	print('Estado inicial:')
	raiz.imprime_tabuleiro()

	# Verifica se a configuração inicial é a solução
	if raiz.data == ideal:
	   
		print('Achou a Solução em {} segundos'.format(time.time()-inicio))
		raiz.imprime_tabuleiro()
	   
		return raiz
	
	# Gerando nós filhos do nivel 1
	lista_pai += raiz.gera_filhos()

	# Verificando nós filhos
	for filho in lista_pai:
		# Verifica se tem solução no nivel 1
		if filho.data == ideal:
		   
			print('Achou a Solução em {} segundos'.format(time.time()-inicio))
			filho.imprime_tabuleiro()
		   
			return filho

	# Gera filhos enquanto nao achar
	while not achou:
		#mais um nivel 
		for filho in lista_pai:
			lista_filho += filho.gera_filhos()

		for filho in lista_filho:
			# Verificando nó
			if filho.data == ideal:
			   
				print('Achou a solução em {} segundos'.format(time.time()-inicio))
				filho.imprime_tabuleiro()

			   
				return filho
		
		# Otimização
		lista_pai.clear()
		lista_pai = deepcopy(lista_filho)
		lista_filho.clear()
		
# A* 
def a_estrela(tab):
	global ideal
	inicio = time.time()

	if not verifica_solucao(tab):
		print('A configuração nao tem  solução')
		
		return 1
	
	raiz = Tab(tab)
	lista_pai = list()
	achou = False	
	
   
	print('Estado Inicial:')
	raiz.imprime_tabuleiro()
	
	# Verifica se a raiz é a propria solução
	if raiz.data == ideal:
	   
		print('Achou a solução em {} segundos'.format(time.time()-inicio))
		raiz.imprime_tabuleiro()
	   
		return raiz
	
	# Gerando nós filhos do primeiro nvel
	lista_pai += raiz.gera_filhos()

	# Verifica se tem solução no nivel 1
	for filho in lista_pai:
		if filho.data == ideal:
		   
			print('Achou a Solução em {} segundos'.format(time.time()-inicio))
			filho.imprime_tabuleiro()
		   
			return filho	

	# Desce enquanto nao achar
	while not achou:
		menor = lista_pai[0].f_x
		menor_indice = 0

		# Identificar menor f_x, e qual atingiu o objetivo
		for i in range(len(lista_pai)):
			if lista_pai[i].data == ideal:
				print('Achou a solução em {} segundos'.format(time.time()-inicio))
				lista_pai[i].imprime_tabuleiro()
				
				return lista_pai[i]

			if lista_pai[i].f_x < menor:
				menor = lista_pai[i].f_x
				menor_indice = i
		
		# Tabuleiro com menor f_x
		menor_tab = lista_pai.pop(menor_indice)
		lista_pai += menor_tab.gera_filhos()


def caminho_solucao(partida):
	print('Caminho da solução:')
	
	lista_tab = list()

	#subindo ate a raiz
	while partida.pai != None:
		lista_tab.append(partida)
		partida = partida.pai

	lista_tab.append(partida)

	#invertendo pra imprimir na ordem de pai a filho
	lista_tab.reverse()

	for elemento in lista_tab:
		#print('Passo {}'.format(i))
		elemento.imprime_tabuleiro()


#___________________MAIN______________________________

ideal = [[1,2,3],[4,5,6],[7,8,0]]

enunciado = [[2,0,4],[3,1,6],[7,5,8]]

temp = (sample(range(0,len(ideal)*len(ideal)),len(ideal)*len(ideal)))
aleatorio = []
aleatorio.append(temp[slice(3)])
aleatorio.append(temp[slice(3,6,1)])
aleatorio.append(temp[slice(6,9,1)]) 
print('Tabuleiro aleatorio')
[print(x) for x in aleatorio]
print('==================================\n')

	

inicio = bfs_Dummy(aleatorio)
#inicio = a_estrela(enunciado)
caminho_solucao(inicio)
