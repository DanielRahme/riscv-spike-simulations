import sys

cpi_list = {
# Sign inject
        'fabs.s': 3,
        'fsgnj.s': 3,
        'fsgnjn.s': 3,
        'fsgnjx.s': 3,

# Arithmetic
        'fadd.s': 2,
        'fsub.s': 2,
        'remu': 6,
        'rem': 6,
        'divu': 6,
        'div': 6,
        'fdiv.s': 6,
        'fmul.s': 2,
        'fsqrt.s': 6,
        'fmadd.s': 2,
        'fmsub.s': 2,

# Negate arithmetic
        'fneg.s': 3,
        'fnmadd.s': 2,
        'fnmsub.s': 2,

# Compare
        'fmax.s': 3,
        'fmin.s': 3,
        
# Move
        'fmv.s': 3,

# Load Store
        'lh': 2,
        'lhu': 2,
        'lb': 2,
        'lbu': 2,
        'lw': 2,
        'c.lw': 2,
        'flw': 2,
        'fsw': 2,
        'c.flw': 2,
        'c.fsw': 2,
        'c.flwsp': 2
}


def read_instruct_csv():
    instruction_count = {}
    for line in sys.stdin:
        instr, count = line.split(",")
        instruction_count[instr] = int(count)

    return instruction_count


def calc_cycles(instructs):
        cycles = 0

        for inst, count in instructs.items():
            # Single cycle instructions
            if inst not in cpi_list:
                cycles += count

            # Multi-cycle instructions
            else:
                cpi = cpi_list.get(inst)
                cycles += cpi * count

        return cycles

def main(case_name):
    clock_freq_mhz = 200 

    instructs = read_instruct_csv()
    cycles = calc_cycles(instructs)
    exec_time = cycles / clock_freq_mhz

    total_instruction_count = sum(instructs.values())

    print(case_name + "," + str(total_instruction_count) + "," + str(cycles) + "," + str(exec_time))


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
