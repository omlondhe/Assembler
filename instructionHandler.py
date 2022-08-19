from io import TextIOWrapper
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
    elif instructionData[2].upper().__contains__('='):
        literal: str = instructionData[2].split(',')[1]
        literalTable.add(literal, -1)
        variables.processedAssemblyCode += f"{variables.LC} {instructionData[1]} {instructionData[2]}\n"


def handleInstruction(instruction: str):
    instruction = re.sub("\s\s+", ' ', instruction).replace(", ", ',')

    if instruction.upper().startswith("START"): 
        variables.LC = int(instruction.split(' ')[1])
    
    elif instruction.split(' ').__len__() == 3:
        instructionData: list[str] = getInstructionData(instruction)
        handleLabeledInstruction(instructionData)
        variables.LC += 1
    
    else:
        variables.processedAssemblyCode += f"{variables.LC} {instruction}\n"
        variables.LC += 1
