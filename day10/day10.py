#f = open("sample.txt", "r")
f = open("input.txt", "r")
current_cycle = 1
X = 1
checkpoint = 20
sum_sig_str = 0


for line in f:
    # during
    line = line.split()
    cmd = line[0]

    # during 1st cyc
    if current_cycle==checkpoint and checkpoint <= 220:
        sig_str = (current_cycle)*(X)
        print("sig_str: ", sig_str)
        sum_sig_str += sig_str
        print("sum sig str: ", sum_sig_str)
        checkpoint += 40
    print("X during ", current_cycle, "th cycle: ", X)
    # end 1st cyc
    current_cycle += 1

    if cmd == "addx":
        # during 2nd cyc
        if current_cycle==checkpoint and checkpoint <= 220:
            sig_str = (current_cycle)*(X)
            print("sig_str: ", sig_str)
            sum_sig_str += sig_str
            print("sum sig str: ", sum_sig_str)
            checkpoint += 40
        print("X during ", current_cycle, "th cycle: ", X) 

        # end 2nd cyc
        value = int(line[1])
        X += value
        current_cycle += 1
           
f.close()
 
print("sum signal strenght: ", sum_sig_str)