import os
import math
os.system("cls")
SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

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