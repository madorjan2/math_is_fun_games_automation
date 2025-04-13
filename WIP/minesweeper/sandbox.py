from game_classes import Board

b = []
for i in range(3):
    b.append([])
    for j in range(10):
        b[i].append('_')

b[2][3] = '0'
b[0][1] = '3'
b[1][8] = '2'


my_board = Board(b, 5)
print(my_board)
print(my_board.solve_next_step())