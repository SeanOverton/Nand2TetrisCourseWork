
//this is a push constant translation
@7
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@8
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

