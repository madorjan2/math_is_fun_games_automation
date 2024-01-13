import utils

class TestTiles:

	def setup_method(self):
		self.tile = utils.Tile('pipe-1010')
		self.tile2 = utils.Tile('pipe-0110')
		self.empty_tile = utils.Tile('pipe-0000')


	def test_constructor_and_str(self):
		assert str(self.tile) == '│'
		assert str(self.tile2) == '┌'
		assert str(self.empty_tile) == ' '

	def test_rotate(self):
		self.tile.rotate()
		assert str(self.tile) == '─'

		self.tile2.rotate()
		assert str(self.tile2) == '┐'

		self.empty_tile.rotate()
		assert str(self.empty_tile) == ' '

	def test_set_rotation(self):
		self.tile.set_rotation('0011')
		assert str(self.tile) == '┐'

	def test_is_empty(self):
		assert not self.tile.is_empty()
		assert self.empty_tile.is_empty()

	def test_shape(self):
		assert self.tile.get_shape() == 'straight'
		assert self.tile2.get_shape() == 'curve'

class TestBoard:

	def setup_method(self):
		self.board = utils.Board((-1, 0), (2, 1))
		test_data = [[utils.Tile('pipe-1010'), utils.Tile('pipe-0110')],
					[utils.Tile('pipe-0000'), utils.Tile('pipe-1001')]]
		self.board.setup(2, 2)
		for x in range(len(test_data[0])):
			for y in range(len(test_data)):
				self.board.add_tile(test_data[x][y], x, y)

	def test_constructor_and_str(self):
		assert str(self.board) == '│┌\n ┘\n'

	def test_solve_2_by_2(self):
		self.board.solve()
		assert str(self.board) == '─┐\n └\n'

	def test_solve_big_one(self):
		test_board = utils.Board((-1, 0), (4, 5))
		test_board.setup(6, 4)
		test_board.add_tile(utils.Tile('page-1010'), 0, 0)
		test_board.add_tile(utils.Tile('page-0011'), 0, 1)
		test_board.add_tile(utils.Tile('page-0110'), 0, 2)
		test_board.add_tile(utils.Tile('page-0011'), 0, 3)

		test_board.add_tile(utils.Tile('page-1100'), 1, 0)
		test_board.add_tile(utils.Tile('page-1001'), 1, 1)
		test_board.add_tile(utils.Tile('page-1010'), 1, 2)
		test_board.add_tile(utils.Tile('page-1010'), 1, 3)

		test_board.add_tile(utils.Tile('page-0101'), 2, 0)
		test_board.add_tile(utils.Tile('page-0110'), 2, 1)
		test_board.add_tile(utils.Tile('page-1100'), 2, 2)
		test_board.add_tile(utils.Tile('page-0101'), 2, 3)

		test_board.add_tile(utils.Tile('page-0101'), 3, 0)
		test_board.add_tile(utils.Tile('page-1010'), 3, 1)
		test_board.add_tile(utils.Tile('page-1010'), 3, 2)
		test_board.add_tile(utils.Tile('page-0101'), 3, 3)

		test_board.add_tile(utils.Tile('page-0101'), 4, 0)
		test_board.add_tile(utils.Tile('page-0101'), 4, 1)
		test_board.add_tile(utils.Tile('page-1010'), 4, 2)
		test_board.add_tile(utils.Tile('page-1010'), 4, 3)

		test_board.add_tile(utils.Tile('page-1100'), 5, 0)
		test_board.add_tile(utils.Tile('page-1100'), 5, 1)
		test_board.add_tile(utils.Tile('page-1010'), 5, 2)
		test_board.add_tile(utils.Tile('page-1100'), 5, 3)

		test_board.solve()


		assert str(test_board) == '─┐┌┐\n┌┘││\n│┌┘│\n││││\n││││\n└┘│└\n'