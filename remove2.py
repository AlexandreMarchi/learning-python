def remove_all(vet:list,elem:int):
    i = 0
    while i < len(vet):
        if vet[i] == elem:
            vet.pop(i)
        else:
            i += 1
    print(vet)
            
            

def main():
    vet = [2,5,2,57,349,23,2,328,2,327,23,531,2,38,2]
    remove_all(vet,2)

main()