def get_rows_by_number(file_name: str, start: int, stop=None, copy_table=False):
    with open(file_name, 'r', encoding='utf-8') as f:
        table=f.readlines()
        table_new=[]
        if stop==None:
            stop=len(table)
        for i in range(start, stop+1):
            table_new.append(table[i-1])
    if copy_table:
        with open(f'{file_name}_copy', 'w', encoding='utf-8') as f:
            for row in table_new:
                f.write(''.join([str(i) for i in row]))
    else:
        with open(file_name, 'w', encoding='utf-8') as f:
            for row in table_new:
                f.write(''.join([str(i) for i in row]))

get_rows_by_number('test2', 1, 3, True)
