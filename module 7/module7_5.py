import os
import time

print('Текущая директория:',os.getcwd())
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:

        filepath = os.path.join(rf'C:\Users\mnk-g\PycharmProjects\pythonProject1\module 7\{file}')
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')