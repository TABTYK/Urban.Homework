immutable_var = 1,2,'varchar', 1.3
print(immutable_var)

#immutable_var[0] = 200
#К элементу можно обратиться по индексу и использовать его, но изменить элемент кортежа нельзя, так как это неизменяемый тип данных.

mutable_list = [1,2,6]
mutable_list[2] = 128
print(mutable_list)