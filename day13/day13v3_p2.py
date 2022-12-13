SAMPLE_INPUT_ON = 0 # if 1, code is for SAMPLE_INPUT_ON, else, final
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

# prepare master list
masterlist = []
masterlist.append([[2]])
masterlist.append([[6]])
for line in f:
    if line == "\n":
        continue
    masterlist.append(eval(line.strip()))
f.close()

for listx in masterlist:
    print("list: ", listx)       

fixed_masterlist = []
for listx in masterlist:
    if fixed_masterlist == []:
        fixed_masterlist.append(listx)
        continue
    
    for listy in fixed_masterlist:
        # if listx < listy:
            # continue
        # 

        # if listx < listy:
        if compare_lists(listx, listy) == 1:
            # insert listx
            index = fixed_masterlist.index(listy)
            fixed_masterlist.insert(index, listx)
            break
    else:
        fixed_masterlist.append(listx)

print("FIXED MASTER LIST:")
i = 1
decoder_key = 1
for listx in fixed_masterlist:
    print("list: ", listx)
    if listx == [[2]] or listx == [[6]]:
        decoder_key *= i
    i += 1

print("decoder key: ", decoder_key)