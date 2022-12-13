sum = 0
elf_index = 0
elf_max1 = 0
elf_max2 = 0
elf_max3 = 0
max1 = 0
max2 = 0
max3 = 0
cal = 0
max_line = 0
i = 0

f = open("input.txt")
for line in f:
    if line != "\n":
        cal = int(line)
        sum += cal
    else:
        if (sum > max1):
            max3 = max2
            max2 = max1
            max1 = sum
            elf_max3 = elf_max2
            elf_max2 = elf_max1
            elf_max1 = elf_index
            print("i: ", i)
        elif (sum > max2):
            max3 = max2
            max2 = sum
            elf_max3 = elf_max2
            elf_max2 = elf_index
            print("i: ", i)
        elif (sum > max3):
            max3 = sum
            elf_max3 = elf_index
            print("i: ", i)
        sum = 0
        elf_index = elf_index + 1
    i += 1
f.close()
print()
print("max cals: ", max1, max2, max3)
print("elves: ", elf_max1, elf_max2, elf_max3)
print("last line: ", max_line)
print("total cal: ", max1 + max2 + max3)