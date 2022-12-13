SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# from string array with [,] to int array
def extract_integers(line):
    array = line
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

def extract_brackets_commas(line):
    list_brackets = []
    for ch in line:
        if ch == "[" or ch == "]" or ch == ",":
            list_brackets.append(ch)
    return list_brackets

# parse it correctly pls
line_1 = None
line_2 = None
pair_no = 1
for line in f:
    if line_1 == None:
        print("pair no: ", pair_no)
        line_1 = line
        int_list_1 = extract_integers(line)
        brackets_list_1 = extract_brackets_commas(line)
        print("int list 1: ", int_list_1, "brackets: ", brackets_list_1)

        list_1 = None
        index_per_lvl = None
        curr_lvl = 0
        for ch in brackets_list_1:
            if ch == "[":
                if list_1 == None:
                    list_1 = []
                    index_per_lvl = [0]
                else:
                    list_1.append([])
                    indices
                    curr_lvl += 1
                indices.append(0)
            pass

        #continue
        break
    elif line_2 == None:
        line_2 = line
        int_list_2 = extract_integers(line)
        brackets_list_2 = extract_brackets_commas(line)
        print("int list 2: ", int_list_2, "brackets: ", brackets_list_2)
        break
    else:
        line_1 = None
        line_2 = None
        pair_no += 1
        #continue
        break



f.close()

# 5217 wrong