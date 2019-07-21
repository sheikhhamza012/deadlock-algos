class bankers(object):
    _resources=[]
    _pocess=[]
    _remaining=[]
    _sequence=[]
    def __init__(self,res, pro):
        self._resources=res
        self._pocess=pro
        for x in self._pocess:
            x.append([x[1][i]-x[0][i]  for i in range(0,len(x[0]))])
        sum=[0 for i in res]
        for x in self._pocess:
            for i in range(0,len(x[0])):
                sum[i]=sum[i]+x[0][i]
        self._remaining=[res[i]-sum[i] for i in range(0,len(sum))]
        self._sequence=[i for i in range(0,len(self._pocess))]
    def compare(self,l1,l2):
        com=[x-y for x,y in zip(l1,l2)]
        for i in range(0, len(com)):
            if(com[i]>0):
                return False
        return True
    def seq(self):
        seql=[]
        final=[]
        l=0
        while (len(self._pocess)>0 and l<len(self._pocess)*100):
            x=self._pocess.pop(0)
            y=self._sequence.pop(0)
            if(self.compare(x[2],self._remaining)==True):
                seql.append(x)
                final.append(y)
                self._remaining=[x + y for x, y in zip(x[2], self._remaining)]
            else:
                self._sequence.append(y)
                self._pocess.append(x)
            l+=1;
        return final
    def safe(self):
        x=self.seq()
        if(len(x)>0 and len(self._pocess)==0):
            self._pocess=x
            return True
        return False
    def req(self,pro,req):
        if(self.compare(req,self._pocess[pro-1][2])==True and self.compare(req,self._remaining)==True):
            self._pocess[pro-1][2]=[x-y for x,y in zip(self._pocess[pro-1][2],req)]
            self._pocess[pro-1][0]=[x+y for x,y in zip(self._pocess[pro-1][0],req)]
            self._remaining=[x-y for x,y in zip(self._remaining,req)]
            if(self.safe()):
                return True
            else:
                return False
        return False
name="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#res=[input("total resource {} instances:".format(name[i])) for i in range(0,input("no of resources: "))]
#pro=[[[input("allocated resource {} for process {}:".format(name[k],name[i])) for k in range(0,len(res))],[input("maximum resource {0} for process {1}:".format(name[k],name[i])) for k in range(0,len(res))]] for i in range(0,input("no of processes: ")) ]
res=[100,100,100]
pro=[[[1,1,1],[8,8,8]],[[1,0,0],[2,2,2]],[[3,3,3],[3,3,3]]]
alg= bankers(res,pro)
print(alg.compare([10,1],[10,10]))

print("1 to  check if unsafe\n2 to find safe sequence\n3 to request resource")
a=input()
if(a==1):
    print("it is safe" if(alg.safe()==True) else "unsafe")
if (a==2):
    n=alg.seq()
    print([name[x] for x in n] if len(n)==len(res) else "no seq")
if(a==3):
    i=input("request for process (1:A-n:n): ")
    req=[input("request resource {} : ".format(name[i])) for i in range(0,len(res))]
    print("allocated" if (alg.req(i,req)) else "not enough resources")