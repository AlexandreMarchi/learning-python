def print_ascii(col:int):
    print()
    for i in range(col):
        print("DEC OCT HEX CHR   ", end="")
    print()

    n = 94//col
    if 94 % col != 0:
        n += 1

    c = 33
    for i in range(n):
        for j in range(col):
            idx = c + n * j
            if idx > 126:
                break
            print("%03d %03o %03X %2c    " % (idx, idx, idx, idx), end="")
        c += 1
        print()
    print()
def main():
    print_ascii(5)

if __name__ == "__main__":
    main()