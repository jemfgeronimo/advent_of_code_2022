f = open("input.txt")
for line in f:
    pass
packet = ""
n = 14 - 1
for i in range(n,len(line)):
    duplicate = 0
    packet = line[i-n:i+1]
    print("packet: ", packet)
    for j in range(n):
        print("packet[j]: ", packet[j])
        print("packet[j+1:len(packet)-1]", packet[j+1:len(packet)])
        if packet[j] in packet[j+1:len(packet)]:
            duplicate = 1
            break
    #print("duplicate: ", duplicate)
    if duplicate == 1:
        continue
    else:
        break
print("index: ", i+1) # 1850 should be
f.close()