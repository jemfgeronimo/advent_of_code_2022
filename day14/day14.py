SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

rockmap = []
for i in range(600)
    
    rockmap.append([])
for line in f:
    line = line.strip().split()
    #print(line)

    prev_e = line[0]
    for e in line:
        if e == "->":
            continue
        e = eval(e)
        if e[0] != prev_e[0]:
            pass
            for i in range(prev_e[0], e[0]+1):
                rockmap[e[1]][i]
        if e[1] != prev_e[1]:
            pass
            for i in range(prev_e[1], e[1]+1):
                rockmap[i][e[0]]
        
            #for 
        

        

f.close()

for i in rockmap:
    print(i)