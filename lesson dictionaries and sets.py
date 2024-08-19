my_dict = {'Developer':969600,'User':707070}
print(my_dict)
print(my_dict['Developer'])
my_dict['Admin'] = 123456
print(my_dict)
my_dict.update({'Tester': 000000,
                'User2': 606060})
print(my_dict)
del my_dict['User2']
print(my_dict.get('User2'))

my_set = {3,3,3,2,2,1}
print(my_set)
my_set.update({4,5})
print(my_set)
my_set.remove(3)
print(my_set)
