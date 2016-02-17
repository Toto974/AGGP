
from random import *

class te:
    def __init__(self,ge=None):
        if ge is None :
            self.genome=[randint(0,1) for x in range(2000)]
        else:
            self.genome=ge[:]
    def fitness(self):
        r=0
        g = 0
        for i,x in enumerate(self.genome):
            r+= 2*x-1
            if i>1000:
                if r>4 or r<-4:
                    g+=1
        return g



def index(N,x):
    ind = 0
    j=0
    while x>ind:
        ind += N-j
        j+=1
        
    return j-1

class pyAG:
    def __init__(self,N,prod,txMut,txCross):
        self.N=N
        self.txMut=txMut
        self.txCross=txCross
        self.prod=prod
        self.pop=[prod() for i in range(N)]
        self.gen = 0
    def calc_fitness(self):
        self.f=[]
        self.fitm=0
        self.fim=1000
        for i,x in enumerate(self.pop): 
            fi=x.fitness()
            self.fitm += fi
            if self.fim>fi:
                self.fim=fi
            self.f.append([fi,i])
        self.f.sort()
        self.fitm/=1.0*self.N
    
    def new_pop(self):
        self.npop=[]
        for i in range(self.N):
            r= randint(0,(self.N+1)*(self.N)/2) #somme de 1 a N
            x=index(self.N,r)
            #       print self.f
            #a=self.f
            #print self.f[1][1]
            self.npop.append(self.prod(self.pop[self.f[x][1]].genome))
    def mutation(self):
        for x in self.npop:
            g = x.genome
            for i in range(len(g)):
                if random()<self.txMut:
                    g[i]=1-g[i]
            x.genome=g
    def cross(self):
        for x in self.npop:
            if random()<self.txCross: #taux de croisement
                g = x.genome
                r1= self.pop[randint(0,self.N-1)].genome #genome aleatoire dans la pop pour croiser avec le genome de l'individu x
                z= randint(0,len(g)-1)
                if random()<0.5: #prob de 0.5
                    g[0:z]=r1[0:z] #croisement aleatoire 
                else:
                    g[z:]=r1[z:]
                x.genome=g
    def update(self):
        self.pop=self.npop[:]
    def genloop(self):
        ga.calc_fitness()
        self.new_pop()
        self.mutation()
        self.cross()
        self.update()
        self.gen += 1
        print self.fitm,self.fim

seed(11)
ga = pyAG(100, te, 0.0001, 0.5)
#ga.calc_fitness()
for i in range(1000):
    ga.genloop()
r = 0
f = open("btr2.dat","w")
for x in ga.pop[ga.f[0][1]].genome:
    r += 2*x-1
    f.write("%d\n"%r)
f.close()
