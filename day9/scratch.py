D = 0
U = 0
R = 0
L = 0

f = open("input.txt")
for line in f:
    line = line.split()
    if line[0] == "D":
        D += int(line[1])
    elif line[0] == "U":
        U += int(line[1])
    elif line[0] == "R":
        R += int(line[1])
    elif line[0] == "L":
        L += int(line[1])
f.close()

print("D: ", D)
print("U: ", U)
print("L: ", L)
print("R: ", R)


#D:  1879
#U:  1663
# y = -216
#L:  1663
#R:  1630
# x = -33

#D:  2961
#U:  2914
# y = -47
#L:  2779
#R:  3038
# x = 259