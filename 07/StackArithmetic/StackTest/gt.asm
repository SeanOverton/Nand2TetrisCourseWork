@SP
M=M-1	//pointer decreased
A=M
D=M	//equals first number
@SP
M=M-1	//pointer-1
A=M	//equals second number 	
D=M-D

//check if D equals M
@TRUE
D;JLT	//if D=D-M, results in D = 0 then sets SP to true(-1) otherwise false(0)
D=0
@SP
A=M
M=D
@END
0;JMP
(TRUE)
D=-1
@SP
A=M
M=D
(END)
@SP
M=M+1