import os
import math
os.system("cls")
SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
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

def isInSensor_sBeaconZone(coor: tuple, sensor_manhattan):
    (sensor_x, sensor_y, manhattan_distance) = sensor_manhattan
    (coor_x, coor_y) = coor
    print(coor)

    top_range = sensor_y - manhattan_distance
    bot_range = sensor_y + manhattan_distance
    left_range = sensor_x - manhattan_distance
    right_range = sensor_x + manhattan_distance

    upper_right_line = (sensor_y - top_range) * (coor_x - right_range) / (right_range - sensor_x) + sensor_y    
    print(upper_right_line)
    lower_right_line = (sensor_y - bot_range) * (coor_x - right_range) / (right_range - sensor_x) + sensor_y
    print(lower_right_line)
    lower_left_line = (bot_range - sensor_y) * (coor_x - sensor_x) / (sensor_y - left_range) + bot_range
    print(lower_left_line)
    upper_left_line = (top_range - sensor_y) * (coor_x - sensor_x) / (sensor_x - left_range) + bot_range
    print(upper_left_line)

    if coor_y >= upper_right_line and coor_y <= lower_right_line and coor_y <= lower_left_line and coor_y >= upper_left_line:
        return True
    return False

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

if SAMPLE_INPUT_ON == 1:
    #y = 10
    max_range = 20
else:
    #y = 2000000
    max_range = 4000000
no_beacon_zone = set()
found_beacon = False
for i in range(max_range + 1):
    for j in range(max_range + 1):
        for sensor_manhattan in sensor_manhattans:
            print(sensor_manhattan)
            if isInSensor_sBeaconZone((j, i), sensor_manhattan):
                print("add here")
                no_beacon_zone.add((j,i))
                break
        else:
            found_beacon = True
            beacon_coor = (j,i)
        if found_beacon == True:
            break
    if found_beacon == True:
        break


print("no beacone zone:", no_beacon_zone)

# tuning freq
print("beacon found:", beacon_coor)
tuning_freq = beacon_coor[0] * 4000000 + beacon_coor[1]
print("tuning freq:", tuning_freq)

