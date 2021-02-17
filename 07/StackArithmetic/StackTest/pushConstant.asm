@5 	//target to push to the RAM[segment + variable]
D=A

@SP
A=M	//assigns D address as pointer address value. D should be "5" from address[257]
M=D

@SP
M=M+1 	//pointer is now pointing at address[SP++]

