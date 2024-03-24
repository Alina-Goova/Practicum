desk=[['   ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '   '],
      ['   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '   '],
      ['8  ', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', '  8'],
      ['7  ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', '  7'],
      ['6  ', '.', '.', '.', '.', '.', '.', '.', '.', '  6'],
      ['5  ', '.', '.', '.', '.', '.', '.', '.', '.', '  5'],
      ['4  ', '.', '.', '.', '.', '.', '.', '.', '.', '  4'],
      ['3  ', '.', '.', '.', '.', '.', '.', '.', '.', '  3'],
      ['2  ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', '  2'],
      ['1  ', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', '  1'],
      ['   ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '   '],
      ['   ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '   ']
     ]

pole2={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
pole1={'8':2, '7':3, '6':4, '5':5, '4':6, '3':7, '2':8, '1':9}

def Desk():
    global desk
    for i in desk:
        for j in i:
            print (j, end=' ')
        print()

move_counter=0

def Moves(piece1):
    global rank1, file1, rank2, file2, piece
    if piece1 == 'r': #ладья
        if rank1==rank2 or file1==file2:
            if rank1==rank2:
                for i in range(file1+1, file2):
                    if desk[rank1][i]=='.':
                        return False
            else:
                for i in range(rank1+1, rank2):
                    if desk[file1][i]=='.':
                        return False
        else:
            print('Ладья так не ходит!')
            return False
        return True
    if piece1 == 'n': #конь
        if abs(rank1-rank2)==2 and abs(file1-file2)==1 or abs(rank1-rank2)==1 and abs(file1-file2)==2:
            return True
        else:
            print('Конь так не ходит!')
            return False
    if piece1 == 'b': #слон
        if abs(rank1-rank2)==abs(file1-file2):
            i=rank1
            j=file1
            k1=int((rank2-rank1)/abs(rank1-rank2))
            k2=int((file2-file1)/abs(file1-file2))
            print(k1, k2)
            while i!=rank2 and j!=file2:
                i+=k1
                j+=k2
                if desk[i][j]!='.':
                    return False
        else:
            print('Слон так не ходит!')
            return False
        return True
    if piece1 == 'q': #королева
        if abs(rank1-rank2)==abs(file1-file2) or rank1==rank2 or file1==file2:
            if abs(rank1-rank2)==abs(file1-file2):
                i=rank1
                j=file1
                k1=(rank2-rank1)/abs(rank1-rank2)
                k2=(file2-file1)/abs(file1-file2)
                while i!=rank2 and j!=file2:
                    i+=k1
                    j+=k2
                    if desk[i][j]!='.':
                        return False
            else:
                if rank1==rank2:
                    for i in range(file1+1, file2):
                        if desk[rank1][i]=='.':
                            return False
                else:
                    for i in range(rank1+1, rank2):
                        if desk[file1][i]=='.':
                            return False
        else:
            print('Ферзь так не ходит!')
            return False
        return True
    if piece1 == 'k': #король
        if (abs(rank1-rank2)==1 and abs(file1-file2)==1) or (rank1==rank2 and abs(file1-file2)==1) or (abs(rank1-rank2)==1 and file1==file2):
            if desk[i][j]!='.':
                return False
        else:
            print('Король так не ходит!')
            return False
        return True
    if piece == 'P': #пешка белых
        if (rank1-rank2==1 and file1==file2 and desk[rank2][file2]=='.') or (rank1-rank2==1 and abs(file1-file2)==1 and desk[rank2][file2]!='.'):
            return True
        else:
            print('Пешка так не ходит!')
            return False
    if piece == 'p': #пешка черных
        if (rank2-rank1==1 and file1==file2 and desk[rank2][file2]=='.') or (rank2-rank1==1 and abs(file1-file2)==1 and desk[rank2][file2]!='.'):
            return True
        else:
            print('Пешка так не ходит!')
            return False

while True:
    Desk()
    
    while True:
        print('Выберите фигуру')
        sqare1=tuple(input())
        rank1=pole1[sqare1[1]]
        file1=pole2[sqare1[0]]
        
        piece=desk[rank1][file1]
        print(piece)
        
        if piece == '.':
            print('Это не фигура')
            continue
        
        move_bool=(move_counter%2==0)
        reg_bool=(piece.isupper())
        
        if move_bool!=reg_bool:
            print('Это не ваша фигура')
            continue
        
        while True:
            print('Выберите новую позицию для фигуры')
            sqare2=tuple(input())
            rank2=pole1[sqare2[1]]
            file2=pole2[sqare2[0]]
            if rank1==rank2 and file1==file2:
                print('Фигура должна сменить позицию, а не остаться на прежней')
            else:
                break
        if Moves(piece.lower()):
            desk[rank1][file1]='.'
            desk[rank2][file2]=piece
            break
        else:
            print('Фигура не может пойти на эту позицию, выберите другую')
    
    move_counter+=1
    print(f'Ходов совершено: {move_counter}')
