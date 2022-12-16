import os
import math
os.system("cls")
SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# not used
def computeManhattanDistance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
def noBeaconsAllowed(sensor, beacon, point):
    return computeManhattanDistance(sensor, point) < computeManhattanDistance(sensor, beacon)

def noBeaconZone(sensor: tuple, beacon: tuple, y, no_beacon_zone):
    (sensor_x, sensor_y) = sensor
    (beacon_x, beacon_y) = beacon
    x1 = sensor_x - (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) - abs(sensor_y - y))
    x2 = sensor_x + (abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y) - abs(sensor_y - y))
    xmax = max(x1,x2,0)
    xmin = max(min(x1,x2),0)
    zone = set()
    for i in range(xmin, xmax+1):
        coor = (i, y)
        #if coor == (14,11):
        #    return (14,11)
        if coor not in no_beacon_zone:
            zone.add(coor)
    return zone


sensors = []
beacons = []
for line in f:
    # convert string line to list of 4 integers [sensor_x, sensor_y, beacon_x, beacon_y]
    line = line.strip().split()
    line = [line[2].strip(","), line[3].strip(":"), line[-2].strip(","), line[-1]]
    [sensor_x, sensor_y, beacon_x, beacon_y] = [int(str[2:]) for str in line]
    sensor = (sensor_x, sensor_y)
    beacon = (beacon_x, beacon_y)
    sensors.append(sensor)
    beacons.append(beacon)
f.close()

#print(sensors)
#print(type(sensors))
#print(type(sensors[0]))
#print(beacons)
#print(type(beacons))
#print(type(beacons[0]))

no_beacon_zone = set()
if SAMPLE_INPUT_ON == 1:
    min_range = 0
    max_range = 20
else:
    min_range = 0
    max_range = 4000000
valid_zone = set()
for i in range(min_range, max_range + 1):
    for j in range(min_range, max_range + 1):
        print((i,j))
        valid_zone.add((i,j))
for y in range(min_range, max_range + 1):
    print("y: ", y)
    for sensor in sensors:
        # create no beacon zone per beacon
        print("sensor: ", sensor)
        zone = noBeaconZone(sensor, beacons[sensors.index(sensor)], y, no_beacon_zone)
    #    if zone == (14,11):
    #        break
        print("zone: ", zone)
        no_beacon_zone = no_beacon_zone.union(zone)
    #if zone == (14,11):
    #    break
# remove all existing beacons
print(len(no_beacon_zone))
print(len(beacons))
#no_beacon_zone = no_beacon_zone.intersection(valid_zone)
no_beacon_zone = no_beacon_zone.difference(beacons)
#print(no_beacon_zone)
# reveal beacon zone
beacon_zone = valid_zone.difference(no_beacon_zone)
beacon_zone = beacon_zone.difference(beacons)
print(beacon_zone)

# 