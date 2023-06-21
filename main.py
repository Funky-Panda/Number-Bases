def convertBinary(number,actualBase,base):
    negitiveNum = False
    if str(number)[0] == "-":
        negitiveNum = True


    if actualBase != 10:
        number = convertBase(number,actualBase)
    
    binary = ""
    while True:
        newNumber = int(number/base)
        if newNumber == 0.0:
            remainder = (number-newNumber*base)
            number = newNumber

            binary = str(remainder) + binary
            break
        remainder = (number-newNumber*base)
        number = newNumber

        binary = str(remainder) + binary


    if negitiveNum:
        strNumber = str(binary)[0]
        for i in range(1, len(str(binary))):
            if str(binary)[i] != "-":
                strNumber+=str(binary)[i]
        return strNumber

    return binary

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
        
number = int(input("Please enter the number: "))
actualBase = int(input("Please enter the base (0-10): "))
base = int(input("Please enter the base that you want to convert to (0-10): "))

print(convertBinary(number,actualBase,base))
