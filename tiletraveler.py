# A computer game in which the player is located in a certain tile in a grid
# the player chooses directions and the program tells him/her if the direction is valid or not
# the goal is to reach the victory location (3,1).

tile = '1,1' # always begin at tile [1,1]

def directions_allowed(tile):
    '''checks which tile player is at and prints out available directions'''
    if tile == '1,1' or '2,1':
        print('You can travel: (N)orth.')
    if tile == '1,3':
        print('You can travel: (E)ast or (S)outh.')
    if tile == '1,2' or '3,2':
        print('You can travel: (N)orth or (S)outh.')
    if tile == '2,3':
        print('You can travel: (E)ast or (W)est.')
    if tile == '2,2' or '3,3':
        print('You can travel: (S)outh or (W)est.')

def north(tile):
    if tile == '1,1':
        tile = '1,2'
    elif tile == '2,1':
        tile = '2,2'
    elif tile == '1,2':
        tile = '1,3'
    elif tile == '3,2':
        tile = '3,3'
    else:
        print('Invalid direction')
    return tile

def south(tile):
    if tile == '1,3':
        tile = '1,2'
    elif tile == '1,2':
        tile = '1,1'
    elif tile == '3,3':
        tile = '3,2'
    elif == '3,2':
        tile = '3,1'
    elif tile == '2,2':
        tile = '2,1'
    else:
        print('Invalid direction')
    return tile

def east(tile):
    if tile == '1,3':
        tile = '2,3'
    elif tile == '1,2':
        tile = '2,2'
    elif tile == '2,3':
        tile = '3,3'
    else:
        print('Invalid direction')
    return tile

def west(tile):
    if tile == '2,3':
        tile = '1,3'
    elif tile == '3,3':
        tile = '2,3'
    elif tile == '2,2':
        tile = '1,2'
    else:
        print('Invalid direction')
    return tile


while tile != '3,1':
    directions(tile)
    choose_direction = input('Direction: ').upper()
    if direction == 'N':
        north(tile)
    elif direction == 'S':
        south(tile)
    elif direction == 'E':
        east(tile)
    elif direction == 'W':
        west(tile)

    

# (1,1)
# N 
# (1,2)
# 