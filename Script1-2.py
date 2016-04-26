from Game import *
from Neuron import *
from Player import *

jeu = Game(15)
player1 = HumanPlayer("Jean Neige")
player2 = CPUPlayer("La Machine","medium",15)

jeu.start(player1,player2,True)
