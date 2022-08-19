LC: int = 0
processedAssemblyCode: str = ""

EMOT = {
    "STOP":   (1, 0),
    "ADD":    (1, 1),
    "SUB":    (1, 2),
    "MULT":   (1, 3),
    "MOVER":  (1, 4),
    "MOVEM":  (1, 5),
    "COMP":   (1, 6),
    "BC":     (1, 7),
    "DIV":    (1, 8),
    "READ":   (1, 9),
    "PRINT":  (1, 10),
    "START":  (3, 1),
    "END":    (3, 2),
    "ORIGIN": (3, 3),
    "EQU":    (3, 4),
    "LTORG":  (3, 5),
    "DS":     (2, 1),
    "DC":     (2, 2),
    "AREG":   (4, 1),
    "BREG":   (4, 2),
    "CREG":   (4, 3),
    "EQ":     (5, 1),
    "LT":     (5, 2),
    "GT":     (5, 3),
    "NE":     (5, 4),
    "LE":     (5, 5),
    "GT":     (5, 6),
    "ANY":    (5, 7),
}
symbols = {
    1: "IS",
    2: "DL",
    3: "AD",
    4: "RG",
    5: "CC",
}