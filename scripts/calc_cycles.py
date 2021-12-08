import csv
import os.path
import matplotlib.pyplot as plt
import numpy as np

float_instructions = {
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
    count_lsm = 0
    count_as = 0
    count_mac = 0
    count_muldiv = 0
    count_branch = 0
    count_logical = 0
    count_app = 0
    count_other = 0
    count_not_def = 0

    ## The categories
    load_store_move = ["c.sw","c.flwsp","c.fswsp","li","c.swsp","c.lwsp", "c.flw", "c.fsw", "c.lw",
            "c.mv", "c.li", "c.lui","lui", "lb", "lh", "lw", "lbu", "lhu", "sb", "sh", "sw", "flw",
            "fsw", "fmv.x.w", "fmv.w.x", "mv" ]

    add_sub = ["c.add","c.addi16sp", "auipc", "c.addi","addi", "add","c.sub", "sub", "fadd.s",
            "fsub.s", "c.addi4spn" ]
    mac = ["fmadd.s", "fmsub.s", "fnmsub.s", "fnmadd.s"]

    mult_div = ["mul","mulh","mulhsu","mulhu","div","divu","rem","remu","fmul.s","fdiv.s"]

    branch = ["c.bnz","c.j","beqz","c.jal","jal", "jalr", "beq", "bne", "blt", "bge", "bltu",
            "bgeu", "c.jalr", "c.jr", "c.beqz", "bnez", "c.bnez"
            ]
    logical = ["slti","sltiu","xori","ori","andi","c.slli","slli","srli","srai","sll","slt","sltu"
            , "xor","srl","sra","or","and","feq.s","flt.s","fle.s", "c.or", "c.and", "c.xor",
            "c.andi", "c.srai", "c.srli", "snez" ] 

    application = ["ret","fence", "ecall", "ebreak", "c.ebreak", "c.nop" ]

    other = ["fsqrt.s","fsgnj.s","fsgnjn.s","fsgnjx.s","fmin.s","fmax.s","fcvt.w.s",
            "fcvt.wu.s","fclass.s","fcvt.s.w","fcvt.s.wu"] 

    for inst, count in data.items():
        # Single cycle instructions
        if inst in load_store_move:
            count_lsm += count
        elif inst in add_sub:
            count_as += count
        elif inst in mac:
            count_mac += count
        elif inst in mult_div:
            count_muldiv += count
        elif inst in branch:
            count_branch += count
        elif inst in logical:
            count_logical += count
        elif inst in application:
            count_app += count
        elif inst in other:
            count_other += count
        else:
            count_not_def += count
            print("Instruction <" + inst + "> is not defined in a bin")


    labels = ["load/store/move", "add/sub", "mac", "mult/div", "branch", "logical", "application",
            "other", "not defined"]

    categories = [count_lsm, count_as, count_mac, count_muldiv, count_branch, count_logical, count_app, count_other, count_not_def]

    tot = sum(categories)
    percent = [100 * x/tot for x in categories]
    y_pos = np.arange(len(labels))

    fig, ax = plt.subplots()
    plt.grid(axis = 'x')
    ax.barh(y_pos, percent, align='center', height=0.4)
    ax.set_yticks(y_pos, labels=labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Percent %')
    plt.xlim([0, 50])

    for index, value in enumerate(percent):
        plt.text(value, index, str("{:.2f}".format(value)))

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
