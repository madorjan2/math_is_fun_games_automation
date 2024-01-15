from pom import PageModel

class Tile:
	def __init__(self, orientation):
		self.orientation = orientation.split('-')[1]
		self.visited = False

	def __str__(self):
		match self.orientation:
			case '0000':
				return ' '
			case '1010':
				return '│'
			case '0101':
				return '─'
			case '1100':
				return '└'
			case '0110':
				return '┌'
			case '0011':
				return '┐'
			case '1001':
				return '┘'
			case '1212':
				return '┼'
			case '2121':
				return '┼'

	def rotate(self):
		self.orientation = self.orientation[-1:] + self.orientation[:-1]

	def set_rotation(self, orientation):
		self.orientation = orientation

	def is_empty(self):
		return self.orientation == '0000'

	def get_shape(self):
		if '12' in self.orientation:
			return 'cross'
		elif '11' in self.orientation or '00' in self.orientation:
			return 'curve'
		else:
			return 'straight'

	def get_orientation(self):
		return f'pipe-{self.orientation}'

class Board:
	def __init__(self, start_coordinates, end_coordinates):
		self.grid = []
		self.start = start_coordinates
		self.end = end_coordinates

	def __str__(self):
		out = ''
		for row in self.grid:
			for tile in row:
				out += str(tile)
			out += '\n'
		return out

	def setup(self, rows, columns):
		for i in range(rows):
			self.grid.append([])
			for _ in range(columns):
				self.grid[i].append(None)

	def add_tile(self, tile: Tile, row_index, column_index):
		self.grid[row_index][column_index] = tile

	def solve(self):
		self.solve_for_next(self.start, (-1 * self.start[0], -1 * self.start[1]), [])
		solution = []
		for i, row in enumerate(self.grid):
			solution.append([])
			for tile in self.grid[i]:
				solution[i].append(tile.get_orientation())
		return solution

	def solve_for_next(self, pos, facing, touched, solved=False):
		# print('\n' + str(self))
		if not solved:
			x = pos[0] + facing[0]
			y = pos[1] + facing[1]
			curr_pos = (x, y)
			if curr_pos == self.end:
				return True
			elif (x not in range(len(self.grid[0])) or
				  y not in range(len(self.grid)) or
					self.grid[y][x].is_empty() or
				  (curr_pos in touched) and self.grid[y][x].get_shape() != 'cross'):
				return False
			else:
				touched.append(curr_pos)
				tile = self.grid[y][x]
				shape = tile.get_shape()
				if shape == 'cross':
					solved = self.solve_for_next(curr_pos, facing, touched.copy(), solved)
					return solved
				elif shape == 'straight':
					tile.set_rotation('0101' if facing[1] == 0 else '1010')
					solved = self.solve_for_next(curr_pos, facing, touched.copy(), solved)
					return solved
				else:
					orientation_possibilities = None
					facing_possiblities = [(facing[1], facing[0]), (facing[1] * -1, facing[0] * -1)]
					match facing:
						case (-1, 0):
							orientation_possibilities = ['1100', '0110']
						case (1, 0):
							orientation_possibilities = ['0011', '1001']
						case (0, -1):
							orientation_possibilities = ['0011', '0110']
						case (0, 1):
							orientation_possibilities = ['1100', '1001']
					for i in range(2):
						if not solved:
							tile.set_rotation(orientation_possibilities[i])
							solved = self.solve_for_next(curr_pos, facing_possiblities[i], touched.copy(), solved)
							if solved:
								return True

def remove_ads(page: PageModel):
	for ad in page.ads():
		page.driver.execute_script("""
			var element = arguments[0];
			element.parentNode.removeChild(element);
			""", ad)