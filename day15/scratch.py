line = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n"
print(line)

# convert string line to list of 4 integers [sensor_x, sensor_y, beacon_x, beacon_y]
line = line.strip().split()
line = [line[2].strip(","), line[3].strip(":"), line[-2].strip(","), line[-1]]
line = [int(str[2:]) for str in line]
print(line)