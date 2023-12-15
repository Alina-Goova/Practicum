print('Отсчет с единицы!!')
print()
a=[['[ ]']*12 for i in range(12)]

def pr(a):
    for i in range(1, 11):
        for j in range(1, 11):
            k=0
            if a[i][j]=='[#]':
                if a[i][j]==a[i+1][j-1]=='[#]':
                    k+=1
                if a[i][j]==a[i+1][j]=='[#]':
                    k+=1
                if a[i][j]==a[i+1][j+1]=='[#]':
                    k+=1
                if a[i][j]==a[i-1][j+1]=='[#]':
                    k+=1
                if a[i][j]==a[i][j+1]=='[#]':
                    k+=1
                if a[i][j]==a[i-1][j-1]=='[#]':
                    k+=1
                if a[i][j]==a[i-1][j]=='[#]':
                    k+=1
                if a[i][j]==a[i][j-1]=='[#]':
                    k+=1
                if k>=2:
                    return True
    return False

def ris(a):
    for i in range(1, 11):
        for j in range(1, 11):
            print(a[i][j], end=' ')
        print()

ris(a)
n=0
while not(pr(a)):
    n+=1
    if n==3:
        n=1
    print('Ход', n, 'игрока.')
    while n!=0:
        print('Введите координаты (отсчет с единицы!!!) ячейки, которую хотите заполнить:')
        x, y = map(int, input().split())
        if x<1 or x>10 or y<1 or y>10 or a[x][y]=='[#]':
            print('Ячейка не может быть заполнена!')
        else:
            a[x][y]='[#]'
            break
    ris(a)
n+=1
if n==3:
    n=1
print('Игрок', n, 'победил!!')
    
