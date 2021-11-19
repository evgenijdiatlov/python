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

product = input('insert the product:\n')

shop_items = {
    'milk': 3,
    'butter': 5,
    'bread': 7
}

print(shop_items.get(product, -1))

