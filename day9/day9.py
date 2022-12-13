class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

    def update_pos(self, x=0, y=0):
        if self.parent == None:
            self.x += x
            self.y += y
        else:
            if self.x not in range(self.parent.x - 1, self.parent.x + 2) or self.y not in range(self.parent.y - 1, self.parent.y + 2):
                if self.parent.x > self.x:
                    self.x += 1
                elif self.parent.x < self.x:
                    self.x -= 1
                if self.parent.y > self.y:
                    self.y += 1
                elif self.parent.y < self.y:
                    self.y -= 1

# bottom to top, left to right
# U 483 D 512 R 508 L 497
# -29 rows, 11 col
row = []
grid_checklist = []
for j in range(6000):
    row = []
    for i in range(6000):
        row.append(0)
    grid_checklist.append(row)
#print("grid_checklist: ", grid_checklist)
pre_total = 0
for i in range(6000):
    for j in range(6000):
        pre_total += grid_checklist[i][j]
#print("grid_checklist: ", grid_checklist)

head = Node(3000, 3050)
tail = []
#no_tails = 9
no_tails = 1
for i in range(no_tails):
    tail.append(Node(3000, 3050))
    if i == 0:
        tail[i].parent = head
    else:
        tail[i].parent = tail[i-1]
f = open("input.txt")

for line in f:
    line = line.split()
    dir = line[0]
    dis = int(line[1])
    print("line: ", line)
    print("dis: ", dis)
    for i in range(0, dis):
        if dir == "U":
            head.update_pos(0, 1)
        elif dir == "R":
            head.update_pos(1,0)
        elif dir == "D":
            head.update_pos(0,-1)
        elif dir == "L":
            head.update_pos(-1,0)
        for j in range(no_tails):
            tail[j].update_pos()
        #print("head.x: ", head.x, " head.y: ", head.y, end = " ")
        #print("tail.x: ", tail.x, " tail.y: ", tail.y)
        #if head.x < 0  or tail.x < 0 or head.y < 0 or tail.y < 0:
        #    print("break")
        #    break
        grid_checklist[tail[no_tails-1].y][tail[no_tails-1].x] = 1
    #break # debug
    #if head.x < 0  or tail.x < 0 or head.y < 0 or tail.y < 0:
    #    print("break")
    #    break

f.close()

total = 0
for i in range(6000):
    for j in range(6000):
        num = grid_checklist[i][j]
        total += num
        if num == 1:
            pass
            #print("i, j: ", i, j)
print("pre total: ", pre_total)
print("total: ", total)
#print("grid_checklist: ", grid_checklist)
print("grid_checklist[3050][3000]: ", grid_checklist[3050][3000])
# wrong: 2154000
# correct_1: 6470
# correct_2: 2658