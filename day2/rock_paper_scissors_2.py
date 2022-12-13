score = 0
# rock paper scissors
f = open("input.txt")
for line in f:
    if line[2] == "X": # lose
        #print("X: ", line)
        score += 0
        if line[0] == "A": # rock , scissors
            score += 3
        elif line[0] == "B": # paper, rock
            score += 1
        elif line[0] == "C":
            score += 2
    elif line[2] == "Y": # draw
        score += 3
        if line[0] == "A":
            score += 1
        elif line[0] == "B":
            score += 2
        elif line[0] == "C":
            score += 3
    elif line[2] == "Z": # win
        score += 6
        if line[0] == "A": # rock, paper
            score += 2
        elif line[0] == "B": # paper, scissors
            score += 3
        elif line[0] == "C":
            score += 1
f.close()
print("score: ", score)