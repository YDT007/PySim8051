#This program is still under development
import csv
#Register bank
Acc=None
class instructions():
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
    def toAcc(self,i):
        global Acc
        Acc=self.rbank[i]
    def toReg(self,i):
        global Acc
        self.rbank[i]=Acc
    def toAccimediate(self,r_val):
        global Acc
        Acc=r_val
#INCREMENT/Decrement statement
    def inc(self,i):
        global Acc
        if i=='Acc':
           Acc=Acc+1
        else:    
           i1=int(i[1:])
           self.rbank[i1]=self.rbank[i1]+1 
    def dec(self,i):
        global Acc
        if i=='Acc':
           Acc=Acc-1
        else:    
           i1=int(i[1:])
           self.rbank[i1]=self.rbank[i1]-1 
    def set(self,i):
        global Acc
        if i=='Acc':
           Acc=1
        else:    
           i1=int(i[1:])
           self.rbank[i1]=1           
    def reset(self,i,r):
        global Acc
        if i=='Acc':
            Acc=0
        else:    
           i1=int(i[1:])
           self.rbank[i1]=0 
#ADDITION statement
    #def add(self,i):
        #global Acc
        #Acc=Acc+self.rbank[i]

#Mnemonics
Mnemonics={"mov":None,"add":None,"inc":None,"dec":None,"set":None,"reset":None}
#All Move functions for addressing modes
def MOV1(r,rb,r_val):
    r.put(rb,r_val)
def MOV2(i,r):
    r.toAcc(i)
def MOV3(i,r):
    r.toReg(i)
def MOV4(r_val):
    global Acc
    Acc=r_val    
def ADD1(i,r):
    global Acc
    Acc=Acc+r.rbank[i]
def ADD2(r_val):
    global Acc
    Acc=Acc+r_val
def INC(i,r):
    r.inc(i)
def DEC(i,r):
    r.dec(i)       
#Addition,Increment,Decrement,Set and Clear functions for their respective Mnemonics    

#Mnemonics["mov"]=MOV1
#Mnemonics["add"]=ADD1
Mnemonics["inc"]=INC
Mnemonics["dec"]=DEC

#z=(input("Enter keyword and parameters:")).lower()
#z1=z.split()
#if z1[0] in Mnemonics:
#   z2=Mnemonics[z1[0]]
#parameters=[int(param) for param in z1[1:]]
#x=regBank()
#print(z2(x,*parameters))
Acc=10        
x=instructions()
def selecting_mov(row):
    #if len(row)==3:
    global x
    column1,column2,column3 = row
    z=Mnemonics(column1)
    if column1=='mov' and column2.startswith('R') and column3.startswith('#'):
        Mnemonics["mov"]=MOV1
        column2_int=int(column2[1:])
        column3_int=int(column3[1:])
        z(x,column2_int,column3_int)
    elif column1=='mov' and  column2.startswith('A') and column3.startswith('R'):
        Mnemonics["mov"]=MOV2
        column3_int=int(column3[1:])
        z(column3_int,x)     
    elif column1=='mov' and  column2.startswith('R') and column3.startswith('A'):
        Mnemonics["mov"]=MOV3
        column2_int=int(column2[1:])
        z(column2_int,x)
    elif column1=='mov' and  column2.startswith('A') and column3.startswith('#'):       
        Mnemonics["mov"]=MOV4
        column3_int=int(column3[1:])
        z(column3_int)
    else
        print('Invalid Syntax')  
def selecting_add(row):
    global x
    z=Mnemonics(column1)
    if len(row)==3:
       column1,column2,column3 = row
       if column1=='add' and  column2.startswith('A') and column3.startswith('R'):
          column3_int=int(column3[1:])
          Mnemonics["add"]=ADD1
          z(column3_int,x)
       elif column1=='add' and  column2.startswith('A') and column3.startswith('#'):
          column3_int=int(column3[1:])
          Mnemonics["add"]=ADD2
          z(column3_int)
#Start working from here 28/2/24(Add sub , mul, div, initialization of SJMP and DJNZ)               
def process_row(row):
    # This function can be customized to perform operations on each row
    if len(row)==3:
        column1=row[0]
        if column1=='mov':
           selecting_mov(row)
        elif column1=='add':
           selecting_add(row)
        elif column1=='inc':
           column2=row[1]
           z=Mnemonics(column1)
           global x
           z(column2,x)
        elif column1=='dec':
           column2=row[1]
           z=Mnemonics(column1)
           global x
           z(column2,x)         
    else:
        column1=row[0]
    #print(row)
    # print(str(type(column2_int)) + " " + str(type(column3_int)))
    #(columnn1).lower()
    #print(x.rbank[column2_int][0])
    #z=Mnemonics[column1]

    #if column1=='mov' and column3.startswith('#'):
        #column3_int=int(column3[1:])
        #column2_int=int(column2[1:])
        #z(x,column2_int,column3_int)
    #lse:
        #z(column2_int,x1)
            

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        # Skip header if it exists
        # next(reader, None)
        
        for row in reader:
            # Assuming each row has three columns
            popped_val=row.pop(1)
            split_val=popped_val.split(',')
            row.extend(split_val)
            if len(row)<=3:
                process_row(row)
            else:
                print("Invalid command")
file_path = "D:\PySim8051\PySim8051\Command.txt"  # Replace with the actual file path
read_csv_file(file_path)
print(x.print_register_bank())  
print(Acc)             

                 
                

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
     

