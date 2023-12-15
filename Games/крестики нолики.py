print('Отсчет с единицы!')
print()
m=[['[ ]']*3 for i in range(3)]
def pp(m):
    for i in range(3):
        if m[i].count('[x]')==3 or m[i].count('[o]')==3 or m[0][i]==m[1][i]==m[2][i]=='[x]' or m[0][i]==m[1][i]==m[2][i]=='[o]':
            return True
        elif m[0][0]==m[1][1]==m[2][2]=='[x]' or m[0][0]==m[1][1]==m[2][2]=='[o]' or m[0][2]==m[1][1]==m[2][0]=='[x]' or m[0][2]==m[1][1]==m[2][0]=='[o]':
            return True
        else:
            return False
def em(m):
    for i in range(3):
        for j in range(3):
            if m[i][j]=='[ ]':
                return True
    return False
n=0
while em(m)==True:
    for i in range(3):
        for j in range(3):
            print(m[i][j], end=' ')
        print()
    mr=0
    n+=1
    if n==3:
        n=1
    print('Ход', n, 'игрока')
    if n==1:
        q='[x]'
    else:
        q='[o]'
    while mr==0:
        print('Введите координаты ячейки, в которой хотите нарисовать', q, ':')
        x, y=map(int, input().split())
        x-=1
        y-=1
        if m[x][y]=='[ ]':
            m[x][y]=q
            mr=1
        else:
            print('Ячейка уже занята!')
    if pp(m):
        for i in range(3):
            for j in range(3):
                print(m[i][j], end=' ')
            print()
        print('Игрок', n, 'победил!!!')
        break
if em(m) and not(pp(m)):
    for i in range(3):
        for j in range(3):
            print(m[i][j], end=' ')
        print()
    print('Ничья!')
