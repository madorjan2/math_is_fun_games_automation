def task_to_list(task):
	task_list = []
	for elem in task:
		string_list = elem.text.split('\n')
		int_list = []
		for string in string_list:
			int_list.append(int(string))
		task_list.append(int_list)
	return task_list

class Tile():
	def __init__(self):
		self.fill = 'unknown'
		self.final = False

	def is_final(self):
		return self.final

	def get_fill(self):
		return self.fill

	def is_black(self):
		return self.fill == 'black'

	def is_white(self):
		return self.fill == 'white'

	def is_unknown(self):
		return self.fill == 'unknown'
	def set_black(self):
		self.fill = 'black'

	def set_white(self):
		self.fill = 'white'

	def set_unkown(self):
		self.fill = 'unknown'

	def set_final(self):
		self.final = True
class Nonogram:

	def __init__(self, size, task_column, task_row):
		self.size = size
		self.task_column = task_column
		self.task_row = task_row

		self.grid = []

		for x in range(self.size):
			self.grid.append([])
			for y in range(self.size):
				self.grid[x].append(Tile())

	def __str__(self):
		out = ''
		for x in range(self.size):
			for y in range(self.size):
				tile_fill = self.grid[x][y].get_fill()
				if tile_fill == 'black':
					out += '█'
				elif tile_fill == 'white':
					out += 'x'
				else:
					out += '·'
			out += '\n'

