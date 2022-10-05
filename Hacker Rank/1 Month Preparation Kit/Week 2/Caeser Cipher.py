#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    res = ""
    # Write your code here
    for i in s:
        if i in string.ascii_letters:
            if i.isupper():
                j = u.index(i) + k
                if j >= 26:
                    j %= 26
                j = u[j]
            else:
                j = l.index(i) + k
                if j >= 26:
                    j %= 26
                j = l[j]
        else:
            j = i
        res += j
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
# fff.jkl.gh
