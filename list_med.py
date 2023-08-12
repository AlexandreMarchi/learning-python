def list_med(vet:list) -> float:
    sum = 0
    for e in vet:
        sum += e
    print(f"A média aritmetica: {sum/len(vet)}")

def main():
    vet = [1,23,4,6,12]
    list_med(vet)

main()