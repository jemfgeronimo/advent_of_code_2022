SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final

class Maze:
    def __init__(self, heightmap):
        self.heightmap = heightmap  # in integers
        self.S = [0, 0]
        self.E = [0, 0]
        self.no_rows = 0
        self.no_cols = 0

    def set_no_rows_cols(self):
        self.no_rows = len(self.heightmap)
        self.no_cols = len(self.heightmap[0])

    def find_height(self, height):
        #print("height: ", height)
        #print("heightmap: ", self.heightmap)
        for i in range(len(self.heightmap)):
            for j in range(len(self.heightmap[i])):
                #if self.heightmap[i][j] == ord(height):
                if self.heightmap[i][j] == height:
                    #print(height, j, i)
                    return [j, i]

    # use before change_height_ES
    def setS(self):
        self.S = Maze.find_height(self, ord("S") - ord("a"))    
    def setE(self):
        self.E = Maze.find_height(self, ord("E") - ord("a"))
    def change_height_ES(self):
        self.heightmap[self.S[1]][self.S[0]] = ord("a") - ord("a")
        self.heightmap[self.E[1]][self.E[0]] = ord("z") - ord("a")

class Node:
    def __init__(self, height, x_corr, y_corr, parent_node = None):
        self.height = height
        self.x_corr = x_corr
        self.y_corr = y_corr
        self.parent_node = parent_node
        self.distance_to_end = 0

    def add_distance_to_end(self):
        self.distance_to_end += 1
        if self.parent_node != None:
            self.parent_node.add_distance_to_end()

def find_end(node, maze, node_list):
    x_corr = node.x_corr
    y_corr = node.y_corr
    #print("maze.E: ", maze.E)
    if maze.E == [x_corr, y_corr]:
        node.add_distance_to_end()
        return 0
    # check up
    if (y_corr - 1 >= 0):   # do upper cell exist?
        next_height = maze.heightmap[y_corr - 1][x_corr]
        # check cell if eligible
        if next_height <= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr, y_corr - 1, node)
            node_list.append(new_node)
            if find_end(new_node, maze, node_list) == 0:
                node_list.pop()
    # check right
    if (x_corr + 1 < maze.no_cols):   # do right cell exist?
        next_height = maze.heightmap[y_corr][x_corr + 1]
        #print("next height: ", type(next_height))
        #print("node height: ", type(node.height))
        # check cell if eligible
        if next_height <= node.height + 1:  # if eligible
            print("ryt hr")
            # create node + find path
            new_node = Node(next_height, x_corr + 1, y_corr, node)
            node_list.append(new_node)
            if find_end(new_node, maze, node_list) == 0:
                node_list.pop()
    # check down
    if (y_corr + 1 < maze.no_rows):   # do lower cell exist?
        next_height = maze.heightmap[y_corr + 1][x_corr]
        # check cell if eligible
        if next_height <= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr, y_corr + 1, node)
            node_list.append(new_node)
            if find_end(new_node, maze, node_list) == 0:
                node_list.pop()
    # check left
    if (x_corr - 1 >= 0 ):   # do left cell exist?
        next_height = maze.heightmap[y_corr][x_corr - 1]
        # check cell if eligible
        if next_height <= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr - 1, y_corr, node)
            node_list.append(new_node)
            if find_end(new_node, maze, node_list) == 0:
                node_list.pop()
    # no path
    return 1

if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# create maze from input
maze = Maze([])
for line in f:
    line = line.strip()
    line = [ord(ch) - ord("a") for ch in line]
    #print("line: ", line)
    maze.heightmap.append(line)
f.close()
# set maze size
maze.set_no_rows_cols()
# set coordinates of S and E in maze
maze.setS()
maze.setE()
# change S and E to a and z
maze.change_height_ES()

print("\nmaze:")
for i in maze.heightmap:
    print(i)

print("maze.S[0]: ", maze.S[0], " maze.S[1]: ", maze.S[1])
print("maze.E[0]: ", maze.E[0], " maze.E[1]: ", maze.E[1])
#print("maze.S: ", maze.S, " maze.E: ", maze.E)

# initialize start node
start_node = Node(ord("a"), maze.S[0], maze.S[1])
node_list = []
find_end(start_node, maze, node_list)
print("node_list: ", node_list)
for node in node_list:
    #print("im here")
    print("node_list: ", node.height)