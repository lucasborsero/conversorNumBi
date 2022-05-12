inp = int(input("Insira um número decimal: "))

sub = 2*inp
list = []

for i in range(0,9999999999999999999999999999999999):
    sub = sub//2
    rest = sub%2
    list.append(str(rest))

    if sub > 1:
        continue
    else:
        break

list.reverse()

print("Número binário:","".join(list))