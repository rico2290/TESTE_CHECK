from TAB_Dummy import Tabuleiro
import os 
import time


ideal = Tabuleiro(3)
ideal.configuracao_ideal()

tabuleiro_gerado = Tabuleiro(3)
tabuleiro_gerado.preencher_tabuleiro()

tabuleiros_visitados = [tabuleiro_gerado]
tabuleiros_visitados_h = [(0, tabuleiro_gerado.manhatan_distancia_ideal(), tabuleiro_gerado.manhatan_distancia_ideal(), -1)]

tabuleiros_candidatos = []
candidato_h = []

if ideal in tabuleiros_visitados:
    print('Achou a configuração ideal!!!\n')
    os.sys.exit(1)
else:
  opcao = int(input('Digite 1 para comecar!\n'))
  if opcao == 1:
    print("\nInciando a descida na Arvore...\n")
    time.sleep(1)
    for tabuleiro in tabuleiros_visitados:
      #tabuleiros = tabuleiro.gerar_filhos_tabuleiro()
  
      for tab in tabuleiro.gerar_filhos_tabuleiro():
          print(f'Filho: {tab}')
          if tab not in tabuleiros_visitados:
              if tab not in tabuleiros_candidatos:
                  tabuleiros_candidatos.append(tab)
                  h = tab.manhatan_distancia_ideal()
                  print(f'dist manh = {h}')
                  indice_ant = tabuleiros_visitados.index(tabuleiro)
                  print(f'indice do tabuleiro {indice_ant}')
                  m = tabuleiros_visitados_h[indice_ant][0]
                  print(f'valor do tabuleiro pos[0] = {m}')
                  candidato_h.append((m+1, h, h+m+1, indice_ant))
              else:
                  h = tab.manhatan_distancia_ideal()
                  indice_ant = tabuleiros_visitados.index(tabuleiro)
                  m = tabuleiros_visitados_h[indice_ant][0]
                  indice = tabuleiros_candidatos.index(tab)
                  if ((h+m+1) < candidato_h[indice][2]):
                      candidato_h[indice] = (m+1, h, h+m+1, indice_ant)
          time.sleep(1)
      d_min = 1000
      p_min = 0
      for x in range(0, len(tabuleiros_candidatos)):
          if candidato_h[x][2] < d_min:
              d_min = candidato_h[x][2]
              p_min = x
      tabuleiros_visitados.append(tabuleiros_candidatos[p_min])
      tabuleiros_visitados_h.append(candidato_h[p_min])
      del(tabuleiros_candidatos[p_min])
      del(candidato_h[p_min])
      if ideal in tabuleiros_visitados:
          print('Achou a configuracao ideal\n')
          time.sleep(1)
          break
  ''' Percorrer a lista pra achar índice correspondente a cada tabuleiro'''

  indice = tabuleiros_visitados.index(ideal)

  c = [0]

  while indice not in c:
      x = indice
      y = 0
      while x not in c:
          y = x
          x = tabuleiros_visitados_h[x][3]
      c.append(y)
  print("tabuleiro ")
  # [print(x) for x in tabuleiro.tabuleiro]
  for x in c:
      os.system("cls || clear")
      print('*****************')
      [print(x) for x in tabuleiros_visitados[x].tabuleiro]
      time.sleep(1)

  #print(len(c) - 1)
