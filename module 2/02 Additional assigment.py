result = []

def lovushka(n):
    for i in range(1,n):
        for j in range(1,n):
            divider = i + j
            if i == j:
                continue
            if n % divider ==0:
                if result.count(i) and result.count(j):
                    continue
                result.append(i)
                result.append(j)

    for k in range(len(result)):
        print(result[k], sep="", end='')

lovushka(10)
