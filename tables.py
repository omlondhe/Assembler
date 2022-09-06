
class LiteralTable:
    
    def __init__(self) -> None:
        self.keys = []
        self.values = []
        self.size = 0
        self.keyTracker = {}
    
    def getIndexOfKey(self, key: str) -> int:
        for i in range(poolTable[-1], self.keys.__len__()):
            if key == self.keys[i]:
                return i
        return 0

    def getValue(self, key: str) -> str:
        return self.values[0]
    
    def add(self, key: str, value: int) -> None:
        if key in self.keyTracker: return 
        self.keys.append(key)
        self.values.append(value)
        self.size += 1
        self.keyTracker[key] = value
    
    def update(self, index: int, address: int) -> int:
        self.values[index] = address
        return self.keys[index]
    
    def print(self) -> None:
        for i in range(self.size):
            print(f"{self.keys[i]}:\t{self.values[i]}")


symbolTable = {}
literalTable: LiteralTable = LiteralTable()
poolTable = []

