def count_elements(vet):
    max_value = max(vet)
    count = [0] * (max_value + 1)

    for num in vet:
        count[num] += 1

    for i in range(len(count)):
        if count[i] > 0:
            print(f"O número {i} ocorre {count[i]} vez(es) na lista.")

def main():
    vet = [1, 2, 3, 2, 4, 1, 3, 4, 5]
    count_elements(vet)
