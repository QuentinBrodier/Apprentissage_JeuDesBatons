import random
from Neuron import *

class Player:
    def __init__(self,name):
        self.name = name
        self.nbWin = 0
    def getName(self):
        return self.name
    def getNbWin(self):
        return self.nbWin
    def addWin(self):
        self.nbWin+=1
    def addLoss(self):
        pass

class HumanPlayer(Player):
    def play(self,sticks):
        if sticks==1: return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb=int(nb)
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True
                        print("\n")
                except: pass
            return nb

class CPUPlayer(Player):
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3,nbSticks)
        self.previousNeuron = None
    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)
    def playMedium(self,sticks):
        if sticks==4: return 3
        elif sticks==3: return 2
        elif sticks==2: return 1
        else: return self.playRandom(sticks)
    def playEasy(self,sticks):
        return self.playRandom(sticks)
    def playRandom(self,sticks):
        return random.randint(1, (sticks%3)+1)
    def playHard(self,sticks):
        if self.previousNeuron==None:                               # PREMIER TOUR
            self.previousNeuron = self.netw.getNeuron(sticks)
            neuronPrev = self.previousNeuron
            nextNeuron = neuronPrev.chooseConnectedNeuron(0)
            self.previousNeuron = nextNeuron
            self.netw.activateNeuronPath(neuronPrev,nextNeuron)
            return (neuronPrev.index-nextNeuron.index)
        elif sticks==1:                                             # DERNIER TOUR
            return 1    
        else:                                                       # TOURS INTERMEDIAIRES
            neuronPrev = self.previousNeuron
            nextNeuron = neuronPrev.chooseConnectedNeuron(neuronPrev.index-sticks)
            self.previousNeuron = nextNeuron
            self.netw.activateNeuronPath(neuronPrev,nextNeuron)
            return sticks-nextNeuron.index
    def getNeuronNetwork(self): return self.netw
    def setNeuronNetwork(self,ns): self.netw = ns
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None
    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None




        


