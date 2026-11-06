
from televisor import Televisor
from controleRemoto import ControleRemoto


# Criando o televisor
tv = Televisor('SONY','SONY-123')

# Criando o controle remoto e passando a TV para ele
controle = ControleRemoto(tv)


# Sintonizando canais
controle.sintonizarCanal('SBT')
controle.trocaCanal('SBT')
controle.sintonizarCanal('RECORD')
controle.trocaCanal('RECORD')
controle.sintonizarCanal('CNN')
controle.trocaCanal('CNN')

print("Canais disponíveis:", tv.lista_de_canais)


# Trocando de canal
controle.trocaCanal('SBT')


print("Canal atual:", tv.canal_atual)
