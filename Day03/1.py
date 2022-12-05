import string

def get_priority(character):
    if character in string.ascii_lowercase:
        return string.ascii_lowercase.index(character) + 1
    else:
        return string.ascii_uppercase.index(character) + 27
    

with open(r"input") as f:
    values = f.read().split('\n')
    total = 0
    for value in values:
        first, second = value[:len(value)//2], value[len(value)//2:]
        first = set(first)
        second = set(second)
        total += (get_priority(first.intersection(second).pop()))
    print(total)