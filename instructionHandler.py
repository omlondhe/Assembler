from io import TextIOWrapper
from xml.etree.ElementInclude import include
from tables import symbolTable, literalTable, poolTable
import re
import variables
from utils import getInstructionData


def handleLabeledInstruction(instructionData: list[str]):
    label: str = instructionData[0]
    symbol: str = instructionData[1].upper()
    symbolTable[label] = variables.LC
    EMOTData: tuple(int) = variables.EMOT[symbol]

    if symbol == "DS":
        symbolTable[label] = variables.LC
        variables.processedAssemblyCode += f"{variables.LC}\n"
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) (C, {instructionData[2]})\n"

    elif symbol == "DC":
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[2]}\n"
        literalTable.add(instructionData[2], -1)

    elif symbol == "EQU":
        symbolTable[label] = symbolTable[instructionData[2]]
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) (C, {symbolTable[label]})\n"

    elif instructionData[2].upper().__contains__('='):
        if poolTable.__len__() == 0:
            poolTable.append(literalTable.size)

        instructionParameters: list[str] = instructionData[2].split(',')
        literal: str = instructionParameters[1]
        literalInt: int = int(literal.replace('=', '').replace('\'', ''))
        literalTable.add(literalInt, -1)
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[1]} {instructionData[2]}\n"
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) ({variables.symbols[variables.EMOT[instructionParameters[0]][0]]}, {variables.EMOT[instructionParameters[0]][1]}) (L, {literalTable.getIndexOfKey(literalInt)})\n"
    
    else:
        instructionParameters: list[str] = instructionData[2].split(',')
        reg: str = instructionParameters[0]
        variable: str = instructionParameters[1]
        symbolTable[variable] = -1
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[1]} {instructionData[2]}\n"
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) ({variables.symbols[variables.EMOT[reg][0]]}, {variables.EMOT[reg][1]}) (S, {symbolTable.__len__() - 1})\n"



def handleInstruction(instruction: str):
    instruction = re.sub("\s\s+", ' ', instruction).replace(", ", ',')

    if instruction.upper().startswith("START"): 
        variables.LC = int(instruction.split(' ')[1])
        EMOTData: tuple(int) = variables.EMOT["START"]
        variables.intermediateCode += f"({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) (C, {variables.LC})\n"
    
    elif instruction.upper().startswith("ORIGIN"):
        oldLC: int = variables.LC
        origin: str = instruction.split(' ')[1]
        if origin.__contains__('+'):
            symbol, displacement = origin.split('+')
            variables.LC = (symbolTable[symbol] + int(displacement))

        else: 
            variables.LC = int(origin)
        
        EMOTData: tuple(int) = variables.EMOT["ORIGIN"]
        variables.intermediateCode += f"{oldLC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) (C, {variables.LC})\n"
    
    elif instruction.upper() == "STOP":
        EMOTData: tuple(int) = variables.EMOT["STOP"]
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]})\n"
        variables.LC += 1

    elif instruction.split(' ').__len__() == 3:
        instructionData: list[str] = getInstructionData(instruction)
        handleLabeledInstruction(instructionData)
        variables.LC += 1
    
    elif instruction.__contains__('='):
        if poolTable.__len__() == 0:
            poolTable.append(literalTable.size)

        instructionData: list[str] = getInstructionData(instruction) 
        EMOTData: tuple(str) = variables.EMOT[instructionData[0]]  
        instructionParameters: list[str] = instructionData[1].split(',') 
        literal: str = instructionParameters[1]
        literalInt: int = int(literal.replace('=', '').replace('\'', ''))
        literalTable.add(literalInt, -1)
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[0]} {instructionData[1]}\n"
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) ({variables.symbols[variables.EMOT[instructionParameters[0]][0]]}, {variables.EMOT[instructionParameters[0]][1]}) (L, {literalTable.getIndexOfKey(literalInt)})\n"
        variables.LC += 1

    elif instruction.upper() in ["LTORG", "END"]:
        if  instruction.upper() == "END":
            EMOTData: tuple(str) = variables.EMOT[instruction.upper()]
            variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]})\n"

        for i in range(poolTable[poolTable.__len__() - 1], literalTable.size):
            variables.intermediateCode += f"{variables.LC} (DL, 2) (C, {literalTable.update(i, variables.LC)})\n"
            variables.LC += 1

        if instruction.upper() != "END":
            poolTable.append(literalTable.size)

        literalTable.keyTracker = {}

    elif instruction.__contains__(','):
        instructionData: list[str] = instruction.split(' ')
        EMOTData: tuple(str) = variables.EMOT[instructionData[0]]
        instructionParameters: list[str] = instructionData[1].split(',')
        reg: str = instructionParameters[0]
        variable: str = instructionParameters[1]
        symbolTable[variable] = -1
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[0]} {instructionData[1]}\n"
        variables.intermediateCode += f"{variables.LC} ({variables.symbols[EMOTData[0]]}, {EMOTData[1]}) ({variables.symbols[variables.EMOT[reg][0]]}, {variables.EMOT[reg][1]}) (S, {symbolTable.__len__() - 1})\n"
        variables.LC += 1
    
    else:
        print(instruction)
        variables.LC += 1
