#Opcode table containing all op op-cpdes
#("opcode":("binary_value,type"))
opcode={
    "add"   :   ("00000",0),
    "sub"   :   ("00001",0),
    "mov"   :   (("00010",1),("00011",2)),
    "ld"    :   ("00100",3),
    "st"    :   ("00101",3),
    "mul"   :   ("00110",0),
    "div"   :   ("00111",2),
    "rs"    :   ("01000",1),
    "ls"    :   ("01001",1),
    "xor"   :   ("01010",0),
    "or"    :   ("01011",0),
    "and"   :   ("01100",0),
    "not"   :   ("01101",2),
    "cmp"   :   ("01110",2),
    "jmp"   :   ("01111",4),
    "jlt"   :   ("10000",4),
    "jgt"   :   ("10001",4),
    "je"    :   ("10010",4),
    "hlt"   :   ("10011",5)
}

# Discription of different type of opcodes
# opcode :  (No_of_register , require_imm , require_mem-add) 
types={
    0:  (3,False,False),
    1:  (1,True,False),
    2:  (2,False,False),
    3:  (1,False,True),
    4:  (0,False,True),
    5:  (0,False,False)
}


