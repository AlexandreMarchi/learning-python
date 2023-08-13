a = int(input("Insira o número de dias: "))

ano = a // 365
semana = (a % 365) // 7
dia = (a % 365) % 7 
print(f"{a} dias = {ano} ano(s), {semana} semana(s) e {dia} dia(s)")