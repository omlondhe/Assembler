
class LiteralTable:
    
    def __init__(self) -> None:
        self.map = {}
        self.keys = []
        self.values = []
        self.size = 0
        # self.keyIndex = []

    def getValue(self, key: str) -> str:
        return self.values[self.map[key]]
    
    def add(self, key: str, value: int) -> None:
        self.keys.append(key)
        self.values.append(value)
        self.map[key] = self.values.__len__() - 1
        self.size += 1
    
    def print(self) -> None:
        for i in range(self.size):
            print(f"{self.keys[i]}:\t{self.values[i]}")


symbolTable = {}
literalTable: LiteralTable = LiteralTable()
poolTable = {}

