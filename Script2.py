from Game import *
from Neuron import *
from Player import *

jeu = Game(15)
player1 = CPUPlayer("La Machine 1","hard",15)
player2 = CPUPlayer("La Machine 2","hard",15)

NB_PARTIES = 50000

for i in range(1,NB_PARTIES):
	jeu.start(player1,player2,False)

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")