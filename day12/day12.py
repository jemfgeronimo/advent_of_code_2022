SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final

if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

maze = []
for line in f:
    line = line.split()[0]
    maze.append(line)
f.close()

for line in maze:
    print(line)

#curr_x = 0
#curr_y = 0
NO_ROWS = len(maze)
NO_COLS = len(maze[0])
# coordinate system
# (0,0) (1,0) (2,0)
#print("rows: ", len(maze))
#print("cols: ", len(maze[0]))

path_grid = []
for i in range(NO_ROWS):
    path_grid.append([])
    for j in range(NO_COLS):
        path_grid[i].append(".")
        if maze[i][j] == "S":
            curr_x = j
            curr_y = i

print("curr_x: ", curr_x)
print("curr_y: ", curr_y)

#print("\npath_grid:")
#for line in path_grid:
#    print(line)

curr_cell = maze[curr_y][curr_x]
while(curr_cell != "E"):
#for itr in range(20):
    for line in path_grid:
        for ch in line:
            print(ch, end="")
        print()
    curr_cell = maze[curr_y][curr_x]
    if curr_cell == "S":
        curr_cell = "a"
    print("curr_cell: ", curr_cell, "curr_x: ", curr_x, "curr_y: ", curr_y)
    max = chr(0)
    # check up
    if curr_y - 1 >= 0 and path_grid[curr_y-1][curr_x] == ".":   #
        next_cell = maze[curr_y-1][curr_x]  #
        if  next_cell >= max and ord(next_cell) - ord(curr_cell) <= 1:
            max = next_cell
            path_grid[curr_y][curr_x] = "^" #
    # check down
    if curr_y + 1 < NO_ROWS and path_grid[curr_y+1][curr_x] == ".": #
        next_cell = maze[curr_y+1][curr_x] #
        if  next_cell >= max and ord(next_cell) - ord(curr_cell) <= 1:
            max = next_cell
            path_grid[curr_y][curr_x] = "v" #
    # check right
    if curr_x + 1 < NO_COLS and path_grid[curr_y][curr_x+1] == ".":#
        next_cell = maze[curr_y][curr_x+1]#
        if  next_cell >= max and ord(next_cell) - ord(curr_cell) <= 1:
            max = next_cell
            path_grid[curr_y][curr_x] = ">"#
    # check left
    if curr_x - 1 >= 0 and path_grid[curr_y][curr_x-1] == ".":#
        next_cell = maze[curr_y][curr_x-1]#
        if  next_cell >= max and ord(next_cell) - ord(curr_cell) <= 1:
            max = next_cell
            path_grid[curr_y][curr_x] = "<"#

    if path_grid[curr_y][curr_x] == "^":
        curr_y -= 1
    elif path_grid[curr_y][curr_x] == "v":
        curr_y += 1
    elif path_grid[curr_y][curr_x] == ">":
        curr_x += 1
    elif path_grid[curr_y][curr_x] == "<":
        curr_x -= 1

#print("\npath_grid:")
#for line in path_grid:
#    print(line)
count = 0
for i in range(NO_ROWS):
    for j in range(NO_COLS):
        if path_grid[i][j] != ".":
            count += 1
print("count: ", count)