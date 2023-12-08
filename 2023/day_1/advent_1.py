file = "input.txt"

with open(file, "r") as f:
    asdf = [i.strip() for i in f.readlines()]


fixs = {
    "one": ["oonee", "1"],
    "two": ["ttwoo", "2"],
    "three": ["tthreee", "3"],
    "four": ["ffourr", "4"],
    "five": ["ffivee", "5"],
    "six": ["ssixx", "6"],
    "seven": ["ssevenn", "7"],
    "eight": ["eeightt", "8"],
    "nine": ["nninee", "9"],
}


def fix_inputs(x):
    for k, v in fixs.items():
        if k in x:
            x = x.replace(k, fixs[k][0]).replace(k, fixs[k][1])
    result = x
    return result


def fix_three_and_longer_digits(i, j):
    while i >= 10:
        i = i / 10
    i = int(i)
    j = j % 10
    r = int(str(i) + str(j))
    return r


def fix_one_digit(i):
    r = int(str(i) * 2)
    return r


print(weird_stuff)
wtf_stuff = [fix_inputs(i) for i in weird_stuff]
print(f"Fixed input: {wtf_stuff}")


ints_of_weird_stuff = [int("".join(filter(str.isdigit, ws))) for ws in wtf_stuff]

print(ints_of_weird_stuff)

for ints in ints_of_weird_stuff:
    if ints > 99:
        replace_ints = fix_three_and_longer_digits(ints, ints)
        ints_of_weird_stuff[ints_of_weird_stuff.index(ints)] = replace_ints
    if ints < 10:
        replace_ints = fix_one_digit(ints)
        ints_of_weird_stuff[ints_of_weird_stuff.index(ints)] = replace_ints
print(f"RESULT: {sum(ints_of_weird_stuff)}")
