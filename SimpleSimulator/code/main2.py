global MEM
global PC
global register_file
global halted

def binary_to_decimal(str):
    """Parameter binary number in string formate"""
    total=0
    n=len(str)
    for i in range(0,n):
        total+=(2**i)*int(str[n-1-i])
    return total

def decimal_to_binary(n, p):
    """2 parameters=> (no. to convert, no. of bits)"""
    s=""
    while(n>0 or len(s)<p):
        s=str(n%2)+s
        n=n//2
    return s

#Add, subtract, multiply and divide instruction=> Aditya
#opcode_code=> 0, 1, 6, 7
def ASMD(operands,opcode_code):
    # print("ASMD")
    global register_file
    global PC
    try:
        register_file[7]=[0,0,0,0]
        reg1=binary_to_decimal(operands[2:5])
        reg2=binary_to_decimal(operands[5:8])
        reg3=binary_to_decimal(operands[8:])
        if (opcode_code==0):
            total=register_file[reg2]+register_file[reg3]
            if(total > 255):
                register_file[7][0]=1
                total=total % 256
            register_file[reg1]=total
        elif (opcode_code==1):
            sub=register_file[reg2]-register_file[reg3]
            if(sub < 0):
                register_file[7][0]=1
                sub=0
            register_file[reg1]=sub
        elif (opcode_code==6):
            mul=register_file[reg2]*register_file[reg3]
            if(mul > 255):
                register_file[7][0]=1
                mul=mul % 256
            register_file[reg1]=mul
        elif (opcode_code==7):
            register_file[0]=register_file[reg2]//register_file[reg3]
            register_file[1]=register_file[reg2]%register_file[reg3]
    except:
        print("error in ASMD")
    finally:
        PC+=1

#mov instruction both imm and register_file=> Aditya
#opcode_code=> 2 & 3
def mov(operands,opcode_code):
    # print("mov")
    global register_file
    global PC
    try:
        if opcode_code == 3:
            reg1=binary_to_decimal(operands[5:8])
            reg2=binary_to_decimal(operands[8:])
            if reg2 == 7:
                a=register_file[7]
                register_file[reg1]=binary_to_decimal(str(a[0])+str(a[1])+str(a[2])+str(a[3]))
            else:
                register_file[reg1]=register_file[reg2]
        elif opcode_code==2:
            reg=binary_to_decimal(operands[0:3])
            imm=binary_to_decimal(operands[3:])
            register_file[reg]=imm
    except:
        print("error in mov")
    finally:
        register_file[7]=[0,0,0,0]
        PC+=1

#load and store instructions=> RA
#opcode_code=> 4 & 5
def load_store(operands,opcode_code):
    # print("load_store")
    global PC
    global MEM
    global register_file
    try:
        reg=binary_to_decimal(operands[0:3])
        mem_add=operands[3:]
        if opcode_code==4:
            register_file[reg]=binary_to_decimal(MEM[binary_to_decimal(mem_add)])
        elif opcode_code==5:
            MEM[binary_to_decimal(mem_add)]=decimal_to_binary(register_file[reg],16)
    except:
        print("error in load store")
    finally:
        register_file[7]=[0,0,0,0]
        PC+=1


#shift and Logical operations=> RK
#opcode_code=> 8, 9, 10, 11, 12 & 13
def shift_logical(operands, opcode_code):
    # print("shift logical")
    global PC
    global register_file
    try:
        if opcode_code == 9:    #lshift
            reg = binary_to_decimal((operands[0:3]))  # finding the register which is to modified
            imm = binary_to_decimal((operands[3:]))  # calculating immediate value
            reg_value = register_file[reg]
            output = (2 ** imm) * reg_value
            register_file[reg] = output
        elif opcode_code == 8:  #rshift
            reg = binary_to_decimal((operands[0:3]))  # finding the register which is to modified
            imm = binary_to_decimal((operands[3:]))  # calculating immediate value
            reg_value = register_file[reg]
            output = int(reg_value // (2 ** imm))
            register_file[reg] = output
        elif opcode_code == 10:  #xor
            reg1 = binary_to_decimal(operands[2:5])
            reg2 = binary_to_decimal(operands[5:8])
            reg3 = binary_to_decimal(operands[8:])
            value_of_reg2 = register_file[reg2]
            value_of_reg3 = register_file[reg3]
            output=value_of_reg2^value_of_reg3
            register_file[reg1] = output
        elif opcode_code==11:  #or
            reg1 = binary_to_decimal(operands[2:5])
            reg2 = binary_to_decimal(operands[5:8])
            reg3 = binary_to_decimal(operands[8:])
            value_of_reg2 = register_file[reg2]
            value_of_reg3 = register_file[reg3]
            register_file[reg1]=value_of_reg2|value_of_reg3
        elif opcode_code==12:   #and
            reg1 = binary_to_decimal(operands[2:5])
            reg2 = binary_to_decimal(operands[5:8])
            reg3 = binary_to_decimal(operands[8:])
            value_of_reg2 = register_file[reg2]
            value_of_reg3 = register_file[reg3]
            register_file[reg1] = value_of_reg2 & value_of_reg3
        elif opcode_code==13:
            reg1 = binary_to_decimal(operands[5:8])#finding register which has to be modified
            reg2 = binary_to_decimal(operands[8:])
            t=""
            for i in reg2:
                if i=="0":
                    t=t+"1"
                else:
                    t=t+"0"
            register_file[reg1]=binary_to_decimal(t)
    except:
        print("Error in Shift or Logical Operation")
    finally:
        register_file[7]=[0,0,0,0]
        PC=PC+1


# compare instruction=> RK
# opcode_code=> 14
def compare(operands, opcode_code):
    # print("compare")
    global register_file
    global PC
    try:
        register_file[7]=[0,0,0,0]
        if opcode_code==14:
            reg1 = register_file[binary_to_decimal(operands[5:8])]   # finding register which has to be modified
            reg2 = register_file[binary_to_decimal(operands[8:])]
            if reg1==reg2:
                register_file[7][3] = 1
            elif reg1>reg2:
                register_file[7][2] = 1
            elif reg1<reg2:
                register_file[7][1] = 1
    except:
        print("Error in compare")
    finally:
        PC=PC+1


#jump instruction=> RA
#opcode_code=> 15, 16, 17 & 18
def jump(operands,opcode_code):
    # print("jump")
    global PC
    global register_file
    try:
        new_PC=binary_to_decimal(operands[3:])
        if opcode_code==15:
            PC=new_PC
        elif (opcode_code==16) and (register_file[7][1]==1):
            PC=new_PC
        elif (opcode_code==17) and (register_file[7][2]==1):
            PC=new_PC
        elif (opcode_code==18) and (register_file[7][3]==1):
            PC=new_PC
        else:
            PC+=1
    except:
        print("error in jump")
    finally:
        register_file[7]=[0,0,0,0]

#halt instruction
#opcode_code=> 19
def halt(operands,opcode_code):
    # print("halt")
    global halted
    global register_file
    try:
        if opcode_code==19:
            halted=True
    except:
        print("error in halt")
    finally:
        register_file[7]=[0,0,0,0]


def execute(inst):
    global MEM
    global PC
    global register_file
    fun=[ASMD]*2+[mov]*2+[load_store]*2+[ASMD]*2+[shift_logical]*6+[compare]+[jump]*4+[halt]
    opcode_code=binary_to_decimal(inst[0:5])
    print(decimal_to_binary(PC,8) ,end=" ")
    fun[opcode_code](inst[5:],opcode_code)
    for i in range(0,7):
        print(decimal_to_binary(register_file[i],16), end=" ")
    a=register_file[7]
    print("0"*12+str(a[0])+str(a[1])+str(a[2])+str(a[3]))


def main():
    global register_file
    global PC
    global MEM
    global halted
    halted=False
    MEM=[]
    register_file={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:[0,0,0,0]} #<-Flag:[V,L,G,E]
    PC=0
            #uncomment to run manually
    # for i in range(0,3):
    #     s=input()
    #     MEM.append(s)
            #uncomment for Automated testing
    while True:
        try:
            s=input()
            MEM.append(s)
        except EOFError:
            break
    length_of_program=len(MEM)
    while(len(MEM)<256):
        MEM.append("0"*16)
    while(not halted):
        execute(MEM[PC])
    for j in MEM:
        print(j)


if __name__=="__main__":
    main()