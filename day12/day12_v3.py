SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

hmap = []
for line in f:
    hmap.append([ord(ch) for ch in line.strip()])
    #print(line)

    for i in hmap[-1]:
        if i == ord("S"):
            S_xcorr = hmap[-1].index(i)
            S_ycorr = len(hmap) - 1
            #print(S_xcorr, S_ycorr)
            hmap[S_ycorr][S_xcorr] = ord("a")
        elif i == ord("E"):
            E_xcorr = hmap[-1].index(i)
            E_ycorr = len(hmap) - 1
            hmap[E_ycorr][E_xcorr] = ord("z")
f.close()

#for i in hmap:
#    print(i)
class Cell:
    def __init__(self, x_corr, y_corr):
        self.x_corr = x_corr
        self.y_corr = y_corr

# get S and E coordinates
#print("S: ", S_xcorr, S_ycorr)
#print("E: ", E_xcorr, E_ycorr)

NUM_ROWS = len(hmap)
NUM_COLS = len(hmap[0])
step = 0
q1 = [[S_xcorr, S_ycorr]]
q2 = []
q3 = [1]
q4 = [1]
curr_corr = [S_xcorr, S_ycorr]
while([E_xcorr, E_ycorr] not in q1):
#for i in range(5):
    q2.append(q1.pop(0))
    curr_corr = q2[-1]
    curr_height = hmap[curr_corr[1]][curr_corr[0]]
    no_eligible_cell = 0

    # check up
    if curr_corr[1] - 1 >= 0:   ## is there a cell in that direction?
        next_corr = [curr_corr[0], curr_corr[1] - 1] ##
        next_height = hmap[next_corr[1]][next_corr[0]]
        if next_height <= curr_height + 1 and next_corr not in q1 and next_corr not in q2: # is that cell eligible? and not yet in q1 and q2
            q1.append(next_corr)
            no_eligible_cell += 1
    # check right
    if curr_corr[0] + 1 < NUM_COLS:   ## is there a cell in that direction?
        next_corr = [curr_corr[0] + 1, curr_corr[1]] ##
        next_height = hmap[next_corr[1]][next_corr[0]]
        if next_height <= curr_height + 1 and next_corr not in q1 and next_corr not in q2: # is that cell eligible? and not yet in q1 and q2
            q1.append(next_corr)
            no_eligible_cell += 1
    # check down
    if curr_corr[1] + 1 < NUM_ROWS:   ## is there a cell in that direction?
        next_corr = [curr_corr[0], curr_corr[1] + 1] ##
        next_height = hmap[next_corr[1]][next_corr[0]]
        if next_height <= curr_height + 1 and next_corr not in q1 and next_corr not in q2: # is that cell eligible? and not yet in q1 and q2
            q1.append(next_corr)
            no_eligible_cell += 1
    # check left
    if curr_corr[0] - 1 >= 0:   ## is there a cell in that direction?
        next_corr = [curr_corr[0] - 1, curr_corr[1]] ##
        next_height = hmap[next_corr[1]][next_corr[0]]
        if next_height <= curr_height + 1 and next_corr not in q1 and next_corr not in q2: # is that cell eligible? and not yet in q1 and q2
            q1.append(next_corr)
            no_eligible_cell += 1
    print("no_eligible_cell: ", no_eligible_cell)
    if no_eligible_cell != 0:
        q3.append(no_eligible_cell)
        q4.append(no_eligible_cell)
    q3[0] -= 1
    if q3[0] == 0:
        step += 1
        q3.pop(0)
    print("step: ", step)
    print("q1: ", q1)
    print("q2: ", q2)
    print("q3: ", q3)
    print("q4: ", q4)

print("S: ", S_xcorr, S_ycorr)
print("E: ", E_xcorr, E_ycorr)