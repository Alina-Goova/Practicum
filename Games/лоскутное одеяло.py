print('Координаты отсчитываются с единицы!')
print()
m=[['[ ]']*10 for i in range(10)]
k=0
n=[0]*3

def pr(a):
    for i in range(1, 6):
        for j in range(1, 5):
            if a[i][j]=='[ ]':
                return True
    return False

for i in range(1, 6):
    for j in range(1, 5):
        print(m[i][j], end=' ')
    print()

s=0
while pr(m):
    k+=1
    if k==4:
        k=1
    print('Ход', k, 'игрока')
    z=0
    while z==0:
        print('Введите координаты клетки, которую хотите заполнить:')
        x, y = map(int, input().split())
        if m[x][y]=='[ ]':
            m[x][y]='['+str(k)+']'
            z=1
        else:
            print('Клетка уже заполнена')
    if m[x][y]==m[x-1][y]:
        s+=1
    if m[x][y]==m[x-1][y-1]:
        s+=1
    if m[x][y]==m[x-1][y+1]:
        s+=1
    if m[x][y]==m[x+1][y]:
        s+=1
    if m[x][y]==m[x+1][y+1]:
        s+=1
    if m[x][y]==m[x+1][y-1]:
        s+=1
    if m[x][y]==m[x][y-1]:
        s+=1
    if m[x][y]==m[x][y+1]:
        s+=1
    n[k-1]=+s
    for i in range(1, 6):
        for j in range(1, 5):
            print(m[i][j], end=' ')
        print()

print('Штрафных очков у игроков:')
print('1:', n[0])
print('2:', n[1])
print('3:', n[2])
if min(n)==n[0]:
    print('Игрок 1 победил!!')
elif min(n)==n[1]:
    print('Игрок 2 победил!!')
elif min(n)==n[2]:
    print('Игрок 3 победил!!')
