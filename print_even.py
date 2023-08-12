def print_even(vet:list):
    for e in vet:
        if e % 2 == 0:
            print(f"{e}", end =' ')
    print('\b ')

def main():
    vet = [5,1,2,6,7,8,10,24,14,28,3,6,19,16,2096552,576778]
    print_even(vet)

main()