SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final
if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

# 1 correct
# 0 go on
# -1 incorrect


def compare_ints(int_1, int_2):
    if int_1 < int_2:
        return 1
    elif int_1 > int_2:
        return -1
    return 0

def compare_lists(list_1, list_2):
    len_1 = len(list_1)
    len_2 = len(list_2)
    min = len_1
    if len_2 < min:
        min = len_2
    for i in range(min):
        # find wrong
        elem_1 = list_1[i]
        elem_2 = list_2[i]
        type_1 = type(elem_1)
        type_2 = type(elem_2)
        if type_1 == type_2:
            if type_1 is list:
                res = compare_lists(elem_1, elem_2)
                if res == 0:
                    continue
                return res
            else:
                res = compare_ints(elem_1, elem_2)
                if res == 0:
                    continue
                return res                     
        else:
            if type_1 is list:
                res = compare_lists(elem_1, [elem_2])
                if res == 0:
                    continue
                return res
            else:
                res = compare_lists([elem_1], elem_2)
                if res == 0:
                    continue
                return res
    else:   # nothing wrong yet
        if len_1 < len_2:
            return 1
        elif len_1 > len_2:
            return -1
        return 0


list_1 = None
list_2 = None
no_pair = 1
sum = 0
for line in f:
    if list_1 == None:
        list_1 = eval(line.strip())
        continue
    elif list_2 == None:
        list_2 = eval(line.strip())
    else:
        list_1 = None
        list_2 = None
        no_pair += 1
        continue
    #print(list_1, list_2)
    if compare_lists(list_1, list_2) == 1:
        print("correct pair: ", no_pair)
        sum += no_pair
        #print("it is correct")
        pass
    else:
        #print("it is wrong")
        pass
    #break

f.close()

print("sum: ", sum)
# 5217 wrong
# 6070 right