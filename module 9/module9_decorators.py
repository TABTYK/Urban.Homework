def is_prime(func):
    def wrapper(*args,**kwargs):
        original_result = func(*args,**kwargs)
        if isinstance(original_result,int):
            print('Простое')
            return original_result
        elif isinstance(original_result,float):
            print('Составное')
            return original_result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

print(sum_three(2,5,7))