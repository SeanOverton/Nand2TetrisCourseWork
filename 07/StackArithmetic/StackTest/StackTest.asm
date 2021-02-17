
//this is a push constant translation
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a equal comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@TRUE1
D;JEQ
D=0
@SP
A=M
M=D
@END1
0;JMP
(TRUE1)
D=-1
@SP
A=M
M=D
(END1)
@SP
M=M+1

//this is a push constant translation
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a equal comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@TRUE2
D;JEQ
D=0
@SP
A=M
M=D
@END2
0;JMP
(TRUE2)
D=-1
@SP
A=M
M=D
(END2)
@SP
M=M+1

//this is a push constant translation
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a equal comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@TRUE3
D;JEQ
D=0
@SP
A=M
M=D
@END3
0;JMP
(TRUE3)
D=-1
@SP
A=M
M=D
(END3)
@SP
M=M+1

//this is a push constant translation
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is less than comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE4
D;JLT
D=0
@SP
A=M
M=D
@END4
0;JMP
(TRUE4)
D=-1
@SP
A=M
M=D
(END4)
@SP
M=M+1


//this is a push constant translation
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is less than comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE5
D;JLT
D=0
@SP
A=M
M=D
@END5
0;JMP
(TRUE5)
D=-1
@SP
A=M
M=D
(END5)
@SP
M=M+1


//this is a push constant translation
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is less than comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE6
D;JLT
D=0
@SP
A=M
M=D
@END6
0;JMP
(TRUE6)
D=-1
@SP
A=M
M=D
(END6)
@SP
M=M+1


//this is a push constant translation
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is less than comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE7
D;JGT
D=0
@SP
A=M
M=D
@END7
0;JMP
(TRUE7)
D=-1
@SP
A=M
M=D
(END7)
@SP
M=M+1


//this is a push constant translation
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is less than comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE8
D;JGT
D=0
@SP
A=M
M=D
@END8
0;JMP
(TRUE8)
D=-1
@SP
A=M
M=D
(END8)
@SP
M=M+1


//this is a push constant translation
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is less than comparison
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE9
D;JGT
D=0
@SP
A=M
M=D
@END9
0;JMP
(TRUE9)
D=-1
@SP
A=M
M=D
(END9)
@SP
M=M+1


//this is a push constant translation
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

//add translation
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M+D
@SP
A=M
M=D
@SP
M=M+1


//this is a push constant translation
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub translation
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1


//neg translation
@SP
M=M-1
A=M
D=M
@0
D=A-D
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
A=M
D=A&D
@SP
A=M
M=D
@SP
M=M+1


//this is a push constant translation
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
A=M
D=A|D
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
D=!D
@SP
A=M
M=D
@SP
M=M+1

