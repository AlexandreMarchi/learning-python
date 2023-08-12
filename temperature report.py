def temperature_report(days:list):
    print()
    print("D: ", end="")
    for i in range(days[0]):
        print(">",end="")

    print()

    print("S: ", end="")
    for i in range(days[1]):
        print(">",end="")

    print()

    print("T: ", end="")
    for i in range(days[2]):
        print(">",end="")

    print()

    print("Q: ", end="")
    for i in range(days[3]):
        print(">",end="")

    print()

    print("Q: ", end="")
    for i in range(days[4]):
        print(">",end="")

    print()

    print("S: ", end="")
    for i in range(days[5]):
        print(">",end="")

    print()

    print("S: ", end="")
    for i in range(days[6]):
        print(">",end="")

    print()
    print()

    print(f"A temperatura média foi de {(days[0]+days[1]+days[2]+days[3]+days[4]+days[5]+days[6])/7}")
    print(f"A temperatura mínima foi {min(days)}ºC")
    print(f"A temperatura máxima foi {max(days)}ºC")

def main():
    days = [19,21,25,22,20,17,15]
    temperature_report(days)
main()    