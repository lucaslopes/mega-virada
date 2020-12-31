import random
from tqdm import tqdm

def gera_jogo():
  jogo = []
  while len(jogo) < 6: # aposta simples, com apenas seis dezenas
    if (sorteado := random.choice(range(1,61))) not in jogo:
      jogo.append(sorteado)
  jogo.sort()
  return jogo
 
def cria_N_jogos(N):
  n_jogos = open(f'{N}_jogos.txt', 'w')
  for _ in tqdm(range(N)):
    jogo = gera_jogo()
    n_jogos.write(str(jogo)[1:-1].replace(', ', ',')+'\n') # '\t'
  n_jogos.close()
  
if __name__ == "__main__":
  cria_N_jogos(1_000_000)
