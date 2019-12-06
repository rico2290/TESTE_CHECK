
l = [[1,0,1],[1,1,1],[1,1,1]]
#[print(x, end='\n') for x in l]

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
			print('diagonal', aux_quant_ataques)
			quant_ataques += aux_quant_ataques

	# ataque_colunas = 0
	# for x in range(len(l)):
	# 		#n_linhas = 0
	# 		ab = 0
	# 		for y in range(len(l)):
	# 				if l[y][x] == 1:
	# 					ab +=1
	# 		if ab > 1:
	# 			ab -=1
	# 			ataque_colunas = ataque_colunas + ab

	# ataque = 0
	# ataque_linhas = 0
	# # ataque nas linhas
	# for x in (l):
	# 		if sum(x) > 1:
	# 				ataque_linhas += sum(x)-1
	# ataque += ataque_linhas	
			
	
	return quant_ataques+total#+ataque+ataque_colunas

def teste_colunas(l):
	
	ataque_colunas = 0
	for x in range(len(l)):
			#n_linhas = 0
			ab = 0
			for y in range(len(l)):
					if l[y][x] == 1:
						ab +=1
			if ab > 1:
				ab -=1
				ataque_colunas = ataque_colunas + ab
				#print('\nab', ab)
	#print('total_colunas',ataque_colunas-1, end=' ')
	#ataque += ataque_colunas
	return ataque_colunas

def teste_linha(ll):
	ataque = 0
	ataque_linhas = 0
	# ataque nas linhas
	for x in (ll):
			if sum(x) > 1:
					ataque_linhas += sum(x)-1
	ataque += ataque_linhas
	return ataque	

l = [[1,1,0],[1,1,1],[1,0,1]]
[print(x, end='\n') for x in l]

print('total_linhas',teste_linha(l))

print('\ntotal_colunas',teste_colunas(l))

print('Total diagonais ',quantidade_ataques(l))