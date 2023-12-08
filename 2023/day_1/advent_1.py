file = "input.txt"

with open(file, "r") as f:
    input_from_file = [i.strip() for i in f.readlines()]

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


def replace_str_from_by_int(x):
    for k, v in fixs.items():
        if k in x:
            x = x.replace(k, fixs[k][0]).replace(k, fixs[k][1])
    return x


def get_digit(i):
    j = i
    while i >= 10:
        i = i / 10
    i = int(i)
    j = j % 10
    r = int(str(i) + str(j))
    return r


def double_digit(i):
    r = int(str(i) * 2)
    return r


fixed_input = [replace_str_from_by_int(i) for i in input_from_file]
ints_of_fixed_input = [int("".join(filter(str.isdigit, ws))) for ws in fixed_input]

for ints in ints_of_fixed_input:
    if ints > 99:
        replace_ints = get_digit(ints)
        ints_of_fixed_input[ints_of_fixed_input.index(ints)] = replace_ints
    if ints < 10:
        replace_ints = double_digit(ints)
        ints_of_fixed_input[ints_of_fixed_input.index(ints)] = replace_ints

print(f"RESULT: {sum(ints_of_fixed_input)}")
