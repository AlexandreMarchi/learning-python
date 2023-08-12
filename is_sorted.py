def is_sorted(vet:list) -> bool:
    for i in range(len(vet)-1):
        if vet[i] > vet[i+1]:
            return False
        else:
            pass
    return True

def main():
    vet = [1,2,3,4,5,6,7,8,9]
    is_sorted(vet)
    print(is_sorted(vet))

main()