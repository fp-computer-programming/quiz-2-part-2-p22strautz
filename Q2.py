# Author: SCT (AMDG) 11/17/21

import string

pos = input("Input something for Oscar to respond to\n")

neg = "not"

if neg in pos:
    print("pos")
if neg not in pos:
    print("{0} {1}".format(neg, pos))
