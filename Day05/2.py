with open(r"input") as f:
    values = f.read().split('\n')
    columns = {}
    movements = []
    cargo_done = False
    
    # HUGE PARSE
    for value in values:
        if not value:
            cargo_done = True
            continue
        column = 1
        # for each row
        i = 0
        if not cargo_done:
            while i < len(value):
                if not column in columns:
                    columns[column] = list()
                if value[i+1].isalpha():
                    columns[column].append(value[i+1])
                i += 4
                column += 1
        else:
            m = value.split(" ")
            movements.append((m[1], m[3], m[5]))
    
    # reverse cargos
    for column in columns:
        columns[column].reverse()
    
    # do the movements
    for movement in movements:
        to_move = []
        for i in range(int(movement[0])):
            remove = columns[int(movement[1])].pop()
            to_move.append(remove)
        to_move.reverse()
        new_list = columns[int(movement[2])]
        for m in to_move:
            new_list.append(m)
        columns[int(movement[2])] = new_list

    result = ""
    for column in columns:
        result += columns[column].pop()
    print(result)
