a = int(input("Insira o a: "))
b = int(input("Insira o b: "))
c = int(input("Insira o c: "))

pa = int(input("Insira o PESO de a: "))
pb = int(input("Insira o PESO de b: "))
pc = int(input("Insira o PESO de c: "))


print(f"A média ponderada = {((a*pa)+(b*pb)+(c*pc))/(pa+pb+pc)}")