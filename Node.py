from random import randrange

class Node:
    def  __init__(self, name):
        self.name = name
        self.cw = 16
        self.ebTime = randrange(self.cw)
        self.numOfCollitions = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getEbTime(self):
        return self.ebTime

    def decreaseEbTime(self):
        if(self.ebTime > 0):
            self.ebTime -= 1
            
    
class AP:
    Rbps = 1e6
    t_DIFS = 40.0/Rbps
    t_SIFS = 20.0/Rbps
    t_DATA = 1500.0/Rbps
    t_ACK  = 40.0/Rbps

    tc   = t_DIFS
    tl   = t_DATA + t_SIFS + t_ACK
    
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def allNodes(self):
        return self.nodes

    def getNode(self, index):
        return self.nodes[index]

    def fullSimulation(self, numOfNodes, numOfPackages):
        #start all nodes
        for i in range(numOfNodes):
            self.addNode( Node(i) )
        #print the decrease of the eb time
        for n in range(numOfPackages):
            for node in self.allNodes():
                print(node.getEbTime())
                node.decreaseEbTime()
            print('--------------------')

    def firstSimulation(self, cycles):
        t=0
        eb =0
        for i in range(1,cycles+1):
            self.addNode( Node(i) )
            eb += self.getNode(i-1).getEbTime()
            if (i%5 == 0):
                #print(str(i) + '\tEB*DIFS' )
                t  += self.t_DIFS*self.getNode(i-1).getEbTime()
            elif((i+1)%5==0):
                #print(str(i) + '\tACK' )
                t  += self.t_ACK
            elif((i+2)%5==0):
                #print(str(i) + '\tSIFS')
                t  += self.t_SIFS
            elif((i+3)%5==0):
                #print(str(i) + '\tDATA')
                t  += self.t_DATA
            elif((i+4)%5==0):
                #print(str(i) + '\tDIFS')
                t  += self.t_DIFS
            
        return [t,float(eb)/cycles]

    
AP_1 = AP()
#print (AP_1.firstSimulation(1000))

AP_1.fullSimulation(10,10)
