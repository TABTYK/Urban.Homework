data_structure = [
  [1, 2, 3],
  {'a': 2, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

overallsum = 0

def calculate_structure_sum_dict(main_dict):
    dict_keys = list(main_dict.keys())
    dict_words = []
    for k in main_dict:
        word = main_dict.get(k)
        dict_words.append(word)
    dict_tuple = dict_words + dict_keys
    return calculate_structure_sum(dict_tuple)

def calculate_structure_sum(structure):
    global overallsum
    for i in structure:
        get_type = type(i)
        if get_type == list or get_type == tuple or get_type == set:
            calculate_structure_sum(i)
        elif get_type == int or get_type == float:
            overallsum = overallsum + i
        elif get_type == str:
            overallsum = overallsum + len(i)
        elif get_type == dict:
            calculate_structure_sum_dict(i)
        else:
            continue
    return overallsum

print(calculate_structure_sum(data_structure))
#print(calculate_structure_sum_dict({'a': 2, 'b': 5}))

