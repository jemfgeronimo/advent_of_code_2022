line1 = "[1,1,3,1,1]\n"
line2 = "[1,1,5,1,1]\n"

line3 = "[[1],[2,3,4]]\n"
line4 = "[[1],4]\n"

line5 = "[9]\n"
line6 = "[[8,7,6]]\n"

line7 = "[[4,4],4,4]\n"
line8 = "[[4,4],4,4,4]\n"

line9 = "[7,7,7,7]\n"
line10 = "[7,7,7]\n"

line11 = "[]\n"
line12 = "[3]\n"

line13 = "[[[]]]\n"
line14 = "[[]]\n"

line15 = "[1,[2,[3,[4,[5,6,7]]]],8,9]\n"
line16 = "[1,[2,[3,[4,[5,6,0]]]],8,9]\n"

def day13_line_parser(line1):
    line = line1.strip()
    arr = []
    prev_ch = ""
    for ch in line:
        if ch in ["[", "]", ","]:
            arr.append(ch)
        else:
            if prev_ch not in ["[", "]", ","]:
                arr.append(ch)
            else:
                arr[-1] += ch
        prev_ch = ch
    return arr


parsed_line = day13_line_parser(line1)
for ch in parsed_line:
    print(ch, end=",")