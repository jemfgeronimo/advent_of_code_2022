import os
import math
os.system("cls")
SAMPLE_INPUT_ON = 0 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")
def noBeaconZone(sensor: tuple, beacon: tuple, y, no_beacon_zone, max_range):
    (sensor_x, sensor_y) = sensor
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
        if coor == (14,11):
            #print("it is sensor =", sensor, "with beacon: ", beacon)
            pass
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
    #y = 10
    max_range = 20
else:
    #y = 2000000
    max_range = 4000000
no_beacon_zone = set()
for y in range(0, max_range+1):
#for y in range(9,10):
    for sensor in sensors:
        # create no beacon zone per beacon
        zone = noBeaconZone(sensor, beacons[sensors.index(sensor)], y, no_beacon_zone, max_range)
        no_beacon_zone = no_beacon_zone.union(zone)
        print("y:", y, "sensor:", sensor)
# remove all existing beacons
no_beacon_zone = no_beacon_zone.union(beacons).union(sensors)
#print("no beacon zone: ", no_beacon_zone)
# count elements in set
#no_beacon_spots = len(no_beacon_zone)
#print("no beacon spots: ", no_beacon_spots)

valid_zone = set()
for i in range(max_range + 1):
    for j in range(max_range + 1):
        valid_zone.add((i,j))
print("len of valid zone: ", len(valid_zone))

beacon_zone = valid_zone.difference(no_beacon_zone)
print("len of beacon zone: ", len(beacon_zone))
print("beacon zone: ", beacon_zone)