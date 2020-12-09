#read input
with open ('input.txt', 'r') as f:
    sequence = [line[:-1] for line in f.readlines()]

def execute(instuctions: list) -> (int, int):
    executed_instr, pointer, acc = [], 0, 0

    while pointer not in executed_instr and pointer != len(instuctions):

        #retrieve instruction and append line to blacklist
        instr = instuctions[pointer]
        op = instr[:3]
        val = instr[4:]
        executed_instr.append(pointer)

        #execute instruction
        if op == "acc":
            acc += eval(val)
            pointer += 1
        elif op == "jmp":
            pointer += eval(val)
        elif op == "nop":
            pointer += 1
    
    #return if pointer is at end of instructions or instruction was repeated
    return pointer, acc

def part1() -> int:
    return execute(sequence)[1]

def part2() -> int:
    for i, instr in enumerate(sequence):

        op = instr[:3]
        val = instr[4:]

        if op == "jmp":
            sequence[i] = "nop " + val
            pointer, acc = execute(sequence)
            sequence[i] = instr

        elif op == "nop":
            sequence[i] = "jmp " + val
            pointer, acc = execute(sequence)
            sequence[i] = instr

        else:
            continue

        if pointer == len(sequence):
            return acc

if __name__ == "__main__":
    print(f"Solution for part 1: {part1()}")
    print(f"Solution for part 2: {part2()}")