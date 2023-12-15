import pickle

def load_table_pickle(file_name):
    with open(file_name, 'rb') as f:
        print(pickle.load(f))

def save_table_pickle(file_name, table):
    with open(file_name, 'wb') as f:
        pickle.dump(table, f)