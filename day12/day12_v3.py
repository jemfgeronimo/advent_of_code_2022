SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

hmap = []
for line in f:
    hmap.append([ord(ch) for ch in line.strip()])
    #print(line)

    for i in hmap[-1]:
        if i == ord("S"):
            S_xcorr = hmap[-1].index(i)
            S_ycorr = len(hmap) - 1
            hmap[S_ycorr][S_xcorr] = ord("a")
        elif i == ord("E"):
            E_xcorr = hmap[-1].index(i)
            E_ycorr = len(hmap) - 1
            hmap[S_ycorr][S_xcorr] = ord("z")
f.close()

#for i in hmap:
#    print(i)

# get S and E coordinates
#print("S: ", S_xcorr, S_ycorr)
#print("E: ", E_xcorr, E_ycorr)