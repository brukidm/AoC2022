with open(r"input") as f:
    values = f.read().split('\n')
    print(values)
    calories = []

    total = 0
    for value in values:
        if value != "":
            total += int(value)
        else:
            calories.append(total)
            total = 0
    calories.sort()
    print(sum(calories[-3:]))
