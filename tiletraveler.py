# A computer game where a player is located in a certain tile in a grid
# the player chooses directions and the program tells him/her if the direction is valid or not
# the goal is to reach the victory location [3,1].

# define the beginning tile [1,1]
# Create a function for each direction
# Ask player for direction
# go to the function for the direction chosen
# the functions check the tile where the player is located
# and returns the new location
# if the direction chosen is a closed wall the function prints out 'invalid direction'
# repeated until the player reaches the victory tile [3,3]
# game ends when player reaches victory tile 


tile = '1,1' # always begin at tile [1,1]

def directions_allowed(tile):
    '''checks which tile player is at and prints out available directions'''
    if tile == '1,1' or tile == '2,1':
        print('You can travel: (N)orth.')
    elif tile == '1,3':
        print('You can travel: (E)ast or (S)outh.')
    elif tile == '1,2':
        print('You can travel: (N)orth or (E)ast or (S)outh.')
    elif tile == '2,3':
        print('You can travel: (E)ast or (W)est.')
    elif tile == '2,2' or tile == '3,3':
        print('You can travel: (S)outh or (W)est.')
    elif tile == '3,2':
        print('You can travel: (N)orth or (S)outh.')

def north(tile):
    '''check the tile number and returns a new tile location if direction is possible'''
    if tile == '1,1':
        tile = '1,2'
    elif tile == '2,1':
        tile = '2,2'
    elif tile == '1,2':
        tile = '1,3'
    elif tile == '3,2':
        tile = '3,3'
    else:
        print('Not a valid direction!')
    return tile

def south(tile):
    '''check the tile number and returns a new tile location if direction is possible'''
    if tile == '1,3':
        tile = '1,2'
    elif tile == '1,2':
        tile = '1,1'
    elif tile == '3,3':
        tile = '3,2'
    elif tile == '3,2':
        tile = '3,1'
    elif tile == '2,2':
        tile = '2,1'
    else:
        print('Not a valid direction!')
    return tile

def east(tile):
    '''check the tile number and returns a new tile location if direction is possible'''
    if tile == '1,3':
        tile = '2,3'
    elif tile == '1,2':
        tile = '2,2'
    elif tile == '2,3':
        tile = '3,3'
    else:
        print('Not a valid direction!')
    return tile

def west(tile):
    '''check the tile number and returns a new tile location if direction is possible'''
    if tile == '2,3':
        tile = '1,3'
    elif tile == '3,3':
        tile = '2,3'
    elif tile == '2,2':
        tile = '1,2'
    else:
        print('Not a valid direction!')
    return tile

# the game continues until victory tile is reached, [3,1]
while tile != '3,1':
    # print out directions allowed for the player to choose
    directions = directions_allowed(tile)
    direction = input('Direction: ').upper()
    # checks the chosen direction and invokes the appropriate function
    # to move the player around the tile grid
    if direction == 'N':
        tile = north(tile)
    elif direction == 'S':
        tile = south(tile)
    elif direction == 'E':
        tile = east(tile)
    elif direction == 'W':
        tile = west(tile)
else:
    print('Victory!')
