import csv
import os.path

float_instructions = {
# Sign inject
        'fabs.s': 3,
        'fsgnj.s': 3,
        'fsgnjn.s': 3,
        'fsgnjx.s': 3,

# Arithmetic
        'fadd.s': 2,
        'fsub.s': 2,
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
        'flw': 2,
        'fsw': 2,
        'c.flw': 2,
        'c.fsw': 2,
        'c.flwsp': 2
}


def read_instruct_csv(csv_file):
    with open(csv_file, mode='r', newline='') as fp:
        dictreader = csv.reader(fp, delimiter=',')
        dict_from_csv = {rows[0]:int(rows[1]) for rows in dictreader}

    return dict_from_csv


def calc_cycles(instructs):
        cycles = 0

        for inst, count in instructs.items():
            # Single cycle instructions
            if inst not in float_instructions:
                cycles += count

            # Multi-cycle instructions
            else:
                cpi = float_instructions.get(inst)
                cycles += cpi * count

        return cycles


def write_to_csv(in_file, count, cycles, file_path):
    output_filename = file_path + "results.csv"
    test_case = in_file.removesuffix("-freq-instruct.csv")

    file_exists = os.path.exists(output_filename)
    if (file_exists):
        # Append results to existing results file
        with open(output_filename, 'a') as f:
            w = csv.writer(f)
            w.writerow([test_case,count,cycles])

    # Write CSV header on first row. Create new CSV.
    else:
        with open(output_filename, 'w') as f:
            w = csv.writer(f)
            w.writerow(['test','count','cycles'])
            w.writerow([test_case,count,cycles])


def main(input_file, output_prefix):
    instructs = read_instruct_csv(input_file)
    inst_count = sum(instructs.values())
    cycles = calc_cycles(instructs)
    write_to_csv(input_file, inst_count, cycles, output_prefix)


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
