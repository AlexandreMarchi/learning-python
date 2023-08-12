def histogram(days:list):
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

def main():
    days = [19,21,25,22,20,17,15]
    histogram(days)
main()    