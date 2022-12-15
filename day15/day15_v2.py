import os
import math
os.system("cls")
SAMPLE_INPUT_ON = 0 # if 1, code is for SAMPLE_INPUT_ON, else, final
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
    xmax = max(x1,x2)
    xmin = min(x1,x2)
    zone = set()
    for i in range(xmin, xmax+1):
        coor = (i, y)
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

if SAMPLE_INPUT_ON == 1:
    y = 10
else:
    y = 2000000
no_beacon_zone = set()
for sensor in sensors:
    # create no beacon zone per beacon
    zone = noBeaconZone(sensor, beacons[sensors.index(sensor)], y, no_beacon_zone)
    no_beacon_zone = no_beacon_zone.union(zone)
    print("sensor: ", sensor)
# remove all existing beacons
no_beacon_zone = no_beacon_zone.difference(beacons)
#print(no_beacon_zone)
# count elements in set
no_beacon_spots = len(no_beacon_zone)
print(no_beacon_spots)
# 5100463