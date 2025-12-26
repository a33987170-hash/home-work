#Дан список чисел. Найти сумму всех элементов.
#1. Сложение элементов списка


#lst = [1, 2, 3, 4]
#sum = 0
#for x in lst:
    #sum += x

#print(sum)

#Найди максимальное число в списке без использования max()

#lst = [5, 1, 9, 3, 7]
#mx = lst[0]

#for x in lst:
    #if x > mx:
        #mx = x

#print(mx)

#   Количество чётных чисел

#Посчитай, сколько в списке чётных чисел.

#lst = [2, 5, 6, 9, 8, 11]
#count = 0

#for x in lst:
   # if x % 2 == 0:
       # count += 1

#print(count)


#. Удаление всех нулей

#lst = [0, 5, 0, 3, 0, 7]
#new_lst = []

#for x in lst:
    #if x != 0:
        #new_lst.append(x)

#print(new_lst)


. #Разворот списка

#Развернуть список без использования reverse() и срезов ([::-1]).

#lst = [1, 2, 3, 4, 5]
#rev = []

#for i in range(len(lst)-1, -1, -1):
    #rev.append(lst[i])

#print(rev)

#Проверка на палиндром

#Проверь, является ли список палиндромом (читается одинаково вперёд и назад).

#lst = [1, 2, 3, 2, 1]
#is_pal = True

#for i in range(len(lst)//2):
    #if lst[i] != lst[-1 - i]:
       # is_pal = False
        #break

#print(is_pal)

#Удаление повторяющихся элементов

#Дан список. Сделай новый список, в котором удалены все дубликаты, но порядок сохранён.

#lst = [1, 2, 2, 3, 4, 3, 5]
#new_lst = []
#seen = set()

#for x in lst:
   # if x not in seen:
        #seen.add(x)
        #new_lst.append(x)

#print(new_lst)

#Слияние двух списков без повторений

#Даны два списка. Создай новый список, содержащий все уникальные элементы обоих.

#a = [1, 2, 3, 4]
#b = [3, 4, 5, 6]
#res = []

#for x in a + b:
    #if x not in res:
        #res.append(x)

#print(res)

# Подсчёт количества вхождений элемента

#Дан список и число. Определи, сколько раз число встречается в списке без count().

#lst = [1, 2, 3, 2, 4, 2, 5]
#target = 2
#count = 0

#for x in lst:
    #if x == target:
        #count += 1

#print(count)

#Сдвиг списка вправо

#Сдвинь все элементы списка вправо на 1 позицию. Последний элемент должен стать первым.

#lst = [1, 2, 3, 4]
#shifted = [lst[-1]]  
2
# 8 for i in range(len(lst)-1):
    #shifted.append(lst[i])

#print(shifted)

