from functools import reduce


def find_starts(d):
    return set(reduce(lambda a, b: a + b, d.values())) - set(d.keys())


rules = {}
with open("input") as f:
    for line in f.readlines():
        froms = line.split(' ')[1]
        to = line.split(' ')[7]

        if to in rules:
            rules[to] = rules[to] + froms
        else:
            rules[to] = froms

start_options = sorted(list(find_starts(rules)))
# output = sorted(list(find_starts(rules)))[0]
output = start_options[0]

more = True
while more:
    more = False
    options = start_options
    for o in output[::-1]:
        options = options + list(filter(lambda x: x not in output, ({k: v for k, v in rules.items() if o in v})))
    options = sorted(list(set(options) - set(output)))
    for r in options:
        if (r in rules and len(set(rules[r]) - set(output)) == 0) or (r not in rules and r not in output):
            output = output + r
            more = True
            break

print(output)
