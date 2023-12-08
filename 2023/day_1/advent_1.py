file: str = "input.txt"

with open(file, "r") as f:
    input_from_file: list = [i.strip() for i in f.readlines()]

fixs: dict = {
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


def replace_str_from_list_by_int(x: str) -> str:
    for k, v in fixs.items():
        if k in x:
            x = x.replace(k, fixs[k][0]).replace(k, fixs[k][1])
    return x


def get_first_and_last_digit(i: int) -> int:
    j = i
    while i >= 10:
        i = i / 10
    i = int(i)
    j = j % 10
    r = int(str(i) + str(j))
    return r


def get_double_digit(i: int) -> int:
    r = int(str(i) * 2)
    return r


fixed_input: list = [replace_str_from_list_by_int(i) for i in input_from_file]
ints_of_fixed_input: list = [
    int("".join(filter(str.isdigit, ws))) for ws in fixed_input
]

for ints in ints_of_fixed_input:
    if ints > 99:
        replace_ints = get_first_and_last_digit(ints)
        ints_of_fixed_input[ints_of_fixed_input.index(ints)] = replace_ints
    if ints < 10:
        replace_ints = get_double_digit(ints)
        ints_of_fixed_input[ints_of_fixed_input.index(ints)] = replace_ints

print(f"Result: {sum(ints_of_fixed_input)}")
