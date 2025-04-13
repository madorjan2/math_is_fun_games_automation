import random


class Tile:
    def __init__(self, x, y, state):
        # State is represented as a character
        # '0'-'8' -> revealed, the number of surrounding mines
        # '_' -> unrevealed
        # '*' -> mine
        self.x = x
        self.y = y
        self.state = state
        self.safe = 0

    def get_pos(self):
        return self.x, self.y

    def get_state(self):
        return self.state

    def get_safe_counter(self):
        return self.safe

    def increase_safe_counter(self):
        self.safe += 1

    def nul_safe_counter(self):
        self.safe = 0

    def is_safe(self):
        return self.state != '*'

    def is_bomb(self):
        return self.state == '*'

    def is_unknown(self):
        return self.state == '_'

    def is_number(self):
        return self.state != '_' and self.state != '*'

    def get_number(self):
        return int(self.state)


    def get_neighbours(self, dimensions):
        neighbours = []
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if 0 <= i < dimensions[0] and 0 <= j < dimensions[1] and not(i == self.x and j == self.y):
                    neighbours.append((i,j))
        return neighbours

class Board:

    REQUIRED_SOLUTIONS = 1000

    def __init__(self, state, bombs_left):
        self.bombs_left = bombs_left
        if isinstance(state, Board):
            self.state = state
        else:
            self.state = []
            for i in range(len(state)):
                self.state.append([])
                for j in range(len(state[i])):
                    self.state[i].append(Tile(i, j, state[i][j]))

    def __str__(self):
        out = ''
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                out += self.state[i][j].get_state()
            out += '\n'
        return out

    # Current algorithm
    # Try randomly, until you get n correct solutions
    # Average those solutions for the safest cells
    def solve_next_step(self):
        found_solutions = 0
        while found_solutions < self.REQUIRED_SOLUTIONS:
            random_solved_board = self.monte_carlo()
            if random_solved_board.is_valid_solution():
                found_solutions += 1
                for i in range(len(self.state)):
                    for j in range(len(self.state[i])):
                        if random_solved_board.state[i][j].is_safe():
                            self.state[i][j].increase_safe_counter()
        safest_tile = None
        safest_tile_score = None
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                safety_score = self.state[i][j].get_safe_counter() / found_solutions
                if safest_tile_score is None or abs(50-safety_score) > abs(50-safest_tile_score):
                    safest_tile_score = safety_score
                    safest_tile = (i, j)
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                self.state[i][j].nul_safe_counter()
        return safest_tile, safest_tile_score < 50


    def monte_carlo(self):
        candidates = []
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j].is_unknown():
                    candidates.append((i,j))
        random.shuffle(candidates)
        candidates = candidates[:self.bombs_left]
        new_state = []
        for i in range(len(self.state)):
            new_state.append([])
            for j in range(len(self.state[i])):
                if (i,j) in candidates:
                    new_state[i].append('*')
                else:
                    new_state[i].append(self.state[i][j].get_state())
        return Board(new_state, 0)

    def is_valid_solution(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j].is_number():
                    neighbours = self.state[i][j].get_neighbours((len(self.state), len(self.state[i])))
                    neighbour_bomb_count = 0
                    for neighbour in neighbours:
                        if self.state[neighbour[0]][neighbour[1]].is_bomb():
                            neighbour_bomb_count += 1
                    if neighbour_bomb_count != self.state[i][j].get_number():
                        return False
        return True