def summation(n:int):
    return sum(range(1,n+1))

def main():
    print(summation(10) == 55)
    print(summation(5) == 15)
    print(summation(0) == 0)
    print(summation(-5) == 0)
main()