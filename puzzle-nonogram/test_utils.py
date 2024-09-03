import utils


class TestUtilFunctions:
	def test_create_str_list_from_short_data(self):
		test_data = [[], [1, 1, 2], [5]]
		assert utils.create_str_list_from(test_data, 3) == [' ' * 15, ' 1     1     2 ', '             5 ']

	def test_create_str_list_from_longer_data(self):
		test_data = [[], [1, 1, 2], [5], [1, 2, 3, 4, 5], [], [20, 10]]
		assert utils.create_str_list_from(test_data, 5) == [' ' * 27,
															'             1     1     2 ',
															'                         5 ',
															' 1     2     3     4     5 ',
															' ' * 27,
															'                   20    10']


class TestNonogram:

	def test_constructor_and_str(self):
		test_rows = [[], [1], [1, 20, 3], [1, 2]]
		test_columns = [[4, 50, 6], [4], [], [4, 6]]
		nono = utils.Nonogram(4, test_columns, test_rows)
		assert str(nono) == ('               | 4 |   |   |   |\n\
               |   |   |   |   |\n\
               | 50|   |   | 4 |\n\
               |   |   |   |   |\n\
               | 6 | 4 |   | 6 |\n\
────────────────────────────────\n\
               |···|···|···|···|\n\
────────────────────────────────\n\
             1 |···|···|···|···|\n\
────────────────────────────────\n\
 1     20    3 |···|···|···|···|\n\
────────────────────────────────\n\
       1     2 |···|···|···|···|\n\
────────────────────────────────\n')
