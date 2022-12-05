with open(r"input") as f:
    values = f.read().split('\n')
    total = 0
    for value in values:
        value = value.split(",")
        first, second = value[0], value[1]

        first_range = first.split("-")
        first_range = set(range(int(first_range[0]), int(first_range[1]) + 1))

        second_range = second.split("-")
        second_range = set(range(int(second_range[0]), int(second_range[1]) + 1))

        if first_range.issubset(second_range) or second_range.issubset(first_range):
            total += 1
    print(total)