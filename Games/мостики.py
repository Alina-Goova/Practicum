a=[['   ']*7 for i in range(7)]
n=0
k=0
while a[6][6]=='   ':
    a[n][k]='[ ]'
    n+=2
    if n>6:
        n-=7
        k+=1
for i in range(7):
    for j in range(7):
        if a[i][j]=='   ':
            if i%2==0:
                a[i][j]=' x '
            else:
                a[i][j]=' o '

def ris(a):
    print('    o', ' '*5, 'o', ' '*5, 'o', ' '*5, 'o')
    for i in range(7):
        if i%2==0:
            print('x', end=' '*2)
        else:
            print('  ', end=' ')
        for j in range(7):
            print(a[i][j], end=' ')
        if i%2==0:
            print(' x', end='')
        print()
    print('    o', ' '*5, 'o', ' '*5, 'o', ' '*5, 'o')

def pr(a):
    n=0
    k=0
    while k<7:
        if a[n][k]=='[ ]':
            return True
        n+=2
        if n>6:
            n-=7
            k+=1
    return False

t=['|', '-']
def zp(x, y, w, a):
    if x%2==0:
        a[x][y]='['+t[w%2]+']'
    else:
        a[x][y]='['+t[(w+1)%2]+']'

def prm1(x1, y1, w, a):
    if x1<0 or x1>6 or y1<0 or y1>6 or a[x1][y1]!='['+t[(x1+1)%2]+']':
        return False
    if y1==6:
        return True
    if prm1(x1+1, y1+1, w, a):
        return True
    if prm1(x1-1, y1+1, w, a):
        return True
    if prm1(x1, y1+2, w, a):
        return True
    return False

def prm2(x1, y1, w, a):
    if x1<0 or x1>6 or y1<0 or y1>6 or a[x1][y1]!='['+t[x1%2]+']':
        return False
    if x1==6:
        return True
    if prm2(x1+1, y1+1, w, a):
        return True
    if prm2(x1+1, y1-1, w, a):
        return True
    if prm2(x1+2, y1, w, a):
        return True
    return False

def prs(w, a):
    if w==1:
        for i in range(7):
            if a[0][i]=='[-]':
                if prm1(0, i, w, a):
                    return True
    if w==2:
        for i in range(7):
            if a[i][0]=='[|]':
                if prm2(i, 0, w, a):
                    return True
    return False

ris(a)
w=0
t1=['o', 'x']
mark=0
while pr(a) or not(prm(a, w)):
    mt=0
    w+=1
    if w==3:
        w=1
    print('Ход', w, 'игрока -', t1[w%2])
    while mt==0:
        print('Введите координаты ячейки, которую хотите заполнить:')
        x, y=map(int, input().split())
        if a[x][y]!='[ ]' or (x+y)%2!=0:
            print('Ячейка не может быть заполнена!!')
        else:
            zp(x, y, w, a)
            break
    ris(a)
    if prs(w, a):
        mark=12345
        break
if mark==12345:
    print('Игрок', w, 'победил!!')
else:
    print('Ничья!')
