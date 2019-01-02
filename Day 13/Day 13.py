import numpy as np

init_tracks = open("input.txt").read().split('\n')

# Filter out empty strings
init_tracks = list(filter(None, init_tracks))
tracks = np.ndarray((len(init_tracks),len(init_tracks[0])),object)
for i in range(len(init_tracks)):
    tracks[i] = list(init_tracks[i])


def left(y,x):
    return y,x-1

def up(y,x):
    return y-1,x

def right(y,x):
    return y,x+1

def down(y,x):
    return y+1,x


def is_dir_left():
    return carts[i][3] == 0


def is_dir_up():
    return carts[i][3] == 1


def is_dir_right():
    return carts[i][3] == 2


def is_dir_down():
    return carts[i][3] == 3

def printTracks():
    tracks_copy = tracks.copy()
    for cart in carts:
        tracks_copy[cart[0]][cart[1]] = 'o'
    for i in tracks_copy:
        for j in i:
            print(j,end='')
        print()

'''
Create a (4 x nr of carts) matrix where each row denotes a cart: first column is y-axis, second is x-axis, 
third is the next direction in which this cart turns at the next intersection - 0 is left, 1 is straight and 2 is right
and the forth column is the direction it's facing
'''

dirs = [left, up, right, down]
carts = np.ndarray((0,4),int)
for i in range(len(tracks)):
    for j in range(len(tracks[0])):
        if tracks[i][j] == '<':
            carts = np.append(carts,[[i, j, 0, 0]],0)
            tracks[i][j] = '-'
        if tracks[i][j] == '^':
            carts = np.append(carts,[[i,j,0,1]],0)
            tracks[i][j] = '|'
        if tracks[i][j] == '>':
            carts = np.append(carts,[[i,j,0,2]],0)
            tracks[i][j] = '-'
        if tracks[i][j] == 'v':
            carts = np.append(carts,[[i,j,0,3]],0)
            tracks[i][j] = '|'
crash = False
counter = 0
while True:
    crashed_ixs = []
    # get the list of indices order in which the carts move (top->down, left->right) based on their coords
    ixs_order = np.lexsort((carts[:,1], carts[:,0]),0)
    for i in ixs_order:
        if carts[i][0] != -1:
            direction = dirs[carts[i][3]]
            # new y and x
            carts[i][0],carts[i][1] = direction(carts[i][0],carts[i][1])
            y,x = carts[i][0],carts[i][1]
            if tracks[y][x] == '/':
                if is_dir_left():
                    carts[i][3] = 3
                elif is_dir_up():
                    carts[i][3] = 2
                elif is_dir_right():
                    carts[i][3] = 1
                elif is_dir_down():
                    carts[i][3] = 0
            elif tracks[y][x] == '\\':
                if is_dir_left():
                    carts[i][3] = 1
                elif is_dir_up():
                    carts[i][3] = 0
                elif is_dir_right():
                    carts[i][3] = 3
                elif is_dir_down():
                    carts[i][3] = 2
            elif tracks[y][x] == '+':
                # I know that's unreadable but it helped to avoid about 12 "if" statements
                new_dirs = [[3, 0, 1],[0, 1, 2],[1, 2, 3],[2, 3, 0]]
                carts[i][3] = new_dirs[carts[i][3]][carts[i][2]]
                carts[i][2] = (carts[i][2]+1)%3

            # check if there is a crash
            for o in range(len(carts)):
                if carts[o][0] != -1 and i!=o and (carts[o][0], carts[o][1]) == (carts[i][0], carts[i][1]):
                    crash = True
                    print('CRASH - y,x: {},{} '.format(carts[i][1], carts[i][0]))
                    crashed_ixs.append(i)
                    crashed_ixs.append(o)
                    carts[o][:] = -1
                    carts[i][:] = -1
                    break
    # delete carts that crashed in this tick
    carts = np.delete(carts, crashed_ixs, axis=0)
    
    if len(carts)==1:
        print('The location of the last cart is y,x: {},{}'.format(carts[0][1], carts[0][0]))
        break
    counter+=1
