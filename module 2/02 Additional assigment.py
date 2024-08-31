result = []

def lovushka(n):
    for i in range(1,n):
        for j in range(1,n):
            divider = i + j
            if i == j: 
                break
            if n % divider ==0:
                if result.count(i) and result.count(j): # проверяет есть ли j и i в списке result
                    break
                result.append(j)
                result.append(i)

    for k in range(len(result)):
        print(result[k], sep="", end='')

lovushka(20)
