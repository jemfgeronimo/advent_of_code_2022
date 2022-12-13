f = open("input.txt")
pile = ["","","","","","","","",""]
i = 0
for line in f:
    if i < 8:
        #print("line: ", line)
        if line[1] != " ": pile[0] = line[1] + pile[0]
        if line[5] != " ": pile[1] = line[5] + pile[1]
        if line[9] != " ": pile[2] = line[9] + pile[2]
        if line[13] != " ": pile[3] = line[13] + pile[3]
        if line[17] != " ": pile[4] = line[17] + pile[4]
        if line[21] != " ": pile[5] = line[21] + pile[5]
        if line[25] != " ": pile[6] = line[25] + pile[6]
        if line[29] != " ": pile[7] = line[29] + pile[7]
        if line[33] != " ": pile[8] = line[33] + pile[8]
        print("pile: ", pile)
    #elif i in [10,11,12]:
    elif i >= 10:
        words = line.split()
        #print("words: ", words)
        nums = [int(words[1]), int(words[3]) - 1, int(words[5]) - 1] # converted na to index
        print("nums: ", nums)
        print("nums[0]: ", nums[0])
        print("nums[1]: ", nums[1])
        print("nums[2]: ", nums[2])
        # nums = [0]how many, [1]from, [2]to

        pile[nums[2]] += pile[nums[1]][-nums[0]:len(pile[nums[1]])]
        print(pile[nums[2]])
        pile[nums[1]] = pile[nums[1]][:-nums[0]]
        print(pile[nums[1]])

        #for j in range(nums[0]):
            #print("j: ", j)
            #print(pile[nums[1]])
            #print(type(pile[nums[1]]))
            #print(type(nums[1]))
        #    pile[nums[2]] = pile[nums[2]] + pile[nums[1]][-1]
        #    print(pile[nums[2]])
        #    pile[nums[1]] = pile[nums[1]][ : -1]
        #    print(pile[nums[1]])

    i += 1

f.close()
print("final pile: ", pile)
