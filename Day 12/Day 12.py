import re
pots = open("input.txt").read().split('\n')

# Filter out empty strings
pots = list(filter(None, pots))
initial_state = list(pots[0].split(' ')[2])

# Count plants in current state
def count_plants():
    sum = 0
    for i in range(len(initial_state)):
        if initial_state[i]=='#':
           sum += i-zero_index
    return sum

# Get rules/patterns
rules={}
for rule in pots[1:]:
    pattern = str(re.search('(.*) =>',rule).group(1))
    result = str(re.search('=> (.*)',rule).group(1))
    rules[pattern] = result

pattern_length = 5
zero_index = 0

def getFirstLastPlant(state, zero_index):
    # Get indices of plants
    indices = [i for i, a in enumerate(''.join(state)) if a == '#']

    first_plant_index = indices[0]
    dist_from_start = first_plant_index

    if dist_from_start <= 5 or zero_index<=5:
        start = (5-min(dist_from_start,zero_index))
        state = start * ['.'] + state
        zero_index += start
    else:
        state = state[zero_index-5:]
        zero_index -= zero_index-5
    indices = [i for i, a in enumerate(''.join(state)) if a == '#']
    last_plant_index = indices[-1]
    dist_from_end = len(state)-1-last_plant_index
    if dist_from_end<=5:
        end = (5 - dist_from_end)
        state = state+end*['.']
    else:
        state = state[:last_plant_index+6]
    return state,zero_index


initial_state, zero_index = getFirstLastPlant(initial_state,zero_index)
previous_state_sum = 0
def get_state_after_n_generations(generations):
    global initial_state, zero_index
    for i in range(generations):
        current_state_sum = count_plants()

        # Check if there is any pattern because counting 50000000000 generations is too much even for
        # some crazy data structure written in C
        # Credits: https://www.reddit.com/r/adventofcode/comments/a5eztl/2018_day_12_solutions/ebm4c9d
        # print(i, current_state_sum,previous_state_sum, abs(current_state_sum-previous_state_sum))
        previous_state_sum = count_plants()
        new_initial_state=['']*len(initial_state)

        for j in range(len(initial_state)):
            for pattern in rules:
                found = False
                for l in range(-2,3):

                    if j+l in range(len(initial_state)):
                        if initial_state[j+l] != pattern[l+2]:
                            break
                    else:
                        new_initial_state[j] = '.'
                        found = True
                        break
                    if l==2:

                        new_initial_state[j] = rules[pattern]
                        found = True
                        break

                if found:
                    break

            if new_initial_state[j]=="":
                new_initial_state[j] = '.'
        initial_state, zero_index = getFirstLastPlant(new_initial_state,zero_index)
    print("After {} generations there are {} plants".format(generations,count_plants()))

# Part 2
# From 100th generation onwards each generation has 78 more plants than the previous one
print("Part 1")
get_state_after_n_generations(20)

# Part 2
# From 100th generation onwards each generation has 78 more plants than the previous one
print("Part 2")
get_state_after_n_generations(200)
print("After {} generations there are {} plants".format(50000000000, (50000000000-200)*78+count_plants()))
