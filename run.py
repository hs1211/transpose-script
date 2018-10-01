import sys
import pandas as pd


def read_file(file_name):
    return pd.read_csv(file_name, index_col=0, header=None).T


def write_file(file_name, trans_data):
    trans_data.to_csv(file_name, sep='\t', encoding='utf-8')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: %s filename \n')
        exit()

    trans_data = read_file(sys.argv[1])
    write_file(sys.argv[1]+'.trans', trans_data)


