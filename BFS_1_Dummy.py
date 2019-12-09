from TAB_Dummy import Tabuleiro
import os
import copy
import time


ideal = Tabuleiro(3)
ideal.configuracao_ideal()

tabuleiro = Tabuleiro(3)
tabuleiro.preencher_tabuleiro()

lista_pai = []
lista_filhos = []


lista_pai.append(tabuleiro.tabuleiro)
tabuleiros_visitados = []
tabuleiros_visitados.append(tabuleiro)



lista_indices = [-1]

passos = 100
cont = passos
achou = False

if ideal.tabuleiro in lista_pai:
  print('Tabuleiro gerado tem a configuracao ideal')

else:
  time.sleep(2)
  print("Inciando descida na Arvore...")
  #print('percorrendo ',passos, 'passos ... ')    
  for tabuleiro in tabuleiros_visitados: 
      for tab in tabuleiro.gerar_filhos_tabuleiro():
          if tab.tabuleiro not in lista_pai:
              lista_pai.append(tab.tabuleiro)
              tabuleiros_visitados.append(tab)
              time.sleep(0.1)
          else:
            pass
      passos -=1
      for x in lista_pai:
        if ideal.tabuleiro == x:
            print('\nAchou o Tabuleiro ideal!!!')
            achou = True
            break
        else:
          continue
      aux = copy.deepcopy(lista_filhos)
      lista_pai.clear()
      lista_filhos.clear()
      lista_pai = copy.deepcopy(aux)
      [print(x) for x in lista_pai]
      if passos == 0:
        break
      
  if achou:
    print('Achou com {} passos'.format(cont))
    time.sleep(1)
    # for filho in tabuleiros_visitados:
    #   if filho.tabuleiro == ideal.tabuleiro:
    #     while filho.pai is not None:
    #       print(filho.pai)
    #       filho.pai = filho.pai.pai

      #print('lista de indices=>',lista_indices)
    # indice = 0
    # for x in tabuleiros_visitados:
    #   if x.tabuleiro == ideal.tabuleiro:
    #     indice = tabuleiros_visitados.index(x)
    # #indice = tabuleiros_visitados.index(ideal)
    # #print('indice do ideal', indice)

    # c = [0]

    # while indice not in c:
    #     x = indice
    #     y = 0
    #     while x not in c:
    #         y = x
    #         x = lista_indices[x]
    #     c.append(y)
    # print(c)
    # print("Tabuleiro")
    # #print(tabuleiro)  
    # for x in c:
    #     #os.system("cls || clear")
    #     print("   || ")
    #     print("   \/")
    #     [print(x) for x in tabuleiros_visitados[x].tabuleiro]
    #     time.sleep(1)    
  else:
    print('Nao chou com {} passos'.format(cont))

  # else:
  #   print('Opcao invalida!!!')
  #   os.sys.exit(1)
 