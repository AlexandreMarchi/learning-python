def summation(n:int):
    return sum(range(1,n+1))

def sum_product(a:int, b:int):
    somatorio_a = summation(a)
    somatorio_b = summation(b)
    prod = somatorio_a * somatorio_b
    return prod

def main():
    a = 3
    b = 4   
    print(sum_product(a,b))
main()