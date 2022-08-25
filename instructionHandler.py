from io import TextIOWrapper
from xml.etree.ElementInclude import include
from tables import symbolTable, literalTable, poolTable
import re
import variables
from utils import getInstructionData


def handleLabeledInstruction(instructionData: list[str]):
    label: str = instructionData[0]
    symbolTable[label] = variables.LC

    if instructionData[1].upper() == "DS":
        variables.processedAssemblyCode += f"{variables.LC}\n"
    elif instructionData[1].upper() == "DC":
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[2]}\n"
        literalTable.add(instructionData[2], -1)
    elif instructionData[1].upper() == "EQU":
        symbolTable[label] = symbolTable[instructionData[2]]
    elif instructionData[2].upper().__contains__('='):
        if poolTable.__len__() == 0:
            poolTable.append(literalTable.size)
        literal: str = instructionData[2].split(',')[1]
        literalTable.add(int(literal.replace('=', '').replace('\'', '')), -1)
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[1]} {instructionData[2]}\n"


def handleInstruction(instruction: str):
    instruction = re.sub("\s\s+", ' ', instruction).replace(", ", ',')

    if instruction.upper().startswith("START"): 
        variables.LC = int(instruction.split(' ')[1])
    
    elif instruction.upper().startswith("ORIGIN"):
        origin: str = instruction.split(' ')[1]
        if origin.__contains__('+'):
            symbol, displacement = origin.split('+')
            variables.LC = (symbolTable[symbol] + int(displacement))
        else: 
            variables.LC = int(origin)
    
    elif instruction.split(' ').__len__() == 3:
        instructionData: list[str] = getInstructionData(instruction)
        handleLabeledInstruction(instructionData)
        variables.LC += 1
    
    elif instruction.__contains__('='):
        if poolTable.__len__() == 0:
            poolTable.append(literalTable.size)
        instructionData: list[str] = getInstructionData(instruction)
        literal: str = instructionData[1].split(',')[1]
        literalTable.add(int(literal.replace('=', '').replace('\'', '')), -1)
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[0]} {instructionData[1]}\n"
        variables.LC += 1

    elif instruction.upper() in ["LTORG", "END"] :
        for i in range(poolTable[poolTable.__len__() - 1], literalTable.size):
            literalTable.update(i, variables.LC)
            variables.LC += 1
        poolTable.append(literalTable.size)
        literalTable.keyTracker = {}

    else:
        variables.processedAssemblyCode += f"{variables.LC} {instruction}\n"
        variables.LC += 1
