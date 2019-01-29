# Day 7 part 2

from functools import reduce

# BASE_TASK_DURATION = 0
# NUM_ELFS = 2
# INPUT = "testinput"
BASE_TASK_DURATION = 60
NUM_ELFS = 5
INPUT = "input"


def find_starts(d):
    return set(reduce(lambda a, b: a + b, d.values())) - set(d.keys())


def duration_for_letter(letter):
    return BASE_TASK_DURATION + ord(letter) - 64  # A = 65


rules = {}
with open(INPUT) as f:
    for line in f.readlines():
        froms = line.split(' ')[1]
        to = line.split(' ')[7]

        if to in rules:
            rules[to] = rules[to] + froms
        else:
            rules[to] = froms

start_options = sorted(list(find_starts(rules)))

more = True
in_progress = {}
ticks = 0
fin = ""
while more:
    more = False
    options = start_options

    print(ticks, in_progress, fin)

    finished = sorted({k: v for k, v in in_progress.items() if ticks >= (duration_for_letter(k) + v)})
    for item in finished:
        fin = fin + item

    in_progress = {k: v for k, v in in_progress.items() if not k in finished}

    for o in fin[::-1]:
        options = options + list(filter(lambda x: x not in fin and x not in in_progress,
                                        ({k: v for k, v in rules.items() if o in v and o not in in_progress})))

    for option in sorted(options):
        if (option in rules and len(set(rules[option]) - set(fin)) == 0) or (
                option not in rules and option not in fin and option not in in_progress):
            for x in range(NUM_ELFS):
                if len(in_progress) < NUM_ELFS:
                    in_progress[option] = ticks
    if len(in_progress) > 0:
        more = True

    ticks = ticks + 1

print(ticks - 1)