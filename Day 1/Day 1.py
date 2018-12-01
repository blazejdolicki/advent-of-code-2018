from timeit import default_timer as timer

start = timer()

frequencies = open("input.txt").read().split("\n")
init_freq = 0
final_frequency = init_freq

# Part 1

for i in frequencies:
    if len(i) > 0:
        if i[0] == "+":
            final_frequency += int(i[1:])
        if i[0] == "-":
            final_frequency -= int(i[1:])
print("Final frequency ", final_frequency)

# Part 2
reached_frequencies = set()
final_frequency = init_freq
is_finished = False
count = 0

while not is_finished:
    for i in frequencies:
        if len(i) > 0:
            if i[0] == "+":
                final_frequency += int(i[1:])
            if i[0] == "-":
                final_frequency -= int(i[1:])
            if final_frequency in reached_frequencies:
                print("The first frequency reached twice is ",final_frequency)
                print("Size of the set",len(reached_frequencies))
                is_finished = True
                break
            else:
                reached_frequencies.add(final_frequency)
        print(count)
    count+=1

# ...
end = timer()
print("Elapsed time",(end - start)) 