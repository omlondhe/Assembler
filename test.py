from tables import literalTable, symbolTable

def printSymbolTable():
    print("\nSymbol table:")
    for key, value in symbolTable.items():
        print(f"{key}:\t{value}")

def printLiteralTable():
    print("\nLiteral table:")
    literalTable.print()
