import csv

def load_table_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        reader=csv.reader(f)
        file=list(reader)
        for i in file:
            print(*i)
def save_table_csv(file_name, table):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer=csv.writer(f)
        for row in table:
            writer.writerow(row)