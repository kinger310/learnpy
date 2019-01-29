# Day 15 part 1+2

from termcolor import colored
from collections import deque
import numpy


class MapUnit:
    def __init__(self, pos, type, attack_power):
        self.pos = pos
        self.type = type
        self.attack_power = attack_power
        self.hp = 200

    def alive(self):
        return self.hp > 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.type + "(" + str(self.hp) + ")"


class CombatEnd(Exception):
    pass


class ElfDied(Exception):
    pass


def parse(file_name, elf_attack_power=3):
    with open(file_name) as f:
        max_x = 0
        max_y = 0
        units = set()
        walls = set()

        for y, line in enumerate(f.readlines()):
            max_y = max(max_y, y)
            for x, char in enumerate(line.strip()):
                max_x = max(max_x, x)
                if char in "GE":
                    units.add(MapUnit((x, y), char, (3 if char == "G" else elf_attack_power)))
                if char == "#":
                    walls.add((x, y))

    return units, walls, (max_x, max_y)


def reading_order(xy_tuple):
    return (xy_tuple[1], xy_tuple[0])


def adjacent(xy):
    return [(xy[0] - 1, xy[1]), (xy[0] + 1, xy[1]), (xy[0], xy[1] - 1), (xy[0], xy[1] + 1)]


def bfs(pos, avail, targets, max_xy):
    HIGH_VAL = 1000  # 这个值设的很精妙

    visited = deque([(pos, 0)])
    arr = numpy.zeros((max_xy[1] + 1, max_xy[0] + 1)) + HIGH_VAL

    if pos in targets:
        return pos, 0

    while len(visited) > 0:
        current = visited.popleft()
        if arr[current[0][1]][current[0][0]] == HIGH_VAL:
            options = [x for x in adjacent(current[0]) if x in avail and arr[x[1]][x[0]] == HIGH_VAL]
            for option in options:
                visited.append((option, current[1] + 1))

            arr[current[0][1]][current[0][0]] = current[1]

    min_c = HIGH_VAL
    for targ in targets:
        min_c = min(min_c, arr[targ[1], targ[0]])

    return pos, (min_c if min_c != HIGH_VAL else None)


def do_print(combs, walls, round, max_xy):
    # Clear console
    # print("\33c")

    output = "\nROUND " + str(round) + "\n\n"
    for y in range(max_xy[1] + 1):
        for x in range(max_xy[0] + 1):
            filtered = list(filter(lambda c: c.pos[0] == x and c.pos[1] == y and c.hp > 0, combs))
            if (x, y) in walls:
                output += "#"
            elif len(filtered) > 0:
                if filtered[0].type == "G":
                    output += colored(filtered[0].type, 'green')
                else:
                    output += colored(filtered[0].type, 'red')
            else:
                output += "."

        output += "\t" + str(list(sorted(filter(lambda c: c.pos[1] == y, combs), key=lambda x: (x.pos[0])))).replace(
            "[", "").replace("]", "")

        output += "\n"

    print(output, flush=True)
    input()  # Pause for input


def play(units, walls, max_xy, print_out=True, elf_die_exit=False):
    round = 0
    finished = False
    try:
        while True:
            ordered_units = sorted(units, key=lambda x: reading_order(x.pos))

            for unit in ordered_units:
                # Are they alive?
                if not unit.hp > 0:
                    continue

                # Find opposition that are alive
                targets = set([x for x in ordered_units if x.type != unit.type and x.hp > 0])

                # Check for combat end
                if (len(targets)) == 0:
                    raise CombatEnd('Combat End')

                # Squares we can currently attack
                can_attack = adjacent(unit.pos)

                # If nobody is in attacking range...
                in_range = [x for x in targets if x.pos in can_attack]
                if len(in_range) == 0:
                    # Get the unallocated spaces
                    unnoc = set()
                    for y in range(1, max_xy[1]):
                        for x in range(1, max_xy[0]):
                            alive_units = [x for x in ordered_units if x.hp > 0]
                            if ((x, y) not in walls) and x is not max_xy[0] and y is not max_xy[1] \
                                    and (x, y) not in [d.pos for d in alive_units]:
                                unnoc.add((x, y))
                    unnoc.add(unit.pos)

                    possible_target_squares = []
                    for targ in targets:
                        possible_target_squares.extend([x for x in adjacent(targ.pos) if x in unnoc])

                    # surrounding = list(map(lambda s: bfs(s, unnoc, possible_target_squares, max_xy),
                    #                        [x for x in adjacent(unit.pos) if x in unnoc]))
                    surrounding = []
                    for s in adjacent(unit.pos):
                        if s in unnoc:
                            ele = bfs(s, unnoc, possible_target_squares, max_xy)
                            surrounding.append(ele)
                    surrounding = [x for x in surrounding if x[1] is not None]

                    # If there is a surrounding square free
                    if len(surrounding) > 0:
                        best_move = sorted(surrounding, key=lambda x: (x[1], reading_order(x[0])))[0][0]
                        unit.pos = best_move

                        # Update attacking pos
                        can_attack = adjacent(unit.pos)
                        in_range = [x for x in targets if x.pos in can_attack]

                # If someone is in range, attack..
                if len(in_range) > 0:
                    # Prioritize the weakest unit
                    priority = sorted(in_range, key=lambda x: (x.hp, reading_order(x.pos)))
                    priority[0].hp = max(0, priority[0].hp - unit.attack_power)

                    # For part 2..
                    if elf_die_exit and priority[0].hp == 0 and priority[0].type == "E":
                        raise ElfDied()

            round += 1
            if print_out:
                do_print(units, walls, round, max_xy)

    except CombatEnd:
        finished = True
        total_hp = sum(map(lambda x: x.hp, ordered_units))
        print("Combat ended. Round: " + str(round) + ", total: " + str(round * total_hp), flush=True)
    except ElfDied:
        finished = False

    return finished


units, walls, max_xy = parse("input")
play(units, walls, max_xy, False)  # part 1

elf_win_no_death = False
attack = 3
while not elf_win_no_death:
    attack += 1
    units, walls, max_xy = parse("input", attack)

    elf_win_no_death = play(units, walls, max_xy, False, True)
    print(attack, elf_win_no_death, flush=True)  # part 2