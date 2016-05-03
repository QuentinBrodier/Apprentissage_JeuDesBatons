from Game import *
from Neuron import *
from Player import *
import pickle

NB_STICKS = 15

jeu = Game(NB_STICKS)

# PLAYER NAME
playerName = input('Enter your name : \n')

# GAME MODE
gameMode = ""
while (gameMode!="easy") and (gameMode!="medium") and (gameMode!="hard"):
	gameMode = input('Choose a game mode (easy,medium,hard) : \n')

# PLAYER INSTANCIATION
player1 = HumanPlayer(playerName)
player2 = CPUPlayer("La Machine",gameMode,NB_STICKS)

if(gameMode == "hard"):
	with open('neuronNetwork', 'rb') as inp: ns = pickle.load(inp)
	player2.setNeuronNetwork(ns)

# START GAME
jeu.start(player2,player1,True)