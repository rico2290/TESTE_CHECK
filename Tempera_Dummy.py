import os,time,random,sys,math,copy
#import itertools as it
import numpy as np

TAMANHOTABULEIRO = 40
TEMPERATURA = 100


# ataque nas colunas
def total_ataque_coluna(l):
	ll = list(zip(*l))
	coluna = [sum(x)-1 for x in ll if sum(x)> 1]
	return sum(coluna)

# ataque nas linhas
def total_ataque_linha(l):
	l = [list(x) for x in (l)]
	linha =[sum(x)-1 for x in l if sum(x)>1]
	return sum(linha)

# --------------------------------
def get_linha(matriz):
	 return [[c for c in r] for r in matriz]

def get_coluna(matriz):
	 return list(zip(*matriz))
#ataque nas diagonais
def diagonal_baixo_para_cima(matriz):
	 b = [None] * (len(matriz) - 1)
	 matriz = [b[i:] + r + b[:i] for i, r in enumerate([list(x) for x in get_coluna(matriz)])]
	 #print('\ndiagonal baixo p/cima',list([[c for c in r if c is not None] for r in get_coluna(matriz)]))
	 return list([[c for c in r if c is not None] for r in zip(*matriz)])

#ataque nas diagonais
def diagonal_cima_para_baixo(matriz):
	 b = [None] * (len(matriz) - 1)
	 matriz = [b[:i] + r + b[i:] for i, r in enumerate(get_linha(matriz))]
	 #print('\ndiagonal cima p/baixo',list([[c for c in r if c is not None] for r in get_coluna(matriz)]))
	 return list([[c for c in r if c is not None] for r in zip(*matriz)])

#Total de todas as ataques
def total_ataques(matriz):
	t_diagonal_cima = [sum(x)- 1 for x in diagonal_cima_para_baixo(matriz) if sum(x) > 1]
	t_diagonal_baixo = [sum(x)- 1 for x in diagonal_baixo_para_cima(matriz) if sum(x) > 1]
	#print('TOTAL ATAQUES', total_ataques(matriz))
	return sum(t_diagonal_baixo)+sum(t_diagonal_cima)+total_ataque_coluna(matriz)+total_ataque_linha(matriz)

# -----------------------------------------------------------------

def random_choice(tamanho=TAMANHOTABULEIRO):
	prob_alta = (tamanho-1)
	prob_baixa = (tamanho-tamanho)+1
	res = randomico = np.random.choice([0, 1],size=(tamanho*tamanho), p=[prob_alta/tamanho, prob_baixa/tamanho])
	ll = np.array_split(res, tamanho)
	l = []
	for x in ll:
		l.append(x.tolist())
	return l

def quantidade_rainhas(atual):
	d = 0
	for x in range(0,len(atual)):
		for y in range(0,len(atual)):
			if atual[x][y] == 1:
					d += 1
	return d

def gerar_rainhas_aleatoria(tamanho=TAMANHOTABULEIRO):
	randomico = random_choice(tamanho)
	d = quantidade_rainhas(randomico)

	if d <= 2:
		while True:
				randomico = random_choice(tamanho)
				d= quantidade_rainhas(randomico)
				if d > 2 :
					break
	
	lista = []
	for x in range(0,tamanho):
			lista.append(randomico[x])

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
			a = random.randint(0,len(atual)-1) #(y + p) % len(atual)
			#print('A = ',a)
			b = random.randint(0,len(atual)-1)
			if atual[b][a] == 0:
					aux = atual[b][a]
					atual[b][a] = atual[x][y]
					atual[x][y] = aux #atual[x][a] # 
					break
	return atual

def tempera_simulada(atual, p=1, T=TEMPERATURA):
 
	achou = False
	passos = 0
	lista = [atual]
	inicio = time.time()
	for temp in range(T, 0,-1):
			passos +=1
			time.sleep(1)
			print('TEMPERATURA ATUAL: ', temp)
			if total_ataques(atual) == 0:
					achou = True
					break
			vizinho = move_rainha_aleatoria(copy.deepcopy(atual), p)
			if vizinho not in lista:
				lista.append(vizinho)
				#print(len(lista))
				deltaE = total_ataques(vizinho) - total_ataques(atual)
				if deltaE <= 0:
					atual = vizinho
					print('\nNova')
					[print(x) for x in atual]
					print('Ataques',total_ataques(atual))
				else:
					novo = random.randint(0,T)
					print('Novo {} - exp {}'.format(novo,math.exp(deltaE/T)))
					if novo < math.exp(deltaE/T):
						atual = vizinho
						print('valor aceite')
						[print(x) for x in atual]
						print('Ataques', total_ataques(atual))
					else:
						#pass
						print('O valor {} nao aceito'.format(novo))
	if achou:
		print('Achou com {} passos'.format(passos))
	else:
		print('Nao achou com {}'.format(passos))




inicio = gerar_rainhas_aleatoria(8)

[print(x)  for x in (inicio)]
print('Ataques: ',total_ataques(inicio))
print('Rainhas: ',quantidade_rainhas(inicio))

if total_ataques(inicio) == 0:
	print('O prorpio iniciouleiro eh a solucao')
else:
	t = int(input('digite numero d temperatura: '))
	print()
	tempera_simulada(inicio,T=t)
