SAMPLE_INPUT_ON = 1 # if 1, code is for SAMPLE_INPUT_ON, else, final

if SAMPLE_INPUT_ON:
    f = open("sample.txt", "r")
else:
    f = open("input.txt", "r")

class Monkey:
    def __init__(self):
        self.items = []
        self.op = []
        self.div_test = 0
        self.true_monkey_index = 0
        self.false_monkey_index = 0
        self.no_inspection = 0

monkey = []
monkey_index = 0
monkey_inspection_list = []

for line in f:
    line = line.split()
    print(line)

    if line == []:
        print("empty line")
        monkey_index += 1
    elif line[0] == "Monkey":
        monkey.append(Monkey())
        #monkey_inspection_list.append(0)
    elif line[0] == "Starting":
        for item in line:
            if item == "Starting" or item == "items:":
                continue
            else:
                item = item.split(",")
                print("item: ", item)
                monkey[monkey_index].items.append(int(item[0]))
    elif line[0] == "Operation:":
        monkey[monkey_index].op.append(line[4])
        monkey[monkey_index].op.append(line[5])
    elif line[0] == "Test:":
        monkey[monkey_index].div_test = int(line[-1])
    elif line[0] == "If":
        if line[1] == "true:":
            monkey[monkey_index].true_monkey_index = int(line[-1])
        else:
            monkey[monkey_index].false_monkey_index = int(line[-1])
f.close()

print("len(monkey): ", len(monkey))
NUM_MONKEYS = len(monkey)

for i in range(monkey_index + 1):
    #print("i: ", i)
    print("Monkey: ", i)
    print("self.items: ", monkey[i].items)
    print("self.op: ", monkey[i].op)
    print("self.div_test: ", monkey[i].div_test)
    print("self.true_monkey_index: ", monkey[i].true_monkey_index)
    print("self.false_monkey_index: ", monkey[i].false_monkey_index)
# sample
# 1 - 24  = 2 x 12
# 2 - 100 = 10 x 10
# 3 - 224 = 
# 4 - 400 = 20 x 20
# 5 - 624
# 6 - 900 = 30 x 30
# 7 - 1221
# 8 - 1600 = 40 x 40

# true
# 1 - 110 = 11 x 10
# 2 - 400 = 20 x 20
# 3 - 1044 = 36 x 29
# 4 - 1920 = 48 x 40

# 5 - 2912 = 56 x 52
# 6 - 4284 = 68 x 63
# 7 - 5852 = 77 x 76
# 8 - 7920 - 90 x 88
# 2500000000 WRONG
import sys
MAX_VAL = sys.maxsize
NUM_ROUNDS = 10000
for round in range(20):
    for round1 in range(20):
        for round2 in range(25):
            print("\nround: ", round, round1, round2)
            for i in range(NUM_MONKEYS):
                curr_monkey = monkey[i]
                while curr_monkey.items != []:
                    # inspect
                    worry_level = int(curr_monkey.items[0])
                    temp = worry_level
                    # operate
                    if curr_monkey.op[1] == "old":
                        second_operator = worry_level
                    else:
                        second_operator = int(curr_monkey.op[1])
                    if curr_monkey.op[0] == "+":
                        worry_level += second_operator
                        pass
                    else:
                        worry_level *= second_operator
                        pass
                    # divide by 3
                    #worry_level = int(worry_level/3)
                    #2525059796 - 3
                    #2623693275 - 3.03
                    #2703791988 - 3.1
                    #2500200000 - 3.105
                    #2500200000 - 3.11
                    #2500099992 - 3.2
                    # MANAGE WORRY LEVEL
                    #worry_level = worry_level % (10**24)
                    #worry_lebel = worry_level % (10000 * 10 ** NUM_ROUNDS)
                    #worry_level = worry_level % MAX_VAL
                    #worry_level = worry_level % (2**19)
                    # 20 rounds - 10 ^ 24
                    #10000 - [95, 101, 13, 105]
                    #1000 - [93, 103, 15, 107]
                    #100 - [97, 99, 16, 103]
                    # check divisibility
                    if worry_level % curr_monkey.div_test:
                        divisible = False
                    else:
                        divisible = True
                    # throw
                    if divisible:
                        monkey[curr_monkey.true_monkey_index].items.append(worry_level)
                        #monkey[curr_monkey.true_monkey_index].items.append(temp)
                    else:
                        monkey[curr_monkey.false_monkey_index].items.append(worry_level)
                        #monkey[curr_monkey.false_monkey_index].items.append(temp)
                    curr_monkey.items.pop(0)
                    # tally inspection
                    #monkey_inspection_list[i] += 1
                    #if i == 0 or i == 3:
                    curr_monkey.no_inspection += 1
            for i in range(NUM_MONKEYS):
                #print("monkey ", i, "contains: ", monkey[i].items)
                pass

#monkey_inspection_list = []
for i in range(NUM_MONKEYS):
    #print("i: ", i)
    curr_monkey = monkey[i]
    print("Monkey: ", i)
    print("self.items: ", curr_monkey.items)
    print("self.no_inspection: ", curr_monkey.no_inspection)
    monkey_inspection_list.append(curr_monkey.no_inspection)

print("BEFORE monkey_inspection_list: ", monkey_inspection_list)
monkey_inspection_list.sort(reverse=True)
print("monkey_inspection_list: ", monkey_inspection_list)
monkey_business = monkey_inspection_list[0] * monkey_inspection_list[1]
#monkey_business = monkey[0].no_inspection * monkey[3].no_inspection
print("monkey_business: ", monkey_business)
print("NO OF ROUNDS: ", NUM_ROUNDS)
print("MAX VAL: ", MAX_VAL)