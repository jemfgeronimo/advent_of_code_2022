SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# parse input to easier input format
#for line in f:
for i in range(1):
    line = line.strip()
    line = line.split()
    

f.close()