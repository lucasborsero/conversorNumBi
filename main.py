from converterDeHex import calculatorDecHex, calculatorHexDec
from converterNumBi import calculatorDecBi, calculatorBiDec

q = "y"
while q == "y":

    choose = int(input("Choose the operation: \n1) Decimal -> Hexadecimal; \n2) Hexadecimal -> Decimal. \n3) Decimal -> Binary; \n4) Binary -> Decimal. \n"))

    if choose == 1:
        calculatorDecHex()
    elif choose == 2:
        calculatorHexDec()
    elif choose == 3:
        calculatorDecBi()
    elif choose == 4:
        calculatorBiDec()
    else:
        print("Error in the selection.\n")

    q = input("\nWanna go again? y/n\n")