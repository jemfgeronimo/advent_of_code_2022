elf1 = ""
elf2 = ""
elf3 = ""
common  = ""

f = open("input.txt")
total = 0
for line in f:
    if elf1 == "":
        elf1 = line[0:len(line) - 1]
    else:
        if elf2 == "":
            elf2 = line[0:len(line) - 1]
        else:
            if elf3 == "":
                elf3 = line[0:len(line) - 1]
    if elf1 != "" and elf2 != "" and elf3 != "":
        print("elf1: ", elf1, " elf2: ", elf2, " elf3: ", elf3)
        for ch in elf1:
            if ch in elf2 and ch in elf3 and ch not in common:
                common += ch
        elf1 = ""
        elf2 = "" 
        elf3 = ""

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

        common = ""
    
f.close()
#print("total: ", total)