from database import *

#for errors use <= -1 for different error
global error
global variables
global labels
global program
global PC

def decimal_to_binary(n):
    s=""
    while(n>0 or len(s)<8):
        s=str(n%2)+s
        n=n//2
    return s

# select specific opcode and feed instructn to relevent function
def opcode_fetch():
    # try:
    funct=[decode_A,decode_B,decode_C,decode_D,decode_E,decode_F]
    global program
    global error
    global PC
    while (PC<len(program)-1):
        inst=program[PC]
        opcode=inst[0]
        if opcode in opcode_table.keys():
            print("valid opcode")
            if opcode=="mov":
                if inst[-1][0]=="$":
                    inst[0]=program[PC][0]=opcode="movi"
            funct[opcode_table[opcode][1]](PC)
        elif opcode=="var":
            error[PC]=-4
        elif opcode=="hlt":
            error[PC]=-5
        else:
            error[PC]=-1
        PC+=1
    # except:
    #     print("error in opcode_fetch")


def decode_A(pc):
    try:
        global program
        if(len(program[pc])==4):
            program[pc][0]=opcode_table[program[pc][0]][0]+"00"         #setting the opcode for formate A
            for i in range(1,4):
                if program[pc][i] in register_list.keys():
                    program[pc][i]=register_list[program[pc][i]]        #setting the resistors code 
                else:
                    error[pc]=-7
        else:
            error[pc]=-6
        #print(program)
    except:
        print("error in decode_A")


def decode_B(pc):
    try:
        global program
        if(len(program[pc])==3):
            program[pc][0]=opcode_table[program[pc][0]][0]
            if program[pc][1] in register_list.keys():
                program[pc][1]=register_list[program[pc][1]]
            else:
                error[pc]=-7
            if program[pc][2][0]=="$" and int(program[pc][2][1:])>=0 and int(program[pc][2][1:])<=255:
                program[pc][2]=decimal_to_binary(int(program[pc][2][1:]))
            else:
                error[pc]=-8
        else:
            error[pc]=-6
        print(program)    
    except:
        print("error in decode_B")

def decode_C(pc):
    return

def decode_D(pc):
    return

def decode_E(pc):
    return

def decode_F(pc):
    return


#filters labels and save their location in dictionary
def filter_labels():
    try:
        global program
        global PC
        global error
        global labels
        labels={}
        i=PC
        while(i<len(program)):
            first_str=program[i][0]
            if(first_str[-1]==":"):
                if(first_str[0:-1] in opcode_table):
                    error[i]=-3
                else:
                    labels[first_str[0:-1]]=i
                    program[i].remove(first_str)
            i+=1
    except:
        print("Error in filter labels")


# filters variabls at the starting and addning them to variables list
def filter_var():
    try:
        global program
        global variables
        global error
        global PC
        PC=0
        while(program[PC][0]=="var"):
            if(len(program[PC])==2):
                variables.append(program[PC][1])
            else:
                error[PC]=-2
            PC+=1
    except:
        print("Error in filtering error.")

#we are left with list of labels 
def main():
    global program
    global error
    global variables
    global PC
    variables=[]
    program=[]
    error={}
    for i in range(1,5):
        s=list(input().split(" "))
        if s[0]=="":
            s.remove("")
        program.append(s)
    # while True:
    #     try:
    #         s=tuple(input().split(" "))
    #         program+=(s,)
    #     except EOFError:
    #         break
    print(program)
    filter_var()
    filter_labels()
    opcode_fetch()
    print(variables,labels,error)
    

if __name__=="__main__":
    main()