sticks = 21


def make_move(sticks):
    return sticks % 4 or 1


print('sticks left', sticks)
while sticks > 0:
    my_move = int(input('How many: '))
    sticks -= my_move
    print('sticks left after your move: ', sticks)
    sticks -= make_move(sticks)
    print('sticks left after computer move: ', sticks)
