box_ids = open("input.txt").read().split("\n")

# Part 1
two_occurrences = 0
three_occurrences = 0
for box in box_ids:
    box_occurrences = {}
    for char in box:
        if char in box_occurrences:
            box_occurrences[char] += 1
        else:
            box_occurrences[char] = 1
    two_found = False
    three_found = False
    for key in box_occurrences:
        if not two_found and box_occurrences[key]==2:
            two_occurrences += 1
            two_found = True
        if not three_found and box_occurrences[key]==3:
            three_occurrences += 1
            three_found = True
print("{} box IDs contain a letter which appers twice ".format(two_occurrences))
print("{} box IDs contain a letter which appears three times ".format(three_occurrences))
print("The checksum of the list is",three_occurrences*two_occurrences)

# Part 2
found = False
box_ids = box_ids[:-1]
length = 26

# Quick check if all the box IDs have the same length
for box in box_ids:
    if not len(box)==length:
        print("Different length")
        break

for box1 in box_ids:
    if found:
        break
    for box2 in box_ids:
        different_chars = 0
        for i in range(len(box1)):
            if not box1[i] == box2[i]:
                different_chars += 1
        if different_chars == 1:
            print("The similar box IDs are {} and {}".format(box1, box2))
            for i in range(len(box1)):
                if not box1[i] == box2[i]:
                    print("Different char:\nindex: {} char - box1: {} char - box2: {}".format(i,box1[i],box2[i]))
                    print("Similar part ",box1.replace(box1[i],"",1))
            found = True
            break
