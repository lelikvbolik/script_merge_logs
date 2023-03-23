import argparse
import json

def get_data(file_object):
    l1 = file_object.readline()
    if l1:
        return l1, json.loads(l1)
    else:
        return None, None

def merge_files(file1, file2, out):
    file1_data = open(file1, 'r')
    file2_data = open(file2, 'r')
    out_data = open(out, 'w')
    l1, j1 = get_data(file1_data)
    l2, j2 = get_data(file2_data)
    while j1 and j2:
        if j1["timestamp"] < j2["timestamp"]:
            out_data.writelines([l1])
            l1, j1 = get_data(file1_data)
        else:
            out_data.writelines([l2])
            l2, j2 = get_data(file2_data)
    while j1:
        out_data.writelines([l1])
        l1, j1 = get_data(file1_data)
    while j2:
        out_data.writelines([l2])
        l2, j2 = get_data(file2_data)
    out_data.close()
    file1_data.close()
    file2_data.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('log1')
    parser.add_argument('log2')
    parser.add_argument('-o')
    args = parser.parse_args()
    print(args.log1)
    print(args.log2)
    print(args.o)
    merge_files(args.log1, args.log2, args.o)