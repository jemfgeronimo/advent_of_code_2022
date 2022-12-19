import os
import math
os.system("cls")
SAMPLE_INPUT_ON = 0 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

def computeManhattanDistance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

# create list of sensors and beacons with manhattan distance
sensors = []
beacons = []
sensor_manhattans = []
for line in f:
    # convert string line to list of 4 integers [sensor_x, sensor_y, beacon_x, beacon_y]
    line = line.strip().split()
    line = [line[2].strip(","), line[3].strip(":"), line[-2].strip(","), line[-1]]
    [sensor_x, sensor_y, beacon_x, beacon_y] = [int(str[2:]) for str in line]
    sensor = (sensor_x, sensor_y)
    beacon = (beacon_x, beacon_y)
    sensor_manhattan = (sensor_x, sensor_y, computeManhattanDistance(sensor, beacon))
    sensors.append(sensor)
    beacons.append(beacon)
    sensor_manhattans.append(sensor_manhattan)
f.close()
#print("sensor with manhattan:", sensor_manhattans)

if SAMPLE_INPUT_ON == 1:
    max_range = 20
else:
    max_range = 4000000

#create beacon zone from sensor and manhattan distance
beacon_zone = set()
for sensor_manhattan in sensor_manhattans:
    (sensor_x, sensor_y, manhattan_dist) = sensor_manhattan
    print("creating beacon zone from sensor:", sensor_manhattan)
    from_y_range = sensor_y - manhattan_dist - 1
    to_y_range = sensor_y + manhattan_dist + 1
    x1 = sensor_x
    x2 = sensor_x
    #print("sensor:", sensor_manhattan)
    for i in range(from_y_range, to_y_range + 1):
        #print(x1, i)
        #print(x2, i)
        if x1 >= 0  and x1 <= max_range and i >= 0 and i <= max_range:
            beacon_zone.add((x1, i))
        if x2 >= 0  and x2 <= max_range and i >= 0 and i <= max_range:
            beacon_zone.add((x2, i))
        if i < sensor_y:
            x1 -= 1
            x2 += 1
        else:
            x1 += 1
            x2 -= 1

for spot in list(beacon_zone):
    #print("beacon zone on spot:", spot)
    for sensor_manhattan in sensor_manhattans:
        (sensor_x, sensor_y, manhattan_dist) = sensor_manhattan
        #print("spot:", spot)
        #print("sensor:", sensor_manhattan)
        spot_manhattan = computeManhattanDistance((sensor_x, sensor_y), spot)
        #print("dist of spot:", spot_manhattan)
        if spot_manhattan <= manhattan_dist:
            break
    else:
        beacon_coor = spot
        break

#print("beacon zone:", beacon_zone)
print("beacon:", beacon_coor)

