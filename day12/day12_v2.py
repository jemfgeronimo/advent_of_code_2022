SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final

class Maze:
    def __init__(self, heightmap):
        self.heightmap = heightmap  # in integers
        self.S = None
        self.E = None
        self.no_rows = len(heightmap)
        self.no_cols = len(heightmap[0])

    def find_height(self, height):
        #print("height: ", height)
        #print("heightmap: ", self.heightmap)
        for i in range(len(self.heightmap)):
            for j in range(len(self.heightmap[i])):
                if self.heightmap[i][j] == ord(height):
                    #print(height, j, i)
                    return [j, i]

    def setS(self):
        self.S = Maze.find_height(self, ord("S"))
    
    def setE(self):
        self.E = Maze.find_height(self, ord("E"))

    def change_height_ES(self):
        for i in self.heightmap:
            for j in i:
                if j == ord("S"):
                    i[i.index(j)] = ord("a")
                elif j == ord("E"):
                    i[i.index(j)] = ord("z")

class Node:
    def __init__(self, high_str, x_corr, y_corr, parent_node = None):
        self.high_str = high_str
        self.high_int = ord(high_str)
        self.x_corr = x_corr
        self.y_corr = y_corr
        self.parent_node = parent_node
        self.distance_to_end = 0

    def add_distance_to_end(self):
        self.distance_to_end += 1
        if self.parent_node != None:
            self.parent_node.add_distance_to_end()

def find_path(node, maze, node_list):
    x_corr = node.x_corr
    y_corr = node.y_corr
    if maze.E == [x_corr, y_corr]:
        node.add_distance_to_end() # - TODO HERE
        return
    # check up
    if (y_corr - 1 >= 0):   # do upper cell exist?
        next_height = maze.heightmap[y_corr - 1][x_corr]
        # check cell if eligible
        if next_height >= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr, y_corr - 1, node)
            find_path(new_node, maze)
            node_list.append(new_node)
    # check right
    if (x_corr + 1 < maze.no_cols):   # do right cell exist?
        next_height = maze.heightmap[y_corr][x_corr + 1]
        # check cell if eligible
        if next_height >= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr + 1, y_corr, node)
            find_path(new_node, maze)
            node_list.append(new_node)
    # check down
    if (y_corr + 1 < maze.no_rows):   # do lower cell exist?
        next_height = maze.heightmap[y_corr + 1][x_corr]
        # check cell if eligible
        if next_height >= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr, y_corr + 1, node)
            find_path(new_node, maze)
            node_list.append(new_node)
    # check left
    if (x_corr - 1 >= 0 ):   # do left cell exist?
        next_height = maze.heightmap[y_corr][x_corr - 1]
        # check cell if eligible
        if next_height >= node.height + 1:  # if eligible
            # create node + find path
            new_node = Node(next_height, x_corr - 1, y_corr, node)
            find_path(new_node, maze)
            node_list.append(new_node)
    # u r here

if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# create maze from input
maze = Maze([])
for line in f:
    line = line.strip()
    line = [ord(ch) for ch in line]
    #print("line: ", line)
    maze.heightmap.append(line)
f.close()

print("\nmaze:")
for i in maze.heightmap:
    print(i)

# set coordinates of S and E in maze
maze.setS()
maze.setE()
# change S and E to a and z
maze.change_height_ES()
print("maze.S[0]: ", maze.S[0], " maze.S[1]: ", maze.S[1])
#print("maze.S: ", maze.S, " maze.E: ", maze.E)

# initialize start node
start_node = Node(maze.S[0], maze.S[1])
node_list = []