#!/usr/bin/env python3


import os
import sys


if __name__ == '__main__':
    if len(sys.argv) == 0:
        print("No files selected")
        exit()

    iterator = (path for path in sys.argv[1:] if os.path.isfile(path))
    for path in iterator:
        with open(path, 'r') as file:
            lines = file.readlines()
            if len(lines) != 8:
                print(f"Skipping {path}: not enough lines")
                continue
            index = 63
            number = 0
            for line in lines:
                line = line.strip()
                if len(line) != 8:
                    print(f"Skipping {path}: invalid line")
                    continue
                for c in line:
                    if c == '1':
                        number |= 1 << index
                    index -= 1
            print(f"{path}: {format(number, '#018x')}")
