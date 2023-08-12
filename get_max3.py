def get_max3(vet: list) -> tuple[int, int, int]:
    max1 = max2 = max3 = float('-inf')

    for num in vet:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        else:
            if num > max2:
                max3 = max2
                max2 = num
            else:
                if num > max3:
                    max3 = num

    return max1, max2, max3

def main():
    vet = [7, 8, 21, 3, 3, 5, 1, 25, 10, 19, 29, 39, 47, 58, 46, 50]
    get_max3(vet)
    print(get_max3(vet))

main()
