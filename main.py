def convertBinary(number, actualBase, base):

    letters = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'G',
        17: 'H',
        18: 'I',
        19: 'J',
        20: 'K',
        21: 'L',
        22: 'M',
        23: 'N',
        24: 'O',
        25: 'P',
        26: 'Q',
        27: 'R',
        28: 'S',
        29: 'T',
        30: 'U',
        31: 'V',
        32: 'W',
        33: 'X',
        34: 'Y',
        35: 'Z'
    }

    negativeNum = False
    if str(number)[0] == "-":
        negativeNum = True

    if actualBase != 10:
        number = convertBase(number, actualBase)

    binary = ""
    questions = []

    while True:
        newNumber = int(number / base)
        if newNumber == 0.0:
            remainder = (number - newNumber * base)
            print(f"{number} = {newNumber} * {base} + {remainder}")
            if remainder > 9:
                remainder = letters[remainder]

            binary = str(remainder) + binary
            questions.append([number, base, newNumber, remainder])
            number = newNumber
            break

        remainder = (number - newNumber * base)
        print(f"{number} = {newNumber} * {base} + {remainder}")
        if remainder > 9:
            remainder = letters[remainder]
        questions.append([number, base, newNumber, remainder])
        number = newNumber

        binary = str(remainder) + binary

    return binary+convert_to_subscript(str(base))

def convertBase(number, base):
    newNumber = 0
    strNum = str(number)
    negitiveNum = False
    for i in range(len(strNum)):
        if strNum[i] != '-':  # Skip the negative sign when converting
            newNumber = newNumber + int(strNum[i]) * pow(base, len(strNum) - (i + 1))
        else:
            negitiveNum = True

    if negitiveNum:
        return -newNumber
    return newNumber

def createSizeTable(data):
    os.system("clear")
    headers = ["Question", "Dividend", "Remainder"]
    table_data = [[size, count] for size, count in data.items()]
    print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))
        
number = int(input("Please enter the number: "))
actualBase = int(input("Please enter the base (2-10): "))
base = int(input("Please enter the base that you want to convert to (2-10): "))

def convert_to_subscript(number):
    subscript_digits = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_digits)

print(convertBinary(number,actualBase,base))
