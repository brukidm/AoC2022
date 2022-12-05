with open(r"input") as f:
    values = f.read().split('\n')
    total = 0
    for value in values:
        opp, me = value.split(" ")
        if me == "X":
            total += 1
            if opp == "A":
                total += 3
            elif opp == "C":
                total += 6
        elif me == "Y":
            total += 2
            if opp == "B":
                total +=3
            elif opp == "A":
                total += 6
        else:
            total += 3
            if opp == "C":
                total += 3
            elif opp == "B":
                total += 6
    print(total)