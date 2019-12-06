from TAB_Dummy import Tabuleiro
import os 
import time


ideal = Tabuleiro(3)
ideal.configuracao_ideal()


tabuleiro = Tabuleiro(3)
tabuleiro.preencher_tabuleiro()


tabuleiros_visitados = []

tabuleiros_visitados.append(tabuleiro)

#[print(x, 'ta na lista') for x in tabuleiros_visitados if tabuleiro in tabuleiros_visitados ]
lista_indices = [-1]

achou = False
if ideal in tabuleiros_visitados:
  print('Tabuleiro gerado tem a configuracao ideal')

else:
  opcao = int(input('Digite 1 para comecar!\n'))
  if opcao == 1:
    time.sleep(1)
    print("\nInciando a descida na Arvore...\n")
    
    for tabuleiro in tabuleiros_visitados:
        #tabuleiros =  gerar_filhos_tabuleiro
        # print(f'tamanho dos filhos gerados: {len(tabuleiros)}')    
        for tab in tabuleiro.gerar_filhos_tabuleiro():
            #print(type(tab), tab)
            if tab not in tabuleiros_visitados:
                #print(f'Filho: {tab}')
                tabuleiros_visitados.append(tab)
                lista_indices.append(tabuleiros_visitados.index(tabuleiro))
                print('Filho {} '.format(tab))
                time.sleep(1)
            else:
              print(f'{tab} ja ta na lista')
        if ideal in tabuleiros_visitados:
            print('\nAchou o Tabuleiro ideal!!!')
            achou = True
            break
        
    print('lista de indices=>',lista_indices)
    time.sleep(1)

    indice = tabuleiros_visitados.index(ideal)
    #print('indice do ideal', indice)

    c = [0]

    while indice not in c:
        x = indice
        y = 0
        while x not in c:
            y = x
            x = lista_indices[x]
        c.append(y)
    print("Tabuleiro")
    #print(tabuleiro)  
    for x in c:
        #os.system("cls || clear")
        print("   || ")
        print("   \/")
        [print(x) for x in tabuleiros_visitados[x].tabuleiro]
        time.sleep(1)
  else:
    print('Opcao invalida!!!')
    os.sys.exit(1)
 