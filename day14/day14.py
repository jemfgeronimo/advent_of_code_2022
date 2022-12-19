SAMPLE_INPUT_ON = 0 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

rockmap = []
#for i in range(600)
#    
#    rockmap.append([])
for line in f:
    line = line.strip().split() # list of string in form ["498,4", "->", ]    
    while "->" in line: # remove "->"
        line.remove("->")
    line = [eval(ch) for ch in line]    # list of tuples in form [[498,4],etc.]
    #print(line)
    for pair in line:
        if pair[0] > max_cols:
            max_cols = pair[0]
        if pair[1] > max_rows:
            max_rows = pair[1]
    input.append(line)
f.close()
NUM_ROWS = max_rows + 1
NUM_COLS = max_cols + 1
print(NUM_COLS, NUM_ROWS)
#print(input[1])

# create initial rockmap
#NUM_ROWS = 2 + 1
#NUM_COLS = 3 + 1
# rockmap with no rocks yet
rockmap = []
for i in range(NUM_ROWS):
    rockmap.append([])
    for j in range(NUM_COLS):
        rockmap[i].append(".")
#print(rockmap)
# put rocks in rockmap
for line in input:
    prev_pair = None
    for pair in line:
        if prev_pair != None:
            if prev_pair[0] == pair[0]:
                max_range = max(prev_pair[1], pair[1])
                min_range = min(prev_pair[1], pair[1])
                for i in range(min_range, max_range+1):
                    rockmap[i][pair[0]] = "#"
            if prev_pair[1] == pair[1]:
                max_range = max(prev_pair[0], pair[0])
                min_range = min(prev_pair[0], pair[0])
                for i in range(min_range, max_range+1):
                    rockmap[pair[1]][i] = "#"
        prev_pair = pair

# drop while stop condition is not met - TODO
abyss = 0
no_of_sands = 0
while abyss == 0:
#for i in range(2):
    stop = 0
    curr_coor = (500,0)
    while stop == 0:
        if curr_coor[1] + 1 < NUM_ROWS:
            below_coor = (curr_coor[0], curr_coor[1] + 1)
            if curr_coor[0] - 1 >= 0:
                below_left_coor = (curr_coor[0] - 1, curr_coor[1] + 1)
            else:
                below_left_coor = None
            if curr_coor[0] + 1 < NUM_COLS:
                below_right_coor = (curr_coor[0] + 1, curr_coor[1] + 1)
            else:
                below_right_coor = None
        else:
            below_coor = None
            below_left_coor = None
            below_right_coor = None
            abyss = 1

        if any(x == None for x in [below_coor, below_left_coor, below_right_coor]):
            abyss = 1
            stop = 1
        else:           
            # check below
            below = rockmap[below_coor[1]][below_coor[0]]
            below_left = rockmap[below_left_coor[1]][below_left_coor[0]]
            below_right = rockmap[below_right_coor[1]][below_right_coor[0]]
            if below not in ["#", "o"]:
                curr_coor = below_coor
                stop = 0
            # check left below
            elif  below_left not in ["#", "o"]:
                curr_coor = below_left_coor
                stop = 0
            elif  below_right not in ["#", "o"]:
                curr_coor = below_right_coor
                stop = 0
            else:
                stop = 1
    if abyss == 0:
        rockmap[curr_coor[1]][curr_coor[0]] = "o"
        no_of_sands += 1


# debugger: print rockmap in x[490-NUM_ROWS]
#print(rockmap[:20][490:-1])
for i in range(NUM_ROWS):
    print(rockmap[i][490:])
print("no. of sands: ", no_of_sands)