#Opcode table containing all op op-cpdes
#("opcode":("binary_value,type"))
opcode_table={
    "add"   :   ("00000",0),
    "sub"   :   ("00001",0),
    "movi"  :   ("00010",1),
    "mov"   :   ("00011",2),
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
    "je"    :   ("10010",4)
    # "hlt"   :   ("10011",5) 
}

error_table={
    -1: "Error: Typo Error at line: ",
    -2: "Error: Invalid var declaration at line: ",
    -3: "Error: Opcode can be used as label at line: ",
    -4: "Error: variable cannot be initialised in between at line ",
    -5: "Error: hlt cannot be used between program at line ",
    -6: "Error: Syntax not followed at line ",
    -7: "Error: not a valid resister at line ",
    -8: "Error: Invalid immediate Value/notation (correct->$value [0<=value<=255]) at line ",
    -9: "Error: Invalid variable used at line ",
    -10:"Error: labels cannot be used as variables at line ",
    -11:"Error: Variables cannot be used as labels at line ",
    -12:"Error: label not defined at line ",
    -13:"Error: Hlt statement missing at line ",
    -14:"Error: same variable name cannot be used at line ",
    -15:"Error: same label name cannot be used at line ",
    -16:"Error: label name cannot be null at line "
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

register_list={
    "R0":   "000",
    "R1":   "001",
    "R2":   "010",
    "R3":   "011",
    "R4":   "100",
    "R5":   "101",
    "R6":   "110",
    #"FLAGS":"111"
    }

