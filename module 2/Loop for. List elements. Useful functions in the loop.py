numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(numbers[1],len(numbers)+1):
    for j in range(numbers[1],len(numbers)+1):
        if i % j == 0 and i is not j:
            not_primes.append(i)
            break
        elif i % j == 0 and i == j:
            primes.append(i)
            break
        else:
            continue
print(primes)
print(not_primes)

