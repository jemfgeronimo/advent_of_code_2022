#line = "33-62,26-62\n"
#nums_str = ["","","",""]
#nums = [0,0,0,0]

tally = 0
f = open("input.txt")
#str = str.split("-" | "," | "\n")
#str[1] = str[1].split(",")
#print(str)
for line in f:
    nums_str = ["","","",""]
    nums = [0,0,0,0]
    i = 0
    for ch in line:
        #print("ch: ", ch)
        if ch == "-" or ch == "," or ch == "\n":
            i += 1
        else:
            nums_str[i] += ch
    i = 0
    for s in nums_str:
        nums[i] = int(s)
        i += 1
    print("nums: ", nums)
    if (nums[2] > nums[1]) or (nums[0] > nums[3]):
        # does not overlap
        pass
    else:
        print("overlap")
        tally += 1
f.close()

print("tally: ", tally)
#print("nums_str: ", nums_str)
#print("nums: ", nums)
#print("i: ", i)