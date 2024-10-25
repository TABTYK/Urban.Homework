import time
from threading import Thread

def write_words(word_count,file_name):
    with open(file_name,'a', encoding='UTF-8') as file:
        for x in range(1,word_count+1):
            file.write(f'Какое-то слово № {x}\n')
            time.sleep(0.1)
        file.close()
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()
write_words(10,'example1.txt')
write_words(30,'example2.txt')
write_words(100,'example3.txt')
write_words(50,'example4.txt')
end_time = time.time()
print('Безпотоковое выполнение:',end_time - start_time)

thr1 = Thread(target=write_words,args=(10,'example5.txt'))
thr2 = Thread(target=write_words,args=(30,'example6.txt'))
thr3 = Thread(target=write_words,args=(100,'example7.txt'))
thr4 = Thread(target=write_words,args=(50,'example8.txt'))


start_time_2 = time.time()
thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

end_time_2 = time.time()
print('Потоковое выполнение:',end_time_2 - start_time_2)