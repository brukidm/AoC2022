with open(r"input") as f:
    values = f.read().split('\n')
    total = 0
    for value in values:
        opp, me = value.split(" ")
        if me == "X": # lose
            if opp == "A":
                total += 3
            elif opp == "B":
                total += 1
            else:
                total += 2
        elif me == "Y": # draw
            total += 3
            if opp == "A":
                total += 1
            elif opp == "B":
                total += 2
            else:
                total += 3
        else: # win
            total += 6
            if opp == "A":
                total += 2
            elif opp == "B":
                total += 3
            else:
                total += 1
    print(total)