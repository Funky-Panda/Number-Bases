def convertBinary(number, actualBase, base):

    base64_chars = get_base_character_set(base)

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
            # print(f"{number} = {newNumber} * {base} + {remainder}")
            questions.append([number, newNumber, base, remainder])
            remainder = base64_chars[remainder]

            binary = str(remainder) + binary
            number = newNumber
            break

        remainder = (number - newNumber * base)
        # print(f"{number} = {newNumber} * {base} + {remainder}")
        questions.append([number, newNumber, base, remainder])
        remainder = base64_chars[remainder]
        number = newNumber

        binary = str(remainder) + binary
    # print(questions)
    return binary , questions

def get_base_character_set(base):
    if base < 2 or base > 62:
        raise ValueError("Base must be between 2 and 36.")

    base64_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/="

    if base <= 36:
        return base64_chars[:base]
    else:
        return base64_chars[:36] + base64_chars[36:base]

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
        
# number = int(input("Please enter the number: "))
# actualBase = int(input("Please enter the base (2-10): "))
# base = int(input("Please enter the base that you want to convert to (2-10): "))

def convert_to_subscript(number):
    subscript_digits = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_digits)


# answer , working = convertBinary(number,actualBase,base)

# print(answer,working)
