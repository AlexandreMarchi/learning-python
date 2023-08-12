def get_multiples(vet:list,value:int) -> list:
    vet2 = []
    for e in vet:
        if e % value == 0:
            vet2.append(e)
    print(vet2)

def main():
    vet = [1,3,6,7,5,10,23,22,25,30,18,15,55]
    value = 5
    get_multiples(vet,value)

main()