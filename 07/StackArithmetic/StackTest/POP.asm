//this testing stack POP

@258
D=A
@SP
M=D

@12 	//target to pop to the RAM[segment + variable]
D=A
@257
M=D

@2048 	//stores 2048 as local (exmample segment) pointer location
D=A
@LCL
M=D

@SP
M=M-1 	//pointer is now pointing at address[SP--]


//this is the actual POP

@3	//arbitrarilly chosen variable number
D=A
//@LCL 
//A=M 	//accesses segment pointer
@5

D=A+D 	//D should now equal desired destination addresss ie. 2051?
        //M is now at the correct segment location
	//assigns M variable to D for final assignment

@temp	//should equal the final pop address ie. 2051
M=D

@SP
A=M	//assigns D address as pointer address value. D should be "5" from address[257]
D=M

@temp
A=M
M=D

