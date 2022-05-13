def calculatorDeBi():

    inp = int(input("Insert a decimal number: "))

    sub = 2*inp
    list = []

    while sub > 1:
        sub = sub//2
        rest = sub%2
        list.append(str(rest))

    list.reverse()

    print("Binary Number:","".join(list))

# _________________________________________________
def calculatorBiDe():

    inp = input("Insert a binary number: ")

    i = 0
    bi_list = []
    for i in range(len(inp)):
        biNum = inp[i:i+1]
        bi_list.append(biNum)
        i = i

    bi_list.reverse()

    numDecimal = 0
    for j in range(len(bi_list)):
        numDecimal = numDecimal + (int(bi_list[j])* 2**(j))

    print("Decimal Number: ",numDecimal)

# _________________________________________________

choose = int(input("Choose the operation: \n1) Decimal -> Binary; \n2) Binary -> Decimal. \n"))

if choose == 1:
    calculatorDeBi()
else:
    calculatorBiDe()

# _________________________________________________
