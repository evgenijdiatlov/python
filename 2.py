# # first_name = 'Evgenij'
# # last_name = 'Diatlov'
# # #print ("Hello, {first} {last}".format(first=first_name, last=last_name))

# # print (f"Hello, {first_name} {last_name}")

# # N = int(input('enter seconds:\n'))
# # hours = N//3600
# # minutes = (N - hours*3600)//60
# # seconds = (N - hours * 3600) - minutes * 60
# # print (f'{hours}:{minutes}:{seconds}')


# # N = int(input('Введите секунды:\n'))
# # x = N // 3600
# # y = (N - x*3600) // 60
# # z = (N - x*3600) - y*60
# # print(f'{x}:{y}:{z}')

# teemp_string = 'aabbbaaabbAAAAAAAA'
# print(teemp_string.find('bb')) # откуда начинается строка с 'bb'
# print(teemp_string.find('bb', 4)) # откуда начинаеся строка 'bb' начиная с 4 позиции)
# print(teemp_string.replace('bb', 'cc')) 
# print(teemp_string.isdigit()) # является ли строка числом
# a = '1212334'
# print(a.isdigit())
# print('fac'.join(a))  
# print('     '.join(['1', '2', '3'])) #в список добавить fac (5пробелов)
# print(teemp_string.lower()) #перенос строки в нижний регистр
# print(teemp_string.upper()) #в верхний регистр
# print('GADFGHDFH'.lower())
# print('gsfhgjkjhgk'.upper())

#print(10!=11)

#l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#l.append(11) #добовляет в конец списка число 11
#l.pop(3) #удаляет число под индексом 3
#l.pop () #удаляет последнее число
#print(l.count(10)) #сколько цифер 10 в списке
#print(l.index(1)) # под каким индексом 1
#print(l)

#a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]] #не забывать между массивами запятые
# a = [1, 2, 3, 4, 5, 7, 6]
# b = a.copy() # можно [:] так. копирует значения а в b и можно работать 
# #над каждым в отдельности возможно со сложными системами не работает
# b.pop()
# a.reverse() # разварачивает массив
# a.sort() # сортирует массив
# print(a)
# print(b)

'''tuple - статический (неизменяемый) тип данных, может быть использован
в качесте ключа в словаре A=('s') != A=('s,')'''

# new_tuple = (1) # это int т.к. без запятой
# new_tuple1 = (1,) #это tuple т.к. есть запятая
# print(type(new_tuple))
# print(type(new_tuple1))
# print(new_tuple)
# print(new_tuple1)

'Операторы членства (in) =(в)'
# new_tuple = (1,2,3,4,5,6,7,8,9,10,)
# print(new_tuple.index(2))
# print(type(new_tuple))
# print(11 in new_tuple) #есть ли 11 в массиве

'''хэш функция hash(объект), только со статическими типами работает
код шифрования переменной'''
# print(hash('12345'))
# print(hash('123456'))
 
 #'dickt словари кей велью'
d = {
    'a': 'first value',
    'b': 'sekond value',
    'c': 'third value',
    1: 'one',
    (1,2,3,4,): 'typle'
}
print(d['a'])
print(d['b'])
print(d['c'])
print(d[1])
print(d[(1,2,3,4,)])

d = dict(key=123, second=321)
print(d['key'])


