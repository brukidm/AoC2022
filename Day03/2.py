import string

def get_priority(character):
    if character in string.ascii_lowercase:
        return string.ascii_lowercase.index(character) + 1
    else:
        return string.ascii_uppercase.index(character) + 27
    

with open(r"input") as f:
    values = f.read().split('\n')
    total = 0
    for i in range(0, len(values), 3):
        first, second, third = set(values[i]), set(values[i+1]), set(values[i+2])
        intersection = first.intersection(second)
        intersection = intersection.intersection(third)
        total += get_priority(intersection.pop())
    print(total)