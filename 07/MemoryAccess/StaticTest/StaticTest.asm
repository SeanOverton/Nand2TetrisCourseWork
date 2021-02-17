
//this is a push constant translation
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

//this is a push constant translation
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
//this is a pop static translation
@SP
M=M-1
@SP
A=M
D=M
@StaticTest8
M=D
//this is a pop static translation
@SP
M=M-1
@SP
A=M
D=M
@StaticTest3
M=D
//this is a pop static translation
@SP
M=M-1
@SP
A=M
D=M
@StaticTest1
M=D
//this is a push constant translation
@StaticTest3
D=M
@SP
A=M
M=D
@SP
M=M+1
//this is a push constant translation
@StaticTest1
D=M
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

//this is a push constant translation
@StaticTest8
D=M
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

