f = open("input.txt")
total = 0
for line in f:
    common = ""
    #print(len(line), ": ", line)
    line_length = len(line) - 1
    line_length_half = int(line_length/2)
    #print(line_length, ": ", line)
    #print("line_length/2 - 1 = ", line_length/2 - 1)
    rucksack_1 = line[0 : int(line_length/2)]
    rucksack_2 = line[int(line_length/2) : line_length]
    print("rucksack1: ", rucksack_1, " rucksack_2: ", rucksack_2)
    print("r1len: ", len(rucksack_1), " r2len: ", len(rucksack_2))

    for ch in rucksack_1:
        if ch in rucksack_2 and ch not in common:
            common += ch

    #for i in range(0,len(rucksack_1)):
    #    if i
    #    for j in range(0, len(rucksack_2)):
    #        if rucksack_1[i] == rucksack_2[j]:
    #            #common.append(rucksack_1[i])
    #            if rucksack_1[i] not in common:
    #                common += rucksack_1[i]
    print("common: ", common)
    for ch in common:
        if ch >= "a" and ch <= "z":
            #print("lowercase")
            print("equivalent: ", ord(ch[0]) - ord('a') + 1)
            total += (ord(ch[0]) - ord('a') + 1)
        else:
            #print("uppercase")
            print("equivalent: ", ord(ch[0]) - ord('A') + 27)
            total += (ord(ch[0]) - ord('A') + 27)
        print("total: ", total)
f.close()
#print("total: ", total)