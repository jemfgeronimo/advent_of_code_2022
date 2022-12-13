SAMPLE_INPUT_ON = 0 # if 1, code is for SAMPLE_INPUT_ON, else, final

def parse_fix_list(array):
    array = array.strip()
    # turn into array of characters
    array = [ch for ch in array]
    # remove unneccessary characters ([,],,)
    while "[" in array:
        array.remove("[")
    while "]" in array:
        array.remove("]")
    while "," in array:
        array.remove(",")
    return [int(ch) for ch in array]

def parse_no_numbers(line_1):
    line_1 = [ch for ch in line_1]
    while "," in line_1:
        line_1.remove(",")
    return [ord(ch) for ch in line_1]

if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

list_1 = None
list_2 = None
pair_no = 1
sum = 0
for line in f:
    pass

    # distribute lists
    if list_1 == None:
        line_1 = line
        list_1 = parse_fix_list(line)
        continue
    elif list_2 == None:
        line_2 = line
        list_2 = parse_fix_list(line)
    else:
        list_1 = None
        list_2 = None
        pair_no += 1
        continue

    # compare
    # length per list
    len_list_1 = len(list_1)
    len_list_2 = len(list_2)
    # cases:
    # case 1: both nonempty lists
    if len_list_1 > 0 and len_list_2 > 0:
        pass
        num_iters = len_list_2
        if len_list_1 < len_list_2:
            num_iters = len_list_1
        for i in range(num_iters):
            # find wrong
            if list_1[i] < list_2[i]: # correct
                print("pair_no: ", pair_no)
                sum += pair_no
                break
            elif list_1[i] == list_2[i]:
                continue
            else:
                break
        else: # all equal so far
            if num_iters == len_list_1: # but 1st list should be shorter
                print("pair_no: ", pair_no)
                sum += pair_no

    # case 2: both empty lists
    elif len_list_1 == 0 and len_list_2 == 0:
        pass
        # check for [ and ]
        # remove ,
        list_1 = parse_no_numbers(line_1)
        list_2 = parse_no_numbers(line_2)
        len_list_1 = len(line_1)
        len_list_2 = len(line_2)
        num_iters = len_list_2
        if len_list_1 < len_list_2:
            num_iters = len_list_1
        for i in range(num_iters):
            # find wrong
            #[:  91
            #]:  93
            if list_1[i] > list_2[i]: # correct
                print("pair_no: ", pair_no)
                sum += pair_no
                break
            elif list_1[i] == list_2[i]:
                continue
            else:
                break
        else: # all equal so far
            if num_iters == len_list_1: # but 1st list should be shorter
                print("pair_no: ", pair_no)
                sum += pair_no
    # case 3: hetero lists
    elif len_list_1 == 0 or len_list_2 == 0:
        if len_list_1 == 0:
            print("pair_no: ", pair_no)
            sum += pair_no
        pass
    #print("list 1: ", list_1, "\tlist 2: ", list_2)
    
f.close()

print("sum: ", sum)

# 5217 wrong