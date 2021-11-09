n = 3
f = open('zveza.txt', 'w')
for i in range(n, 2 * n):
    f.write(' ' * (2 * n - 1 - i))
    f.write('* ' * i)
    f.write('\n')
 
# for i in range(2 * n - 2, n - 1, -1):
#     f.write(' ' * (2*n - 1 - i))
#     f.write('* ' * i)
#     f.write('\n')

f.close() 

# ??? не рисует последнию строку звездочек * * *
