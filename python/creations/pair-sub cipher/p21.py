replacements = {
# ------------------- lowercase ------------------
    "a": "l",
    "b": "c",
    "c": "b",
    "d": "j",
    "e": "i",
    "f": "h",
    "h": "f",
    "i": "e",
    "j": "d",
    "k": "s",
    "l": "a",
    "m": "z",
    "n": "x",
    "o": "w",
    "p": "q",
    "q": "p",
    "r": "u",
    "s": "k",
    "t": "y",
    "u": "r",
    "w": "o",
    "x": "n",
    "y": "t",
    "z": "m",
# ------------------- captialcase ------------------
    "A": "L",
    "B": "C",
    "C": "B",
    "D": "J",
    "E": "I",
    "F": "H",
    "H": "F",
    "I": "E",
    "J": "D",
    "K": "S",
    "L": "A",
    "M": "Z",
    "N": "X",
    "O": "W",
    "P": "Q",
    "Q": "P",
    "R": "U",
    "S": "K",
    "T": "Y",
    "U": "R",
    "W": "O",
    "X": "N",
    "Y": "T",
    "Z": "M",
# ------------------- symbols ------------------
    "<": "?",
    "?": "<",
    ",": "/",
    "/": ",",
    ".": ">",
    ">": ".",
    ";": "'",
    "'": ";",
    ":": ":",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "-": "=",
    "=": "-",
    "_": "+",
    "+": "_",
    "~": "`",
    "`": "~",
    "!": ")",
    ")": "!",
    "@": "(",
    "(": "@",
    "#": "*",
    "*": "#",
    "$": "&",
    "&": "$",
    "%": "^",
    "^": "%",

# ------------------- numbers ------------------
    "1": "0",
    "0": "1",
    "2": "9",
    "9": "2",
    "3": "8",
    "8": "3",
    "4": "7",
    "7": "4",
    "5": "6",
    "6": "5"
}

table = str.maketrans(replacements)
def cipher():
    text = input("Enter a phrase to scramble or unscramble: ")

    new_text = text.translate(table)

    print(new_text)

while True:
    cipher()
    choice = input("do you want to try again? (Y/N) ").lower().strip()
    if choice == "y":
        continue
    elif choice == "n":
        print("oka")
        break
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")
