def calculatorDecBi():

    inp = int(input("Insert a decimal number: "))

    sub = 2*inp
    list = []

    while sub > 1:
        sub = sub//2
        print(sub)
        rest = sub%2
        print(rest)
        list.append(str(rest))

    list.reverse()

    print("Binary Number:","".join(list))

# _________________________________________________
def calculatorBiDec():

    inp = input("Insert a binary number: ")

    i = 0
    biList = []

    for i in range(len(inp)):
        biNum = inp[i]
        biList.append(biNum)
        print(i)

    print(biList)
    biList.reverse()

    numDecimal = 0
    for j in range(len(biList)):
        numDecimal = numDecimal + (int(biList[j])*2**(j))

    print("Decimal Number: ",numDecimal)

# _________________________________________________
