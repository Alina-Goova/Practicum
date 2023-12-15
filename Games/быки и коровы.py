c='3625'
n=''
while n!=c:
    print('Введите число:', end = ' ')
    n=input()
    b=0
    k=0
    for i in n:
        if i in c and c.find(i)==n.find(i):
            b+=1
        elif i in c:
            k+=1
    print('Быки:', b)
    print('Коровы:', k)
print('Победа!')
