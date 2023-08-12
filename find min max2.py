def find_min_max(vet:list) -> tuple[int,int]:
    min = vet[0]
    max = vet[0]
    for i in range(len(vet)):
        if vet[i] < min:
            min = vet[i]
    for i in range(len(vet)):
        if vet[i] > max:
            max = vet[i]
    return min,max

def main():
    vet = [56,1,2,16,12,6,21,213,5,1235,123,5531]
    find_min_max(vet)
    print(find_min_max(vet))

main()