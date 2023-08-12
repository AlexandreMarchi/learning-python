def find(vet:list,elem:int):
    vet.sort()
    i = 0
    f = len(vet)-1

    while i <= f:
        m = (i + f) // 2

        if vet[m] == elem:
            return m 
        elif vet[m] < elem:
            i = m + 1
        else:
            f = m - 1

    return None


        
        
def main():
    vet = [5,6,1,2,45,8,9,19,27,18,28] # [1,2,5,6,8,9,18,19,27,28,45]
    pos = find(vet,27)
    print(pos)

main()