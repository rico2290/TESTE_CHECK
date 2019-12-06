
atual = [[1,0,1],[0,1,1],[1,1,1]]
[print(x, end='\n') for x in atual]

def total_ataques(atual):
	total_ataques = 0
	d = 0
	total = 0
	while d <= len(atual)-1:
			cont = 0
			i = d
			j = 0
			while j <= d:
					if atual[j][i] == 1:
							cont +=1
					i = i-1
					j =j+1
			if cont > 1:
					cont -=1
					total = total+cont
			else:
					total = total+cont
			d +=1
							
	total_ataques += total

	for x in range(len(atual)-2,-1,-1):
			aux_quant_ataques = 0
			j = 0
			for i in range(x,len(atual)):
					if atual[i][j] == 1:
							aux_quant_ataques += atual[i][j]
					j+=1

			aux_quant_ataques -= 1
			total_ataques += aux_quant_ataques



	for x in range(1,len(atual)-1):          
			i = 0
			aux_quant_ataques = 0

			for j in range(x,len(atual)):        
					aux_quant_ataques += atual[i][j]
					i+=1
			
			aux_quant_ataques -= 1
			total_ataques += aux_quant_ataques

	ataque_colunas = 0
	for x in range(len(atual)):
			n_linhas = 0
			for y in range(len(atual)):
					n_linhas += atual[y][x]
					if n_linhas > 1:
							ataque_colunas += n_linhas-1
	total_ataques +=ataque_colunas

	ataque = 0
	ataque_linhas = 0
	# ataque nas linhas
	for x in (atual):
			if sum(x) > 1:
					ataque_linhas += sum(x)-1
	total_ataques += ataque_linhas

		
	#quant_ataques = quant_ataques+
	
	return total_ataques

print(total_ataques(atual))
