def is_prime(n: int) -> bool:
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def main():
    print(is_prime(2))

main()