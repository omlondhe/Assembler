# Roll No: 321091
# GR No: 22120276
# Name: Om Prashant Londhe

from io import TextIOWrapper

with open("./script.txt", 'r') as script:
    # reading the script
    code: str = script.read()
    # getting instruction list
    instructions: list[str] = code.split('\n')
    numberOfInstructions: int = instructions.__len__()
    # defining the output file
    outputFile: TextIOWrapper = open('output.txt', 'a')
    
    # looping over all the instructions
    for instruction in instructions:
        if instruction.__len__() != 0:
            print(instruction)
            # handleInstruction(outputFile, instruction)
    
    # closing the output file
    outputFile.close()
        
