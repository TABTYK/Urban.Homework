def custom_write(file_name, strings):
    result = dict()
    N = 1
    file = open(f'{file_name}','a', encoding='utf-8')
    for string in strings:
        result[(f'{N}', f'{file.tell()}')] = f'{string}'
        file.write(f'{string}\n')
        N += 1
    file.close()
    return result

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

resultUwU = custom_write('test.txt', info)
for elem in resultUwU.items():
  print(elem)