def get_primes(vet:list) -> list:
    
    vet2 = []
    for e in vet:
        if e < 2:
            continue

        is_prime = True

        for i in range(2,e):
            if e % i == 0:
                is_prime = False
                break

        if is_prime:                    
            vet2.append(e)

    print(vet2)


def main():
    vet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    get_primes(vet)

main()