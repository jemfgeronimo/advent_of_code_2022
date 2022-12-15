SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# parse input to easier input format
# + extract min and max values of virtual plane
# + extract size of virtual plane
xmin = None
xmax = None
ymin = None
ymax = None
input = []
for line in f:
    # convert string line to list of 4 integers [sensor_x, sensor_y, beacon_x, beacon_y]
    line = line.strip().split()
    line = [line[2].strip(","), line[3].strip(":"), line[-2].strip(","), line[-1]]
    line = [int(str[2:]) for str in line]

    # min/max values of plane
    if xmin == None:
        xmin = min(line[0], line[2])
    else:
        xmin = min(line[0], line[2], xmin)
    if xmax == None:
        xmax = max(line[0], line[2])
    else:
        xmax = max(line[0], line[2], xmax)
    if ymin == None:
        ymin = min(line[1], line[3])
    else:
        ymin = min(line[1], line[3], ymin)
    if ymax == None:
        ymax = max(line[1], line[3])
    else:
        ymax = max(line[1], line[3], ymax)

    input.append(line)
f.close()
# size of virtual plane
NUM_COLS = xmax - min(xmin, 0)
NUM_ROWS = ymax - min(ymin, 0)
print(NUM_COLS, NUM_ROWS)
print(ymin)
#print(input)