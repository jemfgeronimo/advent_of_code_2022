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
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        # borders
        # top and bottom borders
        if row == 0 or row == NUM_ROWS - 1:
            count += 1
        # side borders
        elif col == 0 or col == NUM_COLS - 1:
            count += 1
        else:
            # check top
            for i in range(row):
                if input_grid[i][col] >= input_grid[row][col]: # not vis
                    break
            else:
                count += 1
                continue
            # check right
            for i in range (col+1, NUM_COLS):
                if input_grid[row][i] >= input_grid[row][col]:
                    break
            else:
                count += 1
                continue
            # check below
            for i in range(row+1, NUM_ROWS):
                if input_grid[i][col] >= input_grid[row][col]:
                    break
            else:
                count += 1
                continue
            # check left
            for i in range(col):
                if input_grid[row][i] >= input_grid[row][col]:
                    break
            else:
                count += 1
                continue
            


print("count: ", count)