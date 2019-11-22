from random import randrange
    
class AP:
    Rbps = 1e6
    t_DIFS = 40.0*8/Rbps
    t_SIFS = 20.0*8/Rbps
    t_DATA = 1500.0*8/Rbps
    t_ACK  = 40.0*8/Rbps
    
    def __init__(self):
        self.tc = self.t_DIFS
        self.tl = self.t_DATA + self.t_SIFS + self.t_ACK
        
    def StartSimulation(self, paqs):
        t=0
        eb =0
        eb_t = 0
        paq_tx = 0
        i = 1

        while (paq_tx < paqs):
            if (i%5 == 0):
                print(str(i) + '\tEB*DIFS' )
                eb = randrange(16)
                eb_t += eb
                t  += self.t_DIFS*eb
            elif((i+1)%5==0):
                print(str(i) + '\tACK' )
                t  += self.t_ACK
            elif((i+2)%5==0):
                print(str(i) + '\tSIFS')
                t  += self.t_SIFS
            elif((i+3)%5==0):
                print(str(i) + '\tDATA')
                t  += self.t_DATA
                paq_tx += 1
            elif((i+4)%5==0):
                print(str(i) + '\tDIFS')
                t  += self.t_DIFS
            i += 1
        print('Los paquetes transmitidos fueron ' + str(paq_tx))

        #bits en 1000 transmisiones/tiempo para las 1000 transmisiones
        Rbps_prom = (1500*8*paq_tx)/(t)
            
        return [t,float(eb_t)/paq_tx, Rbps_prom]

    
AP_1 = AP()
print(AP_1.StartSimulation(1000))
