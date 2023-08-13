num = int(input("Insira votos: (1, 2, 3 ou 4) (5 para nulo) (6 para branco) (0 para finalizar): "))

freq1 = freq2 = freq3 = freq4 = freq5 = freq6 = 0

while num > 0:
    if num > 6:
        print("Voto inválido")
    num = int(input("> "))
    if num == 1:
        freq1 += 1
    elif num == 2:
        freq2 += 1
    elif num == 3:
        freq3 += 1
    elif num == 4:
        freq4 += 1
    elif num == 5:
        freq5 += 1
    elif num == 6:
        freq6 += 1
    
max = freq1
if freq2 > max:
    freq2 = max
if freq3 > max:
    freq3 = max
if freq4 > max:
    freq4 = max

if max == freq1:
    freq1 += freq6
if max == freq2:
    freq2 += freq6
if max == freq3:
    freq3 += freq6
if max == freq4:
    freq4 += freq6

print("Frequência de candidato 1:", freq1)
print("Frequência de candidato 2:", freq2)
print("Frequência de candidato 3:", freq3)
print("Frequência de candidato 4:", freq4)
print("Frequência de votos nulos: ", freq5)
