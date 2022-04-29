#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    c = []
    d = []
    for i in range(97,123):
        c.append(chr(i))
    for j in word:
        pos = c.index(j)
        d.append(h[pos])

    return max(d) * len(d)

if __name__ == '__main__':


    h = list(map(int, input().rstrip().split()))

    word = input()

    print(designerPdfViewer(h, word))

