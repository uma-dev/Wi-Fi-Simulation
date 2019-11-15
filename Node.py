from random import randrange

class Node:
    
    def  __init__(self, name):
        self.name = name
        self.cw = 10
        self.ebTime = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def EB(self):    
        self.ebTime = randrange(self.cw)

    def getEbTime(self):
        return self.ebTime
        
class AP:
    Rbps = 1000000
    tc = 40/Rbps
    tl = (1500+40)/Rbps
    DIFS = 40/Rbps
    SIFS = 20/Rbps
    DATA = 1500/Rbps
    ACK = 40/Rbps
    
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes
        
a = Node('omar')
a.EB()
print(a.getName())
print(a.getEbTime())

AP_1 = AP()
AP_1.addNode(a)
print(AP_1.getNodes())
