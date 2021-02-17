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

		type = parser.getType()
		
		if(type == "memory"):
			coder.writeMemoryAccess(parser.getCommand(), parser.segmentType(), parser.getVariable())
		elif(type == "arithmetic"):
			coder.writeArithmetic(parser.getCommand())
		
class Parser():
	def __init__(self):
		self.labels = {"LOCAL": 0, "R1": 1, "R2": 2, "R3": 3, "R4":4, "R5":5, "R6":6, "R7":7,
				"R8":8, "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, "R14": 14,
				"R15":15, "SCREEN":16384, "KBD":24576, "SP":0, "LCL":1, "ARG":2,
				"THIS":3, "THAT":4}	

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

	def setSymbol(self, label, value):
		self.labels[label] = value	

	def getSymbol(self):
		labels = self.labels
		command = self.command
		variableCount = self.variableCount
		x = None
		try:
			x = labels[command]
		except:
			print(labels)
			if(x == None):
				labels[command] = variableCount
				x = variableCount
				self.variableCount = variableCount+1
		
		return x
	
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
		#TODO: write a generic push/pull asmCode, and then add segment translation
		command = command.strip()
		segment = segment.strip()
		variable = variable.strip()
		
		segmentTranslate = {"temp": "temp", "constant": "constant", "local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"} 
		
		segment = segmentTranslate[segment]	

		if((segment == "constant") and (command == "push")):
			asmCode = "\n//this is a push constant translation\n@"+ variable +"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
			self.asmFile.write(asmCode) 
		elif((segment == "temp") and (command == "push")):
			asmCode = "@"+variable+"\nD=A\n@5\nD=A+D\n@temp\nM=D\n@temp\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
			self.asmFile.write(asmCode)
		elif((segment == "temp") and (command == "pop")):
			asmCode = "@SP\nM=M-1\n@" + variable + "\nD=A\n@5\nD=A+D\n@temp\nM=D\n@SP\nA=M\nD=M\n@temp\nA=M\nM=D\n"
			self.asmFile.write(asmCode)
		elif(command == "pop"):
			asmCode = "@SP\nM=M-1\n@" + variable + "\nD=A\n@" + segment + "\nA=M\nD=A+D\n@temp\nM=D\n@SP\nA=M\nD=M\n@temp\nA=M\nM=D\n"
			self.asmFile.write(asmCode)
		elif(command == "push"):
			#RAM[segment + variable] = RAM[pointer]
			#pointer=-1
			asmCode = "@"+variable+"\nD=A\n@" + segment + "\nA=M\nD=A+D\n@temp\nM=D\n@temp\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
			self.asmFile.write(asmCode)
	
	#stores address in a temp variable to be accessed when popped/pushed
	def setAddress(segment, variable):
		#finds the address number in the stack
		if(segment == "temp"):
			address = 5 + variable
		else:
			segmentTranslate = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"} 
		
			address = segmentTranslate[segment]  		

			asmCode = "" + variable + ""
		
		#stores this number in a variable 'stackAddress'
		asmCode = ""
		self.asmFile.write(asmCode)
	
	#uses above address set in temp to pop from stack
	def writePop():
		asmCode = ""
		self.asmFile.write(asmCode)
	
	#uses above address set in temp to push to stack
	def writePush():
		asmCode = ""
		self.asmFile.write(asmCode)
main()