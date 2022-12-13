#f = open("sample.txt", "r")
f = open("input.txt", "r")
current_cycle = 1
X = 1
checkpoint = 20
sum_sig_str = 0
screen = []
NUM_ROWS = 6
for i in range(NUM_ROWS):
    screen.append("")

for line in f:
    # during
    line = line.split()
    cmd = line[0]

    # during 1st cyc
    if current_cycle in range(1,41):
        screen_index = 0
    elif current_cycle in range(41,81):
        screen_index = 1
    elif current_cycle in range(81,121):
        screen_index = 2
    elif current_cycle in range(121,161):
        screen_index = 3
    elif current_cycle in range(161,201):
        screen_index = 4
    elif current_cycle in range(201,241):
        screen_index = 5
    if len(screen[screen_index]) in range(X-1, X+2):
        ch = "#"
    else:
        ch = "."
    screen[screen_index] += ch
        

    #1 - 0,1,2 len
    #16 - 15,16,17 len

    # end 1st cyc
    current_cycle += 1

    if cmd == "addx":
        # during 2nd cyc
        if current_cycle in range(1,41):
            screen_index = 0
        elif current_cycle in range(41,81):
            screen_index = 1
        elif current_cycle in range(81,121):
            screen_index = 2
        elif current_cycle in range(121,161):
            screen_index = 3
        elif current_cycle in range(161,201):
            screen_index = 4
        elif current_cycle in range(201,241):
            screen_index = 5
        if len(screen[screen_index]) in range(X-1, X+2):
            ch = "#"
        else:
            ch = "."
        screen[screen_index] += ch

        # end 2nd cyc
        value = int(line[1])
        X += value
        current_cycle += 1
           
f.close()
 
for line in screen:
    print(line)