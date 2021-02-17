import sys

#opens file and creates binary file
def main():
	#create Parser and Code instance 
	parser = Parser("M=D")
	coder = Code()	

	#creates new binaryFile
	binFile = open(sys.argv[1][:-4] + ".hack", "w");

	firstParse = True
	
	def loop():
		#opens sourceFile
		sourceFile = open(sys.argv[1], "r")
		
		index = 0
		for line in sourceFile:
			parser.advance(line)
			
			def aCommand():
				print("Filtered Command: " + (str)(parser.command))

				if(parser.command.isnumeric()):
					#code = bin((int)(parser.command))
					code = "{:018b}".format((int)(parser.command))
				else:
					#code = bin(parser.getSymbol())
					code = "{:018b}".format(parser.getSymbol())
				
				#write to binFile and new line
				print("aCommand: " + code[2:]+"\n")
				binFile.write(code[2:])
				binFile.write("\n")

			def lCommand():
				if(firstParse):
					parser.setSymbol(parser.command, index)
					print("Label converted to value")
					print("Index: "+(str)(index))
					print("Filtered Command: " + (str)(parser.command))
					code = "{:018b}".format(parser.getSymbol())
			
					print("lCommand: " + code[2:]+"\n")
				else:
					print("Filtered Command: " + (str)(parser.command))
					code = "{:018b}".format(parser.getSymbol())
			
					#print("lCommand: " + code[2:]+"\n")
					#binFile.write(code[2:])
					#binFile.write("\n")
		
			def cCommand():
				print("Filtered Command: " + (str)(parser.command))
				code = bin(7) + coder.comp(parser.comp()) + coder.dest(parser.dest()) + coder.jump(parser.jump())
				
				#write to binFile

				print("cCommand: " + code[2:]+"\n")
				binFile.write(code[2:])
				binFile.write("\n")
			print("Index: "+(str)(index))
			type = parser.commandType()

			if(firstParse and type=="L_COMMAND"):
				lCommand()
			elif(firstParse and type != None):
				index = index+1
			elif(firstParse != True):
				if type == "A_COMMAND": aCommand()
				elif type == "L_COMMAND": lCommand() 
				elif type == "C_COMMAND": cCommand()
				else: continue	
		sourceFile.close
	
	loop()
	if(firstParse):
		firstParse = False
		loop()

	print("Succesful compilation")
	binFile.close		

class Parser():

	def __init__(self, last):
		self.last = last
		self.variableCount = 16
		self.jumpCommand = ""
		self.compCommand = ""
		self.destCommand = ""
		self.labels = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4":4, "R5":5, "R6":6, "R7":7,
				"R8":8, "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, "R14": 14,
				"R15":15, "SCREEN":16384, "KBD":24576, "SP":0, "LCL":1, "ARG":2,
				"THIS":3, "THAT":4}
		self.command=""
						
	
	def hasMoreCommands(self):
		return self.command != self.last

	def advance(self, command):	
		self.command = command
		print("Command: " + (str)(command))

	def commandType(self):
		command = self.command
		
		if "//" in command:
			self.command = command.split("//")[0]
			command = command.split("//")[0]
		
		if("\n" in command):
			self.command = command.split("\n")[0]
			command = command.split("\n")[0]
		
		if(command == ""):
			return None
	
		if "@" in command:
			self.command = command.split("@")[1].strip()
			return "A_COMMAND"
	
		if "(" in command:
			#should remove brackets
			self.command = command.replace("(", "")	
			self.command = self.command.replace(")", "")

			return "L_COMMAND"

		elif "=" in command:
				x = command.split("=")
				self.destCommand = x[0] 
				self.compCommand = x[1]

				if ";" in x[1]:
					y = x[1].split(";")
					self.compCommand = y[0]
					self.jumpCommand = y[1]
				else:
					self.jumpCommand = ""
				return "C_COMMAND"
	
		elif ";" in command:
			x = command.split(";")
			self.compCommand = x[0]
			self.jumpCommand = x[1]
			self.destCommand = ""
		else:	
			self.destCommand = ""
			self.jumpCommand = ""
			
		#note at this point all dest, comp, jump fields are correctly initialised
		return "C_COMMAND"

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
	
	#all return strings
	def dest(self):
		return self.destCommand

	def comp(self):
		return self.compCommand
		
	def jump(self):
		return self.jumpCommand

#all return strings of binary encoded and expect strings
class Code():
	def dest(self, destStr):
		destStr = destStr.strip()
		d1 = "0"
		d2 = "0"
		d3 = "0"
	
		if "A" in destStr:
			d1 = "1"
		if "D" in destStr:
			d2 = "1"
		if "M" in destStr:
			d3 = "1"		

		return d1+d2+d3

	def comp(self, compStr):
		
		compStr = compStr.strip()

		reg = ""
		code = ""

		if "M" in compStr:
			reg = "M"
			code = "1"
		else:
			reg = "A"
			code = "0"
		
		#TODO: add binary values for returning
		switcher = {"0": "101010", "1": "111111", "-1": "111010", "D": "001100", reg:"110000", "!D":"001101",
				 "!"+reg:"110001", "-D":"001111", "-"+reg:"110011", "D+1":"011111", reg+"+1":"110111",
				 "D-1":"001110", reg+"-1":"110010", "D+"+reg:"000010", "D-"+reg:"010011", 
				reg+"-D":"000111", "D&"+reg:"000000", "D|"+reg:"010101"}	
		newCode = None
		
		print("compStr:" + compStr)
		
		if(compStr != ""):		
			newCode = switcher[compStr]

		if (newCode != None):
			code += newCode
		else:
			code += "000000"
		return code

	def jump(self, jumpStr):
		
		jumpStr = jumpStr.strip()
		
		switcher = {"": "0b000", "JGT": bin(1), "JEQ": bin(2), "JGE": bin(3), "JLT": bin(4), "JNE": bin(5),
				"JLE": bin(6), "JMP": bin(7)}
		x = "0b0"
		
		if(jumpStr != ""):
			x = switcher[jumpStr]
		
		x = x[2:]

		if(len(x) == 3):
			return x
		elif(len(x) == 2):
			return "0"+x
		elif(len(x) == 1):
			return "00"+x
								

if __name__ == "__main__":
	main()