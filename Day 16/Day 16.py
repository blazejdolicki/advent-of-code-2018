import re

samples = open("input.txt").read().split('\n\n')[:-2]

# create a new list with all samples
new_samples = [[] for i in range(len(samples))]
for i in range(len(samples)):
    split = samples[i].split('\n')
    for line in split:
        numbers = re.findall('\d+', line)
        numbers = list(map(int,numbers))
        new_samples[i].append(numbers)


def is_opcode_consistent(result,output):
    return int(result == output)

def addr(input, instructionA, instructionB):
    operation = input[instructionA] + input[instructionB]
    return operation

def addi(input, instructionA, instructionB):
    operation = input[instructionA] + instructionB
    return operation


def mulr(input, instructionA, instructionB):
    operation = input[instructionA] * input[instructionB]
    return operation


def muli(input, instructionA, instructionB):
    operation = input[instructionA] * instructionB
    return operation


def banr(input, instructionA, instructionB):
    operation = input[instructionA] & input[instructionB]
    return operation


def bani(input, instructionA, instructionB):
    operation = input[instructionA] & instructionB
    return operation


def borr(input, instructionA, instructionB):
    operation = input[instructionA] | input[instructionB]
    return operation


def bori(input, instructionA, instructionB):
    operation = input[instructionA] | instructionB
    return operation


def setr(input, instructionA, instructionB):
    operation = input[instructionA]
    return operation


def seti(input, instructionA,instructionB):
    operation = instructionA
    return operation

def gtir(input, instructionA, instructionB):
    operation = int(instructionA>input[instructionB])
    return operation


def gtri(input,instructionA, instructionB):
    operation = int(input[instructionA] > instructionB)
    return operation


def gtrr(input,instructionA, instructionB):
    operation = int(input[instructionA] > input[instructionB])
    return operation



def eqir(input, instructionA, instructionB):
    operation = int(instructionA == input[instructionB])
    return operation


def eqri(input, instructionA, instructionB):
    operation = int(input[instructionA] == instructionB)
    return operation


def eqrr(input, instructionA, instructionB):
    operation = int(input[instructionA] == input[instructionB])
    return operation


def check_opcodes(extract):
    possible_opcodes = set()
    input = extract[0]
    instructionA = extract[1][1]
    instructionB = extract[1][2]
    instructionC = extract[1][3]
    output = extract[2]
    working_opcodes_amount = 0

    def isOpCodeWorking(func):
        print(func)
        result = input.copy()
        result[instructionC] = func(input,instructionA,instructionB)
        # print('after', result)
        print(func)
        if is_opcode_consistent(result, output) and func not in opcodes_encodings:
            possible_opcodes.add(func)
        return is_opcode_consistent(result, output)

    working_opcodes_amount += isOpCodeWorking(addr)
    working_opcodes_amount += isOpCodeWorking(addi)
    working_opcodes_amount += isOpCodeWorking(mulr)
    working_opcodes_amount += isOpCodeWorking(muli)
    working_opcodes_amount += isOpCodeWorking(banr)
    working_opcodes_amount += isOpCodeWorking(bani)
    working_opcodes_amount += isOpCodeWorking(borr)
    working_opcodes_amount += isOpCodeWorking(bori)
    working_opcodes_amount += isOpCodeWorking(setr)
    working_opcodes_amount += isOpCodeWorking(seti)
    working_opcodes_amount += isOpCodeWorking(gtir)
    working_opcodes_amount += isOpCodeWorking(gtri)
    working_opcodes_amount += isOpCodeWorking(gtrr)
    working_opcodes_amount += isOpCodeWorking(eqir)
    working_opcodes_amount += isOpCodeWorking(eqri)
    working_opcodes_amount += isOpCodeWorking(eqrr)

    return working_opcodes_amount, possible_opcodes

# Part 1

total_sum = 0
opcodes_encodings = [None for i in range(16)]

for i in new_samples:
    working_opcodes_amount,candidate_opcodes = check_opcodes(i)
    print(candidate_opcodes)
    if working_opcodes_amount>=3:
        total_sum += 1
    if len(candidate_opcodes)==1:
        opcode_encoded = int(i[1][0])
        opcodes_encodings[opcode_encoded] = candidate_opcodes.pop()
        print(i,'is resolved with',opcodes_encodings[opcode_encoded])
print('Total sum',total_sum)

# Part 2

test = open("input.txt").read().split('\n\n')[-1]
instructions = test.split('\n')[:-1]
register = [0,0,0,0]
for i in range(len(instructions)):
    print('before',register)
    instruction = instructions[i].split(' ')
    instruction = list(map(int,instruction))
    operation_encoding = instruction[0]
    instructionA = instruction[1]
    instructionB = instruction[2]
    instructionC = instruction[3]
    operation = opcodes_encodings[operation_encoding]
    register[instructionC] = operation(register,instructionA,instructionB)
    print('instruction',instruction)
    print('opcode',operation.__name__)
    print('after',register)
print('Registers after executing the program', register)
