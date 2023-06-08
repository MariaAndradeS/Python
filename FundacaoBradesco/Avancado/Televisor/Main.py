from Funcionalidades import *

tv = Televisor('Samsumg','SAMSUMG-123')
controle = ControleRemoto(tv)

controle.sintonizaCanal('Globo')
controle.trocaCanal('Globo')

print(tv.canal_Atual)