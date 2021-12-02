import csv
import os.path
import matplotlib.pyplot as plt

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
        'lw': 2,
        'c.lw': 2,
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


def print_bar_chart(file_prefix, data):
    names = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(names, values)

    fig.suptitle('Instruction frequency')
    plt.xticks(rotation=90)
    plt.tick_params(axis='x', which='major', labelsize=7)
    ax.set_ylabel('Freq')
    ax.set_xlabel('Instruction')

    bar_chart_file = file_prefix + "-barchart.png"
    plt.savefig(bar_chart_file, dpi=300)

def print_pie_chart(file_prefix, data):
    labels = list(data.keys())
    sizes = list(data.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    pie_chart_file = file_prefix + "-piechart.png"
    plt.savefig(pie_chart_file, dpi=300)

def main(input_file):
    import os

    clock_freq_mhz = 200 
    case_name = os.path.basename(input_file).removesuffix("-freq-instruct.csv")

    instructs = read_instruct_csv(input_file)
    inst_count = sum(instructs.values())
    cycles = calc_cycles(instructs)
    exec_time = cycles / clock_freq_mhz

    print(case_name + "," + str(inst_count) + "," + str(cycles) + "," + str(exec_time))
    print_bar_chart(input_file, instructs)
    print_pie_chart(input_file, instructs)


if __name__ == "__main__":
    import sys
    main(sys.argv[1])
