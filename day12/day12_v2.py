SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final

class Maze:
    def __init__(self, array):
        self.array = array
        self.S = None
        self.E = None

    def find_char(self, char):
        #print("char: ", char)
        #print("array: ", self.array)
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                if self.array[i][j] == ord(char):
                    #print(char, j, i)
                    return [j, i]

    def setS(self):
        self.S = Maze.find_char(self, "S")
    
    def setE(self):
        self.E = Maze.find_char(self, "E")

class Node:
    def __init__(self, x_corr, y_corr, parent_node = None):
        self.x_corr = x_corr
        self.y_corr = y_corr
        self.parent_node = parent_node

    def check_up(self, Maze):
        if self.y_corr - 1 >= 0:
            pass
            if Maze.array[self.y_corr][self.x_corr]
        else:
            return None

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
    maze.array.append(line)
f.close()

print("\nmaze:")
for i in maze.array:
    print(i)

# set coordinates of S and E in maze
maze.setS()
maze.setE()
print("maze.S[0]: ", maze.S[0], " maze.S[1]: ", maze.S[1])
#print("maze.S: ", maze.S, " maze.E: ", maze.E)
start_node = Node(maze.S[0], maze.S[1])
#while