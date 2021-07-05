#!/usr/bin/python3

import json
import random
import sys  

def main():
    # input file
    data_file = open(sys.argv[1])
    # output file
    output_file = open(sys.argv[2], 'w')

    data = json.load(data_file)

    # indexing starting point
    i = int(sys.argv[3])
    for obj in data:
        obj['id'] = i
        obj['rating'] = round((random.random() * 5), 1)
        i += 1

    json.dump(data, output_file)

    output_file.close()

if __name__ == '__main__':
    main()