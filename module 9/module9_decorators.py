def is_prime(func):
    def wrapper(*args,**kwargs):
        original_result = func(*args,**kwargs)
        modified_result = (original_result/x for x in range(1,original_result) if original_result % x == 0)
        #print(list(modified_result))
        if len(list(modified_result))==1:
            print('Простое')
            return original_result
        else:
            print('Составное')
            return original_result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

print(sum_three(2,5,7))
print(sum_three(5,5,7))
