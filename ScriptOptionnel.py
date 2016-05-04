from Game import *
from Neuron import *
from Player import *

jeu = Game(15)
player1 = CPUPlayer("La Machine 1","hard",15)
player2 = CPUPlayer("La Machine 2","hard",15)

NB_PARTIES = 5000

for i in range(1,NB_PARTIES+1):
	jeu.start(player1,player2,False)
	print("Partie " + str(i) + " : T_Erreur(Machine1) = " + str(player1.getTauxErreur()) + "%  /  T_Erreur(Machine2) = " + str(player2.getTauxErreur()) + "%")
	player1.resetTauxErreur()
	player2.resetTauxErreur()

print(str(player1.getName()) + " : " + str(player1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(player2.getName()) + " : " + str(player2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")