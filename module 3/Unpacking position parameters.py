values_list = [12, 'а где', False]
values_list2 = [12, True]
values_dict = {'a':12, 'b':False, 'c': "qwerty"}
values_dict2 = {'a':12}

def print_params(a = 1, b = 'здесь был TABTYK', c = True):

    print(a,b,c)


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 52)
print_params(**values_dict2)