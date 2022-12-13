#input_grid = []
input_grid = []

f = open("input.txt")
for line in f:
    #print("type(line): ", type(line))
    line = line.split()[0]
    input_grid.append(line)
f.close()

#for i in range()
#print("len(input_grid): ", len(input_grid)) #rows
#print("len(input_grid[0]): ", len(input_grid[0])) #cols
NUM_ROWS = len(input_grid)
NUM_COLS = len(input_grid[0])
count = 0
max_score = 0
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        score = 1
        # borders
        # top and bottom borders
        if row == 0 or row == NUM_ROWS - 1:
            #count += 1
            continue
        # side borders
        elif col == 0 or col == NUM_COLS - 1:
            #count += 1
            continue
        else:
            # check top
            for i in range(row-1,-1,-1):
                if input_grid[i][col] < input_grid[row][col]: # not vis
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0
            # check right
            for i in range (col+1, NUM_COLS):
                if input_grid[row][i] < input_grid[row][col]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0
            # check below
            for i in range(row+1, NUM_ROWS):
                if input_grid[i][col] < input_grid[row][col]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0
            # check left
            for i in range(col-1, -1, -1):
                if input_grid[row][i] < input_grid[row][col]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0

            # update max score
            if score > max_score:
                max_score = score
            


print("max_score: ", max_score)

# 5762400 wrong
# 5568000 wrong