result = []

def lovushka(n):
    for i in range(1,n):
        for j in range(1,n):
            divider = i + j
            if i == j:
                break
            if n % divider ==0:
                if result.count(i) and result.count(j):
                    break
                result.append(i)
                result.append(j)
                continue

lovushka(20)
print(result)
