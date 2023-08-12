def find_max2(vet:list) -> int:
    vet.sort()
    return vet[-2]

def main():
    vet = [1,5,6,2,6,908,8,3,10,29,38,16,26,27,284,182,389,390,170,402]
    find_max2(vet)
    print(find_max2(vet))

main()