import random

a=[['[ ]']*20 for i in range(20)]

def ris(mt, i1, j1):
    for i in range(i1, 10+i1):
        for j in range(j1, 10+j1):
            print(mt[i][j], end=' ')
        print()

def pole(a):
    for i in range(1, 5):
        for j in range(5-i):
            mark=0
            while mark==0:
                k=random.randint(1, 10)
                n=random.randint(1, 10)
                nap=0
                if i>1:
                    nap=random.randint(0, 2)
                if a[k][n]=='[ ]' and pr(k, n, i, nap):
                    imp(a, k, n, i, nap)
                    mark=1

def pr(k, n, i, nap):
    if nap==0:
        if k+i<11:
            if pr1(a, k, n, i, 0):
                return True
    if n+i<11:
        if pr1(a, k, n, 0, i):
            nap=1
            return True
    return False

def pr1(a, k, n, i, j):
    if i==0:
        i+=1
    if j==0:
        j+=1
    for i1 in range(k, k+i+1):
        for j1 in range(n, n+j+1):
            if pr2(i1, j1)==False:
                return False
    return True

def pr2(i, j):
    if a[i][j]!='[ ]':
        return False
    if a[i+1][j]!='[ ]':
        return False
    if a[i+1][j+1]!='[ ]':
        return False
    if a[i+1][j-1]!='[ ]':
        return False
    if a[i-1][j]!='[ ]':
        return False
    if a[i-1][j-1]!='[ ]':
        return False
    if a[i-1][j+1]!='[ ]':
        return False
    if a[i][j-1]!='[ ]':
        return False
    if a[i][j+1]!='[ ]':
        return False
    return True
  
def imp(a, k, n, i, nap):
    if nap==0:
        i1=i
        j1=1
    else:
        j1=i
        i1=1
    for i2 in range(k, k+i1):
        for j2 in range(n, n+j1):
            a[i2][j2]='[@]'

pole(a)

def pra(a):
    for i in range(1, 11):
        for j in range(1, 11):
            print(a[i][j])
            ww=a[i][j]
            if ww[1]=='@':
                return True
    return False

ris(a, 1, 1)

m=[['[ ]']*10 for i in range(10)]
while pra(a):
    mark=0
    print('Введите координаты, в которые хотите выстрелить:')
    while mark == 0:
        i, j=map(int, input().split())
        if i>9 or i<0 or j>9 or j<0:
            print('Координаты введены некорректно!')
        elif m[i][j]!='[ ]':
            print('Координаты введены некорректно!')
        else:
            if a[i+1][j+1]!='[ ]':
                a[i+1][j+1]='[ ]'
                m[i][j]='[X]'
                print('Попадание!!')
            else:
                m[i][j]='[o]'
                print('Промах!')
        ris(m, 0, 0)
        print()
        ris(a, 1, 1)
print('Игра окончена!!')
