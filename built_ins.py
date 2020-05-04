#abs(number) возвращает модуль (абсолютное значение) числа
# print(abs(-1.5))

#all(iterable) возвращает True, если все элементы iterable правдивы
# print(all(['a', 'b', '']))
# def all(iterable):
#     result = True
#     for item in iterable:
#         if not item:
#             result = False
#             break
#     return result

#any(iterable) возвращает True, если хотя бы один элемент правдив
# print(any(['', '', '', '']))

# def any(iterable):
#     result = False
#     for item in iterable:
#         if item:
#             result = True
#             break
#     return result

#class bool(x) - возвращает значение булевого типа для x
#0, '', [], {}, set(), (), None - False, всё остальное True
# print(bool(1)) 

#class dict(iterable) - Берёт iterable и создаёт из него словарь
# print(dict([("math", 2),('logic', 3),('history', 5)])) 

#dir(object) - выдаёт список аттрибутов объекта
# print(dir(1))

#enumerate(iterable, start=0)
# for i in enumerate([1,2,3,4,5,6], start=1):
#     print(i)

#class float(number or string) - переводит в число с плавающей точкой

#class frozenset(iterable) - создаёт из iterable неизменяемое

# help(object) - выдаёт справочную информацию об объекте

# id(object) - выдаёт адрес объекта в памяти

#input(prompt_string) - запрашивает у пользователя ввод данных и возвращает его в виде строки

#class int(string or number) - переводит в целое число

#isinstance(objects, class_name) - проверяет, является ли объект экземпляром некого класса
# print(isinstance('2', str))

#len(sequence) - выдаёт длину послудовательности

#class list(iterable) - переводит iterable в список
# a = (1,2,3,4,5)
# b = list(a)
# print(isinstance(b, list))

#map(func, iterable) - применяет функцию func ко всем элементам iterable, возвращает итератор
# a = map(lambda x: x ** 2, [1,2,3,4,5,6,7])
# print(list(a))

#max(iterable) - выдаёт наибольший элемент iterable
#max(arg1,arg2,arg3....) - находит наибольший из аргументов

# print(max((2,3,4,5,0,10,20,9,12,21)))

#min(iterable) - выдаёт наименьний элемент iterable
#min(arg1,arg2,arg3....) - находит наименьший из аргументов

# print(min((2,3,4,5,0,10,20,9,12,21)))

#class object - является основой всех классов в Python

#pow(num1, num2) - num1 ** num2
# print(pow(5, 3))

#print(*objects, sep='', end='\n')
# for index, item in enumerate(range(10)):
#     print(index, item, sep='-')

#range(start, stop, step) - возвращает диапазон целых чисел от start до stop-1 с шагом step

#round(number, digits_count) - округляет number до точности digits_count

#class set(iterable) - создаёт множество из iterable

#sorted(iterable, key=None, reverse=False)

# a = ['Abc', 'def', 'BCd', 'DDD', 'xyz', 'ccc', 'bbb']
# print(sorted(a, key=str.lower, reverse=True))

#sum(iterable) - выдаёт сумму всех элементов iterable
a = [8,5,2,3,5,1,5,3,5]
# b = 0
# for item in a:
#     b += item
# print(b)
# print(sum(a))

#class tuple(iterable) - превращает iterable в кортеж

#class type(object) - выдаёт имя класса, экземпляром которого является object

"""zip(*iterable) - возвращает итератор, где i-й элемент каждой из последовательностей соотвествует i-му
   значению другой. Останавливается тогда, когда самая короткая последовательность исчерпывается
"""
a = ['Aybek', 'Ermek', 'Janylai', 'Olga']
b = [92, 95, 100, 87, 98]
c = zip(a, b)
print(list(c))



