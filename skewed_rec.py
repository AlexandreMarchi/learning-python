def skewed_rec(m:int, n:int):
    esp = m-1
    for i in range(m):
        for j in range(esp):
            print('  ', end='')

        for j in range(n):
            print('[]', end='')
        print()
        esp -= 1

def main():
    skewed_rec(5,4)

main()