# https://github.com/danong/advent-of-code-2018/blob/master/day15.py

from __future__ import annotations

import itertools
from collections import deque
from dataclasses import dataclass
from typing import Tuple, Generator, Optional, List

import numpy as np


# neighbor helper functions
def neighbors(index: Tuple[int, int], bounds: Tuple[int, int]) -> Generator[Tuple[int, int]]:
    """Yields neighbor indices of a point that are within the board in reading order"""
    print(index)
    potential_cells = ((index[0] - 1, index[1]), (index[0], index[1] - 1),
                       (index[0], index[1] + 1), (index[0] + 1, index[1]))
    for n_idx in potential_cells:
        if 0 <= n_idx[0] < bounds[0] and 0 <= n_idx[1] < bounds[1]:
            yield n_idx


def movable(index: Tuple[int, int], board: np.ndarray) -> Generator[Tuple[int, int]]:
    """Yields neighbor indices of a point that are movable"""
    for n_idx in neighbors(index, board.shape):
        if board[n_idx] == Game.free:
            yield n_idx


def can_attack(idx: Tuple[int, int], board: np.ndarray, target: str, agents: List[Agent]) -> Optional[Agent, bool]:
    """Return index of adjacent cell that should be attacked or False if no enemy targets are in range"""
    attack_list = []
    for n_idx in neighbors(idx, board.shape):
        if board[n_idx] == target:
            attack_list.append(n_idx)
    if attack_list:
        candidates = [agent for agent in agents if agent.location in attack_list]
        min_hp = min(candidates, key=lambda x: x.hp).hp
        candidates = [agent for agent in candidates if agent.hp == min_hp]
        if len(candidates) == 1:
            return candidates[0]
        else:
            return sorted(candidates, key=lambda x: x.location)[0]

    return False


@dataclass
class Agent:
    team: str
    location: Tuple[int, int]
    hp: int
    attack_power: int

    def __repr__(self):
        return 'Char("{}", {}, {}, {})'.format(self.team, self.location, self.hp, self.attack_power)

    def move(self, board: np.ndarray, enemies: List[Agent]) -> None:
        queue = deque([])
        prev = {self.location: None}

        for idx in movable(self.location, board):
            queue.append((idx, 1))
            prev[idx] = self.location
        moves = float('inf')
        cur_idx = None
        potential_moves = []
        while queue:
            print(queue)
            cur_idx, num_moves = queue.popleft()
            if can_attack(cur_idx, board, self.enemy, enemies):
                moves = num_moves
                potential_moves.append(cur_idx)
                continue
            for n_idx in movable(cur_idx, board):
                if n_idx not in prev:
                    prev[n_idx] = cur_idx
                    queue.append(n_idx)

        if moves:
            # backtrack
            while prev[cur_idx]:
                new_location, cur_idx = cur_idx, prev[cur_idx]
            assert (self.location != new_location)
            board[self.location] = Game.free
            self.location = new_location
            board[self.location] = self.team

    def turn(self, board: np.ndarray, enemies: List[Agent]) -> Optional[Agent]:
        """Move agent (optional) and return index of attack target (optional)"""
        if not can_attack(self.location, board, self.enemy, enemies):
            self.move(board, enemies)
        target = can_attack(self.location, board, self.enemy, enemies)
        return target

    @property
    def enemy(self):
        return Game.elf if self.team == Game.goblin else Game.goblin


class Game:
    wall = '#'
    free = '.'
    goblin = 'G'
    elf = 'E'

    def __init__(self, board):
        self.board = board
        self.turns = 0

        self.agents = {self.elf: [], self.goblin: []}
        for index, val in np.ndenumerate(board):
            if val == self.goblin or val == self.elf:
                # self.board[index] = self.free
                self.agents[val].append(Agent(val, index, 200, 3))

    def display(self) -> None:
        print(self.turns, self.scores)
        for row in self.board:
            print(''.join(row))

    def play(self) -> None:
        while not self.won:
            self.display()
            # print(self.agents.values())
            self.turn()
            self.turns += 1
        print((self.turns - 1) * max(self.scores))

    def turn(self):
        sorted_agents = sorted(itertools.chain.from_iterable(self.agents.values()), key=lambda a: a.location)
        for agent in sorted_agents:
            if agent.hp <= 0:
                continue
            target = agent.turn(self.board, self.agents[agent.enemy])
            if target:
                print(f'{agent} attacks {target}')
                target.hp -= agent.attack_power
                if target.hp <= 0:
                    self.board[target.location] = self.free
                    self.agents[agent.enemy].remove(target)
                    # sorted_agents.remove(target)
                    del target

    @property
    def won(self) -> bool:
        return not all(self.agents.values())

    @property
    def scores(self) -> Tuple[int, int]:
        return self.team_score(self.elf), self.team_score(self.goblin)

    def team_score(self, team: str) -> int:
        return sum(agent.hp for agent in self.agents[team])


def main():
    with open('inputtest', 'r') as f_in:
        board = [list(x.strip()) for x in f_in.readlines()]

    board = np.array(board, dtype=str)
    game = Game(board)
    game.play()


if __name__ == '__main__':
    main()