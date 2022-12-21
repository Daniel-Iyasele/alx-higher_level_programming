#!/usr/bin/python3
for i in range(97, 122):
    if chr(i) =='q' or chr(i) == 'e':
        i+=1
    else:
        print("{}".format(chr(i)), end="")

