print('Отсчет с нуля!')
print()
m=[['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '1', '1', '2', '1', '3', '1', '4', '1'], ['5', '1', '6', '1', '7', '1', '8', '1', '9']]
a=[['']*9 for i in range(50)]
for i in range(3):
    for j in range(9):
        a[i][j]=m[i][j]
l=3
def bl(mas):
    for i in range(l-1):
        for j in range(8):
            if mas[i][j]!='0' and mas[i][j] in '123456789' and mas[i][j]!='':
                if mas[i][j+1] in '123456789' and mas[i][j+1]!='':
                    if mas[i][j]==mas[i][j+1] or int(mas[i][j])+int(mas[i][j+1])==10:
                        return True
                if mas[i+1][j] in '123456789' and mas[i+1][j]!='':
                    if mas[i][j]==mas[i+1][j] or int(mas[i][j])+int(mas[i+1][j])==10:
                        return True
    if mas[l-1][8]!='0' and mas[l-1][8] in '123456789' and mas[l-1][8]!='':
        if mas[l-1][8]==mas[l-2][8] or int(mas[l-1][8])+int(mas[l-2][8])==10:
            return True
        if mas[l-1][7] in '123456789' and mas[l-1][7]!='':
            if mas[l-1][8]==mas[l-1][7] or int(mas[l-1][8])+int(mas[l-1][7])==10:
                return True
    return False
k=0
while bl(a):
    l1=l
    while bl(a)==True:
        for i in range(l+1):
            for j in range(9):
                print(a[i][j], end=' ')
            print()
        print('Bведите координаты чисел, которые хотите вычеркнуть:')
        m1, n1 = map(int, input().split())
        m2, n2 = map(int, input().split())
        if a[m1][n1]==a[m2][n2] or a[m1][n1]==a[m2][n2] or int(a[m1][n1])+int(a[m2][n2])==10:
            a[m1][n1]='0'
            a[m2][n2]='0'
        else:
            print('Эту пару нельзя вычеркнуть.')
    for i in range(l1):
        for j in range(9):
            if a[i][j]!='0':
                a[l][k]=a[i][j]
                k+=1
                if k==9:
                    k=0
                    l+=1
print('Игра окончена!')
