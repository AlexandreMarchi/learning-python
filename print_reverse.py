def print_reverse(vet:list):
    for i in range(len(vet)):
        print(vet[-1], end = ' - ')
        vet.pop()
    print('\b\b ')

def main():
    vet = [1,5,6,1,3,9,10,23,41,54] 
    print_reverse(vet)

main()       