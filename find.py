def find(vet:list,elem:int):
    for e in vet:
        if e == elem:
            print(f"O elemento está na posição {vet.index(e)}")
            break
    if elem in vet:
        pass
    else:
        print("O elemento não está na lista")

def main():
    vet = [1,5,2,5,1,6,12,32,56,1,2,5,6,12272,24717,217471,24,5,1,2,45,5,1,25,123,12,4,13,19]
    find(vet,6)

main()