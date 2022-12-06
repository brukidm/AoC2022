with open(r"input") as f:
    values = f.read().split('\n')
    values = list(values[0])
    last_four = []
    i = 0
    for value in values:
        if len(last_four) == 4 and len(last_four) == len(set(last_four)):
            print(i)
            break
        if len(last_four) == 4:
            last_four.pop(0)
        last_four.append(value)
        i += 1
        