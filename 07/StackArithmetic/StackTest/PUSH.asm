//this testing stack POP

@258
D=A
@SP
M=D

@2048 	//stores 2048 as local (exmample segment) pointer location
D=A
@LCL
M=D

@3	//arbitrarilly chosen variable number
D=A
//@LCL 
@5	//default for when segment
//A=M 	//accesses segment pointer

D=A+D 	//D should now equal desired destination addresss ie. 2051?
        //M is now at the correct segment location
	//assigns M variable to D for final assignment

@temp	//should equal the final pop address ie. 2051
M=D

@5 	//target to push to the RAM[segment + variable]
D=A

@temp
A=M
M=D

//this is the actual PUSH from RAM[LCL+3] to stack pointer + 1

@3	//arbitrarilly chosen variable number
D=A
//@LCL 
//A=M 	//accesses segment pointer
@5

D=A+D 	//D should now equal desired destination addresss ie. 2051?
        //M is now at the correct segment location
	//assigns M variable to D for final assignment

@temp	//should equal the final push address ie. 2051
M=D

@temp
A=M
D=M

@SP
A=M	//assigns D address as pointer address value. D should be "5" from address[257]
M=D

@SP
M=M+1

