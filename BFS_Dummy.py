from TAB_Dummy import Tabuleiro
import os 
import time


ideal = Tabuleiro(3)
ideal.configuracao_ideal()


tabuleiro = Tabuleiro(3)
tabuleiro.preencher_tabuleiro()


tabuleiros_visitados = []
visitas = []
tabuleiros_visitados.append(tabuleiro)
visitas.append(tabuleiro.tabuleiro)


#[print(x, 'ta na lista') for x in tabuleiros_visitados if tabuleiro in tabuleiros_visitados ]
lista_indices = [-1]

passos = 1000
cont = passos
achou = False
if ideal in tabuleiros_visitados:
  print('Tabuleiro gerado tem a configuracao ideal')

else:
  time.sleep(2)
  print("Inciando descida na Arvore...")
  print('percorrendo ',passos, 'passos ... ')    
  for tabuleiro in tabuleiros_visitados:
      #print('Filhos gerados')    
      for tab in tabuleiro.gerar_filhos_tabuleiro():
          #print(type(tab), tab)
          if tab not in tabuleiros_visitados:
              tabuleiros_visitados.append(tab)
              visitas.append(tab.tabuleiro)
              lista_indices.append(tabuleiros_visitados.index(tabuleiro))
              #[print(x) for x in tab.tabuleiro]
              #print()
              time.sleep(0.1)
          else:
            pass
      passos -=1
      
      if ideal.tabuleiro in visitas:
          print('\nAchou o Tabuleiro ideal!!!')
          achou = True
          break
      
      #print(passos,'pasos',end=' ')
      if passos == 0:
        break
      
  if achou:
    print('Achou com {} passos'.format(cont))
    time.sleep(1)
      #print('lista de indices=>',lista_indices)
    indice = 0
    for x in tabuleiros_visitados:
      if x.tabuleiro == ideal.tabuleiro:
        indice = tabuleiros_visitados.index(x)
    #indice = tabuleiros_visitados.index(ideal)
    #print('indice do ideal', indice)

    c = [0]

    while indice not in c:
        x = indice
        y = 0
        while x not in c:
            y = x
            x = lista_indices[x]
        c.append(y)
    print(c)
    print("Tabuleiro")
    #print(tabuleiro)  
    for x in c:
        #os.system("cls || clear")
        print("   || ")
        print("   \/")
        [print(x) for x in tabuleiros_visitados[x].tabuleiro]
        time.sleep(1)    
  else:
    print('Nao chou com {} passos'.format(cont))

  # else:
  #   print('Opcao invalida!!!')
  #   os.sys.exit(1)
 