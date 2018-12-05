import string

initial_polymer = open("input.txt").read().strip()

# Part 1
def reactPolymer(polymer):
    i = 0
    while i<len(polymer)-1:
        case = polymer[i].isupper()
        case_next = polymer[i+1].isupper()
        if case != case_next:
            if polymer[i].lower() == polymer[i+1].lower():
                polymer = polymer.replace(polymer[i:i+2], "", 1)
                i = max(-1,i-2)
        i += 1
    print("Length of the polymer in the end",len(polymer))
    return len(polymer)


reactPolymer(initial_polymer)

# Part 2
letters = list(string.ascii_lowercase)
shortest_polymer_length = 50000
for i in letters:
    print("Letter",i)
    polymer1 = initial_polymer.replace(i,"")
    polymer1 = polymer1.replace(i.upper(), "")
    new_polymer_length = reactPolymer(polymer1)

    if new_polymer_length < shortest_polymer_length:
        shortest_polymer_length = new_polymer_length

print("Shortest polymer length",shortest_polymer_length)


