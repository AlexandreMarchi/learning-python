def find_min_max(vet:list) -> tuple[int,int]:
    vet.sort()
    return [vet[0],vet[-1]]

def main():
    vet = [56,1,2,16,12,6,21,213,5,1235,123,5531]
    find_min_max(vet)
    print(find_min_max(vet))

main()