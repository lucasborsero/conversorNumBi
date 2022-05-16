def calculatorDecHex():

    inp = int(input("Insert a decimal number: "))

    sub = inp
    listSub = []
    listRest = []

    while sub >= 1:
        
        rest = sub%16
        sub = sub//16
        
        listSub.append(sub)
        listRest.append(rest)

    hex = ["A", "B", "C", "D", "E", "F"]

    list = []

    for i in range(len(listRest)):
        if listRest[i] > 9:
            list.append(hex[listRest[i] - 10])
        else: 
            list.append(str(listRest[i]))

    list.reverse()

    print("Hexadecimal Number:","".join(list))
# _________________________________________________
def calculatorHexDec():

    inp = input("Insert a hexadecimal number: ")
    
    hexLet = ["A", "B", "C", "D", "E", "F"]
    hexNum = [10, 11, 12, 13, 14, 15]
    i = 0
    hexList = []

    for i in range(len(inp)):
        hexNum = inp[i:i+1]
        hexList.append(hexNum.upper())

    hexList.reverse()

    numDecimal = 0
    for j in range(len(hexList)):
        for k in range(len(hexLet)):

            if hexList[j] == hexLet[k]: 
                        
                hexList[j] = hexNum[hexLet.index(hexList[j])]
            
        numDecimal = numDecimal + (int(hexList[j])* 16**(j))

    print("Decimal Number: ",numDecimal)

# _________________________________________________