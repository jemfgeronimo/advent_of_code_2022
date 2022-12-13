sum = 0
elf_index = 0
elf_max = 0
max = 0
cal = 0
max_line = 0
i = 0

f = open("input.txt")
for line in f:
    if line != "\n":
        cal = int(line)
        sum += cal
    else:
        if (sum > max):
            max = sum
            elf_max = elf_index
            print("i: ", i)
        sum = 0
        elf_index = elf_index + 1
    i += 1
f.close()
print()
print("max cal: ", max)
print("elf: ", elf_max)
print("last line: ", max_line)