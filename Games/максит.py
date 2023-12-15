import random
a=[[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        a[i][j]=random.randint(1, 9)

t=[0]*2

def ris(a):
    for i in range(3):
        for j in range(3):
            print(a[i][j], end=' ')
        print()
        
def pr(a):
    for i in range(3):
        for j in range(3):
            if a[i][j]!=0:
                return True
    return False

def pr1(a, y):
    for i in range(3):
        if a[i][y]!=0:
            return True
    return False

def pr2(a, x):
    for i in range(3):
        if a[x][i]!=0:
            return True
    return False

n=0
w=0
ris(a)
while pr(a):
    n+=1
    if n==3:
        n=1
    w+=1
    print('Ход', n, 'игрока.')
    if w==1:
        print('Введите координаты (с нуля) числа, которое хотите вычеркнуть')
        x, y = map(int, input().split())
        t[n-1]+=a[x][y]
        a[x][y]=0
    else:
        mr=0
        pr1(a, y)
        pr2(a, x)
        while mr==0:
            if not(pr1(a, y1)) and not(pr2(a, x1)):
                mr=2
                break
            elif n==2 and not(pr1(a, y1)) or n==1 and not(pr2(a, x1)):
                mr=1
                break
            print('Введите координаты (с нуля) числа, которое хотите вычеркнуть')
            x, y = map(int, input().split())
            if n==2:
                if y==y1 and a[x][y]!=0 and pr1(a, y):
                    t[n-1]+=a[x][y]
                    a[x][y]=0
                    break
            else:
                if x==x1 and a[x][y]!=0 and pr2(a, x):
                    t[n-1]+=a[x][y]
                    a[x][y]=0
                    break
            
            print('Число не может быть вычеркнуто!!')
        if mr==1:
            print('Игрок', n, 'пропускает ход.')
            continue
        if mr==2:
            print('Игра окончена.')
            break
    ris(a)
    x1=x
    y1=y
print()
print('Баллов у 1 игрока:', t[0])
print('Баллов у 2 игрока:', t[1])
print()
if t[0]>t[1]:
    print('Игрок 1 победил!!')
elif t[0]<t[1]:
    print('Игрок 2 победил!!')
else:
    print('Ничья!!')
