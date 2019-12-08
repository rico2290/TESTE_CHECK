import os,time,random,sys,math,copy
#import itertools as it
import numpy as np

TAMANHOTABULEIRO = 4
TEMPERATURA = 100


m = [[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,1,1,0]]
# [print(x) for x in m]
# print()

# ataque nas colunas
def total_colunas(l):
	ll = list(zip(*l))
	ab = [sum(x)-1 for x in ll if sum(x)> 1]
	#print(ll)
	return sum(ab)

# ataque nas linhas
def total_linhas(l):
	ataque_linhas = 0
	for x in (l):
		if sum(x) > 1:
			ataque_linhas += sum(x)-1
	return ataque_linhas

# --------------------------------
def get_linha(matriz):
	 #print([[c for c in r] for r in matriz])
	 return [[c for c in r] for r in matriz]

def get_coluna(matriz):
	 #print('SAIDA',list(zip(*matriz)))
	 return list(zip(*matriz))

def get_diagonal_baixo_cima(matriz):
	 b = [None] * (len(matriz) - 1)
	 matriz = [b[i:] + r + b[:i] for i, r in enumerate([list(x) for x in get_coluna(matriz)])]
	 #print('\ndiagonal baixo p/cima',list([[c for c in r if c is not None] for r in get_coluna(matriz)]))
	 return list([[c for c in r if c is not None] for r in zip(*matriz)])

def get_diagonal_cima_baixo(matriz):
	 b = [None] * (len(matriz) - 1)
	 matriz = [b[:i] + r + b[i:] for i, r in enumerate(get_linha(matriz))]
	 #print('\ndiagonal cima p/baixo',list([[c for c in r if c is not None] for r in get_coluna(matriz)]))
	 return list([[c for c in r if c is not None] for r in zip(*matriz)])



def total_ataques(matriz):
	t_diagonal_cima = [sum(x)- 1 for x in get_diagonal_cima_baixo(matriz) if sum(x) > 1]
	t_diagonal_baixo = [sum(x)- 1 for x in get_diagonal_baixo_cima(matriz) if sum(x) > 1]
	#print('TOTAL ATAQUES', total_ataques(matriz))
	return sum(t_diagonal_baixo)+sum(t_diagonal_cima)+total_colunas(matriz)+total_linhas(matriz)
#print('TOTAL ATAQUES', total_ataques(matriz))
# -----------------------------------------------------------------

def random_choice(tamanho=TAMANHOTABULEIRO):
	prob_alta = (tamanho-1)
	prob_baixa = (tamanho-tamanho)+1
	res = randomico = np.random.choice([0, 1], size=(
			tamanho*tamanho), p=[prob_alta/tamanho, prob_baixa/tamanho])
	ll = np.array_split(res, tamanho)
	l = []
	for x in ll:
		l.append(x.tolist())
	return l

def quantidade_rainhas(atual):
	d = 0
	for x in range(0,len(atual)):
		#print(quant_ataques)
		for y in range(0,len(atual)):
			if atual[x][y] == 1:
					d += 1
	return d

def gerar_rainhas_aleatoria(tamanho=TAMANHOTABULEIRO):
	randomico = random_choice()
	d = quantidade_rainhas(randomico)

	if d <= 2:
		while True:
				randomico = random_choice()
				d= quantidade_rainhas(randomico)
				if d > 2 :
					break
	
	lista = []
	for x in range(0,tamanho):
			lista.append(randomico[x])
	#print(randomico)
	# print('Tabuleiro Gerado')
	# [print(x, end='\n') for x in lista]
	# print(f'Rainhas => {d}')
	if d >= (tamanho*tamanho)/tamanho+1:
			print('Aviso! Pode nao ter solucao ou demorar para achar')	
	return lista



def localiza_rainhas(atual):
	''' devolver posiçoes de todas as rainhas '''
	lista_rainha = []
	for x in range(len(atual)):
			for y in range(len(atual)):
					if atual[x][y] == 1:
							lista_rainha.append((x, y))
	return lista_rainha


def move_rainha_aleatoria(atual, p):
	''' mover uma rainha por meio de uma escolha randomica '''
	#tamanho = len(atual)
	while True:
			x, y = random.choice(localiza_rainhas(atual))
			#print(f'escolhidos x={x} e y={y}')
			a = (y + p) % len(atual)
			#print('A = ',a)
			if atual[x][a] == 0:
					aux = atual[x][a]
					atual[x][a] = atual[x][y]
					atual[x][y] = aux #atual[x][a] # 
					break
	return atual

def tempera_simulada(atual, p=1, T=TEMPERATURA):
	[print(x) for x in atual],print('N} rainhas: ', quantidade_rainhas(atual)),print('Ataques: ', total_ataques(atual))
	print('Posicao Rainhas: ',localiza_rainhas(atual))
	print()
	achou = False
	inicio = time.time()
	for temp in range(T, 0,-1):
			time.sleep(1)
			print('TEMPERATURA atual: ', temp)
			ataque = total_ataques(atual)
			# print('Posicao Rainhas: ',localiza_rainhas(atual))
			if ataque == 0:
					achou = True
					break
			vizinho = move_rainha_aleatoria(copy.deepcopy(atual), p)
			# print('Nova configuracao')
			# [print(x, end='\n') for x in vizinho]	
			deltaE = ataque  - total_ataques(vizinho)   # exp((F(vizinho) - F(atual)))
			print('Atual - sucessor  = ', deltaE)

			if deltaE >= 0:
					atual = vizinho
					print('Configuracao Atual'),[print(x) for x in  atual], print('Ataques: ', ataque)
					print('Posicao Rainhas: ',localiza_rainhas(atual))

			# Aceitar a jogada com certa probabilidade
			else:
					novo = random.randint(0, 100)
					#print(f'Valor para teste : {novo} ')
					print('Probabilidade : ',math.exp(deltaE/T)) # exp((F(vizinho) - F(atual))/T)
					if novo < math.exp(deltaE/T):
							atual = vizinho
							print('Configuracao Atual'),[print(x) for x in  atual], print('Ataques: ', ataque)
			print()
				
	if achou:
		print('Achou a Solucao')
		print('Ataque =>',ataque)
		[print(x, end='\n') for x in atual]
		print('Tempo de execucao: (^^)',(time.time()-inicio))
	else:
		[print(x, end='\n') for x in atual]
		print('Nao achou solucao\nTempo de execuccao: ',(time.time()-inicio))



tab = gerar_rainhas_aleatoria()

[print(x)  for x in (tab)]

if total_ataques(tab) == 0:
	print('O prorpio tabuleiro eh a solucao')
else:
	t = int(input('digite numero d temperatura: '))
	tempera_simulada(tab,T=t)
