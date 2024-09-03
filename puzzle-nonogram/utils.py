def task_to_list(task):
	task_list = []
	for elem in task:
		string_list = elem.text.split('\n')
		int_list = []
		for string in string_list:
			int_list.append(int(string))
		task_list.append(int_list)
	return task_list

def create_str_list_from(task_list, longest):
	str_task_data = []
	for task in task_list:
		str_task = ''
		for i in range(longest):
			if len(task) < longest - i:
				str_task += '      '
			else:
				str_number = str(task[i - (longest - len(task))])
				str_task += ' ' * (len(str_number) < 3) + str_number + ' ' * (len(str_number) == 1) + '   '
		str_task_data.append(str_task[:-3])
	return str_task_data


class Tile:
	def __init__(self):
		self.fill = 'unknown'
		self.final = False

	def __str__(self):
		if self.fill == 'black':
			return '█'
		elif self.fill == 'white':
			return 'x'
		else:
			return '·'


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
		longest_row_data = max([len(elem) for elem in self.task_row])
		longest_column_data = max([len(elem) for elem in self.task_column])
		str_column_data = create_str_list_from(self.task_column, longest_column_data)
		str_row_data = create_str_list_from(self.task_row, longest_row_data)
		line_separator = '─' * (3 * (longest_row_data * 2 - 1) + 4 * (len(self.task_column)) + 1) + '\n'
		for i in range(longest_column_data * 2 - 1):
			out += '   ' * (longest_row_data * 2 - 1)
			for j in range(len(self.task_column)):
				out += '|' + str_column_data[j][(i * 3):(i * 3) + 3]
			out +='|\n'
		for x in range(len(self.task_row)):
			out += line_separator
			out += str_row_data[x]
			for y in range(len(self.task_column)):
				out += '|' + str(self.grid[x][y]) * 3
			out += '|\n'
		out += line_separator
		return out