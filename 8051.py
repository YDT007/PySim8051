#There will be 4 register banks where each of them having 8 bytes starting from R0-R7 and each of them having 8 bits.By the choice of PSW register we will have to choose the register banks. like if PSW.4=0,PSW.3=0 hence R0 will be selected

#Register bank
Acc=None
class regBank():
    def __init__(self):
        self.rbank=[]
        for i in range(8):
           self.r=[0]
           self.rbank.append(self.r)
        self.print_register_bank()   
    def print_register_bank(self):
        for row in self.rbank:
            print(row)
        print("--------")        
    def put(self,rb,r_val):
        self.rbank[rb]=r_val    

#MOVE statement
class MOV():
    def toAcc(self,i,r):
        global Acc
        Acc=r.rbank[i]
    def toReg(self,i,r):
        global Acc
        r.rbank[i]=Acc
    def toRegbank_add(self,i,j,r):
        r.rbank[i]=r.rbank[j]


#INCREMENT/Decrement statement
class I_D_S_C():
    def inc(self,i,r):
        global Acc
        if i=='Acc':
           Acc=Acc+1
        else:    
           i_n=list(range(8))
           if i==i_n[i]:
              r.rbank[i]=r.rbank[i]+1
           else:
               print("Syntax Error") 
    def dec(self,i,r):
        global Acc
        if i=='Acc':
           Acc=Acc-1
        else:    
           i_n=list(range(8))
           if i==i_n[i]:
              r.rbank[i]=r.rbank[i]-1
           else:
               print("Syntax Error") 
    def set(self,i,r):
        global Acc
        if i=='Acc':
           Acc=1
        else:    
           i_n=list(range(8))
           if i==i_n[i]:
              r.rbank[i]=1
           else:
               print("Syntax Error")   
    def reset(self,i,r):
        global Acc
        if i=='Acc':
            Acc=0
        else:    
           i_n=list(range(8))
           if i==i_n[i]:
              r.rbank[i]=0
           else:
               print("Syntax Error")  

#ADDITION statement
class ADD():
    def add(self,i,r):
        global Acc
        Acc=Acc+r.rbank[i]

#Mnemonics
Mnemonics={"mov":None,"add":None,"inc":None,"dec":None,"set":None,"reset":None}
def MOV1(r,rb,r_val):
    r.put(rb,r_val)
    return r.rbank[rb]

Mnemonics["mov"]=MOV1
z=(input("Enter keyword and parameters:")).lower()
z1=z.split()
if z1[0] in Mnemonics:
    z2=Mnemonics[z1[0]]
parameters=[int(param) for param in z1[1:]]
x=regBank()
print(z2(x,*parameters))        
 


        
                

                 
                

x=regBank() 
#x.put(3,70)
#x.print_register_bank()      
#x1=MOV()
#x1.toAcc(3,x)
#x2=I_D_S_C()
#x2.set(7,x)
#x2.reset(7,x)
#x.print_register_bank()
#x2=ADD()
#x2.add(3,x)
#print(Acc)





#JUMP(DJNZ) statement
     

