import sys

def main():
	print("Commencing VM Translation\n")
	print("-------------------------\n")
	parser = Parser()

	coder = CodeWriter()
	
	sourceFile = open(sys.argv[1])

	for line in sourceFile:
		if "//" in line:
			line = line.split("//")[0]
		
		if(line == ""):
			continue

		print("Parsing line: " + line + "\n")
		parser.setCommand(line)
		parser.parse()
		
		#arithmeticOptions = ("add", "sub", "neg", "eq", "gt", "lt", "and",
		#			"or", "not") 
		#memoryOptions = ("push", "pop")		

		type = parser.getType()
		
		if(type == "memory"):
			coder.writeMemoryAccess(parser.getCommand(), parser.segmentType(), parser.getVariable())
		elif(type == "arithmetic"):
			coder.writeArithmetic(parser.getCommand())
		
class Parser():
	def setCommand(self, command):
		self.type = None
		self.segment = None
		self.variable = None		

		self.command = command

	def parse(self):
		command = self.command

		parsedCommands = command.split(" ")

		self.command = parsedCommands[0].strip()
		
		try:		
			self.segment = parsedCommands[1].strip()
			self.variable = parsedCommands[2].strip()
			self.type = "memory"
		except:
			self.type = "arithmetic"
	
	def getType(self):
		return self.type

	def getCommand(self):
		return self.command
	
	def segmentType(self):
		return self.segment 
	
	def getVariable(self):
		return self.variable

class CodeWriter():
	def __init__(self):
		self.asmFile = open(sys.argv[1][:-3]+".asm", "w")
		self.count = 1

	#arithmetic is all performed by accessing virtual stack
	def writeArithmetic(self, command):
		c = (str)(self.count)		

		#needs newline (\n) characters implemented too to format asm file correctly
		translateDictionary = {"add":"\n//add translation\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M+D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n", 
					"sub":"\n//sub translation\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
					"neg":"\n//neg translation\n@SP\nM=M-1\nA=M\nD=M\n@0\nD=A-D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n", 
					"eq":"\n//this is a equal comparison\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D-M\n@TRUE"+c+"\nD;JEQ\nD=0\n@SP\nA=M\nM=D\n@END"+c+"\n0;JMP\n(TRUE"+c+")\nD=-1\n@SP\nA=M\nM=D\n(END"+c+")\n@SP\nM=M+1", 
					"gt":"\n//this is less than comparison\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@TRUE"+ c +"\nD;JGT\nD=0\n@SP\nA=M\nM=D\n@END"+ c +"\n0;JMP\n(TRUE"+ c +")\nD=-1\n@SP\nA=M\nM=D\n(END"+ c +")\n@SP\nM=M+1\n", 
					"lt":"\n//this is less than comparison\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@TRUE"+ c +"\nD;JLT\nD=0\n@SP\nA=M\nM=D\n@END"+ c +"\n0;JMP\n(TRUE"+ c +")\nD=-1\n@SP\nA=M\nM=D\n(END"+ c +")\n@SP\nM=M+1\n", 
					"and":"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nA=M\nD=A&D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
					"or":"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nA=M\nD=A|D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n", 
					"not":"@SP\nM=M-1\nA=M\nD=M\nD=!D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
					}

		if(command != ""):
			self.count = self.count+1
			code = translateDictionary[command]
			self.asmFile.write(code + "\n")

	def writeMemoryAccess(self, command, segment, variable):
		#TODO: segment needs to be translated and possibly variable?
		command = command.strip()
		segment = segment.strip()
		variable = variable.strip()
		
		if((segment == "constant") and (command == "push")):
			asmCode = "\n//this is a push constant translation\n@"+ variable +"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
			self.asmFile.write(asmCode) 
		elif(command == "pop"):
			asmCode = "@SP\nM=M-1\n@" + variable + "\nD=A\n@" + segment + "\nA=M\nD=A+D\n@temp\nM=D\n@SP\nA=M\nD=M\n@temp\nA=M\nM=D\n"
			self.asmFile.write(asmCode)
		elif(command == "push"):
			#RAM[segment + variable] = RAM[pointer]
			#pointer=-1
			asmCode = "@"+variable+"\nD=A\n@" + segment + "\nA=M\nD=A+D\n@temp\nM=D\n@temp\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
			self.asmFile.write(asmCode)

main()