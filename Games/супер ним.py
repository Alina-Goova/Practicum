import random
lis=[' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ']
m=[['']*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        m[i][j]='['+random.choice(lis)+']'

def pr(a):
    s=0
    for i in range(8):
        for j in range(8):
            if a[i][j]=='[#]':
                s+=1
    if s>0:
        return True
    return False

q='abcdefgh'
k=0
while pr(m):
    k+=1
    if k==3:
        k=1
    for i in range(8):
        print(8-i, end='   ')
        for j in range(8):
            print(m[i][j], end=' ')
        print()
    print()
    print('     a   b   c   d   e   f   g   h')
    print('Введите номер горизонтали или вертикали, с которой хотите снять все фишки:')
    a=input()
    if a in '12345678':
        for i in range(8):
            m[8-int(a)][i]='[ ]'
    elif a in q:
        for i in range(8):
            m[i][q.find(a)]='[ ]'
for i in range(8):
    print(8-i, end='   ')
    for j in range(8):
        print(m[i][j], end=' ')
    print()
print()
print('Игрок', k, 'победил!!!')
