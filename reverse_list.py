def reverse_list(vet:list):
    for i in range(len(vet)):
        vet.insert(i,vet[-1])
        vet.pop(-1)
    print(vet)

def main():
    vet = [1,2,3,4,5,6,7]
    reverse_list(vet)

main()