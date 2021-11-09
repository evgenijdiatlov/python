a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = [x for x in a if x<5]
print(new_a)


N = int(input('Введите трехзначное число:\n'))
x = N // 100
y = (N - x*100) // 10
z = (N - x*100) - y*10
print(x+y+z)


"""
S_triagle == (p*(p-a)*(p-b)*(p-c))**0,5
S_circle == 3,14r**2
S_rectangle == a*b
"""
 
shape = input('Выберите фигуру:\n')
 
if shape = 'triagle':
    а = int(input ('введите сторону а:\n'))
    b = int(input ('введите сторону b:\n'))
    c = int(input ('введите сторону c:\n'))
    p = int(a+b+c)/2
    S_triagle = (p*(p-a)*(p-b)*(p-c))**0,5
    print (S_triagle)
elif shape = 'circle':
    r = int(inpyt ('Ведите радиус оружности r:\n'))
    S_circle = 3,14*r**2
    print (S_circle)
elif shape = 'rectangle':
    а = int(input ('введите сторону а:\n'))
    b = int(input ('введите сторону b:\n'))
    S_rectangle = a*b
    print(S_rectangle)
else:
    print('нет такой фигуры')
 
 
# print(product)
 