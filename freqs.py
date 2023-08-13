a = int(input("Digite um número inteiro: "))

freq0 = freq1 = freq2 = freq3 = freq4 = freq5 = freq6 = freq7 = freq8 = freq9 = 0

while a > 0:
    digito = a % 10
    if digito == 0:
        freq0 += 1
    elif digito == 1:
        freq1 += 1
    elif digito == 2:
        freq2 += 1
    elif digito == 3:
        freq3 += 1
    elif digito == 4:
        freq4 += 1
    elif digito == 5:
        freq5 += 1
    elif digito == 6:
        freq6 += 1
    elif digito == 7:
        freq7 += 1
    elif digito == 8:
        freq8 += 1
    else:
        freq9 += 1
    a //= 10

print("Frequência de 0:", freq0)
print("Frequência de 1:", freq1)
print("Frequência de 2:", freq2)
print("Frequência de 3:", freq3)
print("Frequência de 4:", freq4)
print("Frequência de 5:", freq5)
print("Frequência de 6:", freq6)
print("Frequência de 7:", freq7)
print("Frequência de 8:", freq8)
print("Frequência de 9:", freq9)