from tables import literalTable, symbolTable, poolTable

def printSymbolTable():
    print("\nSymbol table:")
    for key, value in symbolTable.items():
        print(f"{key}:\t{value}")

def printLiteralTable():
    print("\nLiteral table:")
    literalTable.print()

def printPoolTable():
    print("\nPool table:")
    for pool in poolTable:
        print(pool)
