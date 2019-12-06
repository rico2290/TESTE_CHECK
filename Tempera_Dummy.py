import os,time,random,sys,math,copy
#import itertools as it
import numpy as np

TAMANHOTABULEIRO = 3
TEMPERATURA = 100
# --------------------------------

def quantidade_ataques(l):
	d = 0
	total = 0
	while d <= len(l)-1:
			cont = 0
			i = d
			j = 0
			while j <= d:
					if l[j][i] == 1:
							cont +=1
					i = i-1
					j =j+1
			if cont > 1:
					cont -=1
					total = total+cont
			else:
					total = total+cont
			d +=1
							
	quant_ataques = 0

	for x in range(len(l)-2,-1,-1):
			aux_quant_ataques = 0
			j = 0
			for i in range(x,len(l)):
					if l[i][j] == 1:
							aux_quant_ataques += l[i][j]
					j+=1

			aux_quant_ataques -= 1
			quant_ataques += aux_quant_ataques



	for x in range(1,len(l)-1):          
			i = 0
			aux_quant_ataques = 0

			for j in range(x,len(l)):        
					aux_quant_ataques += l[i][j]
					i+=1
			
			aux_quant_ataques -= 1
			quant_ataques += aux_quant_ataques
	
	return quant_ataques+total

# -------------------------


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
	if d >= (tamanho*tamanho)/tamanho+1:
			print('Pode ate nao ter solucao')
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
	print('Tabuleiro Gerado')
	[print(x, end='\n') for x in lista]
	print(f'Rainhas => {d}')
	return lista

	for x in range(0,tamanho):
			lista.append(randomico[x])

	return lista


def localiza_rainhas(atual):
	''' devolver posiçoes de todas as rainhas '''
	lista_rainha = []
	for x in range(len(atual)):
			for y in range(len(atual)):
					if atual[x][y] == 1:
							lista_rainha.append((x, y))
	return lista_rainha

# '''
# def calcula_ataques(atual):
# 	''' Fazer varredura nas linhas, colunas e nas diagonais '''
# 	ataque = 0
# 	ataque_linhas = 0
# 	# ataque nas linhas
# 	for x in (atual):
# 			if sum(x) > 1:
# 					ataque_linhas += sum(x)-1
# 	ataque += ataque_linhas

# 	ataque_colunas = 0
# 	for x in range(len(atual)):
# 			n_linhas = 0
# 			for y in range(len(atual)):
# 					n_linhas += atual[y][x]
# 					if n_linhas > 1:
# 							ataque_colunas += n_linhas-1
# 	ataque += ataque_colunas

# 	prox = localiza_rainhas(atual)
# 	d = 0
# 	for i, coordenada in enumerate(prox):
# 			x, y = coordenada
# 			#print(f'x={x} e y={y}')
# 			# ataque diagonal esquerdo
# 			w, z = x+1, y+1
# 			#print(f'w={w} e z={z}')
# 			while (z > 0 and z < len(atual) and w < len(atual)):
# 					if atual[w][z] == 1:
# 							d += 1
# 							break
# 					z -= 1
# 					w += 1
# 			# ataque diagonal direito
# 			a, b = x+1, y+1
# 			while (a < len(atual) and b < len(atual)):
# 					if atual[a][b] == 1:
# 							d += 1
# 							break
# 					a += 1
# 					b += 1
# 	ataque += d
# 	return ataque
# '''

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
					atual[x][y] = aux
					break
	return atual

def tempera_simulada(atual, p=1, T=TEMPERATURA):

	achou = False
	inicio = time.time()
	for temp in range(T, 1,-1):
			time.sleep(1)
			print('TEMPERATURA atual: ', temp)
			ataque = quantidade_ataques(atual)
			print('Atual: ', atual)
			print('Ataques: ', ataque)
			if ataque == 0:
					achou = True
					#print('Achou a Solucao')
					#return ('solucao', atual,ataque,(time.time()-inicio))
					break
			vizinho = move_rainha_aleatoria(copy.deepcopy(atual), p)
			print('Nova configuracao')
			[print(x, end='\n') for x in vizinho]	
			deltaE = quantidade_ataques(vizinho) - ataque  # exp((F(vizinho) - F(atual)))
			print('Delta => ', deltaE)

			if deltaE > 0:
					atual = vizinho
			# Aceitar a jogada com certa probabilidade
			else:
					#novo = random.randint(0, 100)
					print(f'Valor para teste probabilidade: {deltaE} ')
					print('Probabilidade : ',math.exp(deltaE/T)) # exp((F(vizinho) - F(atual))/T)
					if deltaE < math.exp(deltaE/T):
							atual = vizinho
				
	if achou:
		print('Achou a Solucao')
		print('Ataque =>',ataque)
		[print(x, end='\n') for x in atual]
		print('Tempo de execucao: ',(time.time()-inicio))
	else:
		('Nao achou solução')

#[print(x) for x in random_choice()]

tab = gerar_rainhas_aleatoria()

#[print(x, end='\n') for x in tab]
print('posicao das rainhas:')
[print(x, end=' ') for x in localiza_rainhas(tab)]
print('\n---------------------')
time.sleep(2)
tempera_simulada(tab,T=5)
