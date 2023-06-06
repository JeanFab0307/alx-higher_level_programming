#!/usr/bin/python3
for i in range(0, 9+1):
    j = 0
    for j in range(0, 9+1):
        if i != j and j > i:
            if i != 0 or j != 1:
                print(", ", end="")
            print("{}{}".format(i, j), end="")
        else:
            continue

else:
    print("")
