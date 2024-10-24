# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).
print('\tПервое решение\n')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while int(my_list[i]) >= 0:
    if int(my_list[i]) > 0:
        print(my_list[i])
    i+=1
# print('\tВторое решение\n')
# my_list = sorted(my_list, reverse=True)
# while int(my_list[i]) >= 0:
#    if int(my_list[i]) > 0:
#        print(my_list[i])
#    i+=1
#
# print('\tТретье решение\n')
# while i < len(my_list):
#     if int(my_list[i]) > 0:
#         print(my_list[i])
#     i += 1
