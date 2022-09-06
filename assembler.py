# Roll No: 321091
# GR No: 22120276
# Name: Om Prashant Londhe

from io import TextIOWrapper
from instructionHandler import handleInstruction
from test import printLiteralTable, printPoolTable, printSymbolTable
import variables

with open("./input.txt", 'r') as script:
    # reading the script
    code: str = script.read()
    # getting instruction list
    instructions: list[str] = code.split('\n')
    numberOfInstructions: int = instructions.__len__()
    # defining the output file
    outputFile: TextIOWrapper = open('output.txt', 'w')
    
    # looping over all the instructions
    for instruction in instructions:
        # proceeding only if the instruction is not just a blank line
        if instruction.__len__() != 0:
            handleInstruction(instruction)
    
    printSymbolTable()
    printLiteralTable()
    printPoolTable()

    # writing to output file
    outputFile.write(variables.intermediateCode)
    # closing the output file
    outputFile.close()
        
