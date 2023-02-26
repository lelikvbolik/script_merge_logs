import argparse
import json

def merged_files(file1, file2, out):
    file1_data = open(file1, 'r')
    file2_data = open(file2, 'r')
    lines = []
    for line in file1_data.readlines():
        obj = json.loads(line)
        lines.append(obj)
    for line in file2_data.readlines():
        obj = json.loads(line)
        lines.append(obj)
    lines.sort(key=lambda x: x["timestamp"])
    out_data = open(out, 'w')
    for line in lines:
        json_result = json.dumps(line)
        out_data.write(json_result)
        out_data.write('\n')
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
    merged_files(args.log1, args.log2, args.o)
