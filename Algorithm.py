import random

class N_Queue:
    def __init__(self):
        self.n=10
        self.clear()
    def clear(self):
        self.pos=list()
        self.running=False
        self.f=0
        self.method=0
        self.cnt=0
        self.rst=False
        self.colli_lst=[False for i in range(self.n)]
    def F(self,i,j)->int:
        tpos=self.pos.copy()
        a=tpos[i]
        tpos[i]=tpos[j]
        tpos[j]=a
        return self.calcu(tpos)
    def calcu(self,p)->int:
        rt=0
        self.colli_lst = [False for i in range(self.n)]
        for i in range(self.n):
            for j in range(i+1,self.n):
                if abs(p[i]-p[j])==abs(i-j):
                    rt+=1
                    self.colli_lst[i]=True
                    self.colli_lst[j]=True
        return rt
    def swap(self,i,j):
        a=self.pos[i]
        self.pos[i]=self.pos[j]
        self.pos[j]=a
    def genedata(self,rd=False):
        self.pos=list(range(self.n))
        if rd:
            random.shuffle(self.pos)
        self.f=self.calcu(self.pos)
    def restart(self,method):
        self.clear()
        self.method = method
        self.genedata()
        self.running=True
    def next(self)->bool:
        if not self.running:
            return False
        if self.method==0:
            self.stochastic()
        elif self.method==1:
            self.first_choice()
        else:
            self.random_restart()
        self.f=self.calcu(self.pos)
        return True
    def stochastic(self):
        tp_lst=list()
        for i in range(self.n):
            for j in range(i+1,self.n):
                newf=self.F(i,j)
                if newf<self.f:
                    tp_lst.append((i,j,newf))
        if len(tp_lst)==0:
            self.running=False
            return
        tp=tp_lst[random.randint(0,len(tp_lst)-1)]
        self.f=tp[2]
        self.swap(tp[0],tp[1])
        self.cnt+=1
    def first_choice(self):
        fla=False
        for i in range(self.n):
            for j in range(i + 1, self.n):
                newf = self.F(i, j)
                if newf < self.f:
                    self.f=newf
                    self.swap(i,j)
                    self.cnt+=1
                    fla=True
                    break
            if fla:
                break
        if not fla:
            self.running=False
    def random_restart(self):
        tp_lst = list()
        for i in range(self.n):
            for j in range(i + 1, self.n):
                newf = self.F(i, j)
                if newf < self.f:
                    tp_lst.append((i, j, newf))
        if self.f == 0:
            self.running = False
            return
        self.rst=False
        if len(tp_lst)>0:
            tp = tp_lst[random.randint(0, len(tp_lst) - 1)]
            self.f = tp[2]
            self.swap(tp[0], tp[1])
            self.cnt += 1
        else:
            self.genedata(True)
            self.rst=True