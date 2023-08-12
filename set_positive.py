def set_positive(vet:list):
    for e in vet:
        if e < 0:
            e = e*(-1)
            print(e, end = ' ')
        else:
            print(e, end = ' ')
    print('\b ')

def main():
    vet = [1,-5,67,-45,-1,-1,0,48]
    set_positive(vet)

main()