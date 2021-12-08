# d = {
#     'a': 'first value',
#     'b': 'sekond value',
#     'c': 'third value',
#     1: 'one',
#     (1,2,3,4,): 'typle'
# }

# print(d.keys()) # вывод всех возможных ключей
# print(d.values()) #вывод всех возможных вэлью(значения)
# print(d.items()) # вывод всех ключей+значений
# print(list(d.items()))
# print(d['a'])
# print(d.get('c'))
# print(d.pop('c'))
# print(d.get('c', 'No value'))

#s = set ([1, 2, 3, 4, 5, 6]) # класс сет
#s = {1, 2, 3, 4, 5, 6}
# s = frozenset ([1, 2, 3])
# print(type(s))

# print (4 in s)
# print(12 in s)
# print

# a = 100
# #b = 1000
# b = a
# print(id(a))
# print(id(b))
# print(a is b)
# print(a == b)


# if 5 == 5:
#     print('true')
# else:
#     print('false') # else можно не использовать в данном случае

# if 5 >  5:
#     print('true')
#     if 4 == 4:
#         print('ok')
#         if 3 < 4:
#             print('зае..Ок')
# else:
#     print ('x..ня')

# is_working = False
# state = 'working' if is_working else 'not working'

# print(state)

# a = 2

# b = 'Ok' if a else "no"
# print(b)


a = int(input('enter nomber:\n'))
if a == 1:
    print('A')
elif a == 2:
    print('B') 
elif a == 3:
    print('C')
elif a == 4:
    print('D')
elif a == 5:
    print('E')
else:
    print('no result')
