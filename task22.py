# product = input('insert the product:\n')
# if product == "milk":
#     print(3)
# else:
#     if product == "butter":
#         print(5)
#     else:
#         if product == 'bread':
#             print(7)
#         else:
#             print(-1)
# #print(product)

# product = input('insert the product:\n')
# if product == "milk":
#     print(3)
# elif product == "butter":
#     print(5)
# elif product == 'bread':
#     print(7)
# else:
#     print(-1)

# product = input('insert the product:\n')

# shop_items = {
#     'milk': 3,
#     'butter': 5,
#     'bread': 7
# }

# print(shop_items.get(product, -1))

# i = 0

# while i < 10:
#     i += 1 # прибавить 1 к i
#     print(i)

# i = 0

# while i < 10 and type(i) == int or type(i) == float):
#     i += 1 # прибавить 1 к i
#     print(i)

# d = {
#     'a': 123,
#     'b': 231,
#     'c': 321,
#     'd': 421,
#     'e': 521,
# }
# #for x in d:
# # for x in d.keys():
# # for x in d.values():
# for x in d.items():
#     for y in x:
#         print(y)


# telephone_nomber = "+36775466437"
# for elem in telephone_nomber:
#     if elem == "+":
#         continue # пропускает команду +
#     print(elem)

# telephone_nomber = "+3677546f6437"
# for elem in telephone_nomber:
#     if elem == "+":
#         continue
#     if not elem.isdigit():
#         print('ошибка')
#         break
#     print(elem)
# else:
#     print('все ок')

array = [1, 2, 3, 4, 5, 6, 7, 54, 49, 14, 45, 56]

for i, x in enumerate(array):
    if x % 7 == 0:
        print(x, i)
        
