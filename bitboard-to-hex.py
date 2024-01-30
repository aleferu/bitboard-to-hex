#!/usr/bin/env python3


# Copyright 2024 Alejandro Fernández <aleferu888@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
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
            skipped = False
            for line in lines:
                line = line.strip()
                if len(line) != 8:
                    print(f"Skipping {path}: invalid line")
                    skipped = True
                    break
                for c in line:
                    if c == '1':
                        number |= 1 << index
                    index -= 1
            if skipped:
                continue
            print(f"{path}: {format(number, '#018x')}")
