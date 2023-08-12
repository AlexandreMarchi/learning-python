def remove_all(vet:list, elem:int):
    for i in range(len(vet)):
        try:
            vet.remove(elem)
        except:
            print("Elemento retirado da lista")
            break
    print(vet)

def main():
    vet = [2,5,2,57,349,23,2,328,2,327,23,531,2,38,2]
    remove_all(vet,2)

main()