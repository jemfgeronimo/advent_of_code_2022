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

def noBeaconZone(sensor: tuple, beacon: tuple, y, no_beacon_zone, max_range):
    (sensor_x, sensor_y, manhattan_distance) = sensor
    (beacon_x, beacon_y) = beacon
    if (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) - abs(sensor_y - y)) < 0:
        return set()
    x1 = sensor_x - (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) - abs(sensor_y - y))
    x2 = sensor_x + (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) - abs(sensor_y - y))
    xmax = min(max(x1,x2,0),max_range)
    xmin = max(min(x1,x2),0)
    zone = set()
    for i in range(xmin, xmax+1):
        coor = (i, y)
        if coor in no_beacon_zone:
            continue
        zone.add(coor)
    return zone

def createNoBeaconZone(sensor, no_beacon_zone):
    (sensor_x, sensor_y, manhattan_distance) = sensor
    top_range = sensor_y - manhattan_distance
    bot_range = sensor_y + manhattan_distance
    left_range = sensor_x
    right_range = sensor_x
    zone = set()
    for i in range(top_range, bot_range + 1):
        #print("i:", i)
        for j in range(left_range, right_range + 1):
            #print("j:", j)
            print("i:", i, "j:", j)
            if (j,i) not in no_beacon_zone:
                zone.add((j,i))
        if i < sensor_y:
            left_range -= 1
            right_range += 1
        else:
            left_range += 1
            right_range -= 1
    return zone

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

#print(sensors)
#print(type(sensors))
#print(type(sensors[0]))
#print(beacons)
#print(type(beacons))
#print(type(beacons[0]))

#print("sensors: ", sensors)
# sort beacon list based on coordinates
#def coordinateValue(coor):
#    return coor[0] + coor[1]*10
#sensors.sort(key=coordinateValue)
#print("sensors: ", sensors)

# create no beacon zone without restriction
no_beacon_zone = set()
for sensor_manhattan in sensor_manhattans:
    print("sensor: ", sensor_manhattan)
    zone = createNoBeaconZone(sensor_manhattan, no_beacon_zone)
    no_beacon_zone = no_beacon_zone.union(zone)

# create valid zone
if SAMPLE_INPUT_ON == 1:
    #y = 10
    max_range = 20
else:
    #y = 2000000
    max_range = 4000000
valid_zone = set()
for i in range(max_range + 1):
    for j in range(max_range + 1):
        valid_zone.add((i,j))
#print("len of valid zone: ", len(valid_zone))

# create no beacon zone with restriction
no_beacon_zone = no_beacon_zone.intersection(valid_zone)

# show beacon zone
beacon_zone = valid_zone.difference(no_beacon_zone)
print("len of beacon zone: ", len(beacon_zone))
print("beacon zone: ", beacon_zone)

# tuning freq
beacon_coor = list(beacon_zone)[0]
tuning_freq = beacon_coor[0] * 4000000 + beacon_coor[1]
print("tuning freq:", tuning_freq)