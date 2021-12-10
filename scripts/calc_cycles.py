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
    count_load = 0
    count_store = 0
    count_add = 0
    count_fadd = 0
    count_sub = 0
    count_fsub = 0
    count_addi = 0
    count_move = 0
    count_fmove = 0
    count_fmac = 0
    count_mult_div = 0
    count_fmult_div = 0
    count_branch = 0
    count_logical = 0
    count_other = 0

    ## The categories
    cat_load = [
            "flw",
            "c.flw",
            "c.flwsp",
            "c.lwsp",
            "c.lw",
            "lb",
            "lh",
            "lw",
            "lbu",
            "lhu"
            ]

    cat_store = [
            "c.sw",
            "c.fsw",
            "c.fswsp",
            "c.swsp",
            "sb",
            "sh",
            "sw",
            "fsw"
            ]

    cat_add = [
            "c.mv",
            "c.add",
            "add"
    ]
    cat_fadd = [
            "fadd.s",
            ]

    cat_sub = [
            "c.sub",
            "sub",
            ]

    cat_fsub = [
            "fsub.s",
            ]

    cat_addi = [
            "c.li",
            "li",
            "mv",
            "c.addi",
            "addi",
            "c.addi16sp",
            "auipc",
            "c.addi4spn" 
            ]


    cat_move = [
            "lui",
            "c.lui"
            ]
    cat_fmove = [
            "fmv.x.w",
            "fmv.w.x"
            ]


    cat_fmac = [
            "fmadd.s",
            "fmsub.s",
            "fnmsub.s",
            "fnmadd.s"
            ]

    cat_mult_div = [
            "mul",
            "mulh",
            "mulhsu",
            "mulhu",
            "div",
            "divu",
            "rem",
            "remu"
            ]

    cat_fmult_div = [
            "fmul.s",
            "fdiv.s"
            ]

    cat_branch = ["c.bnz",
            "c.j",
            "beqz",
            "c.jal",
            "jal",
            "jalr",
            "beq",
            "bne",
            "blt",
            "bge",
            "bltu",
            "bgeu",
            "c.jalr",
            "c.jr",
            "c.beqz",
            "bnez",
            "c.bnez"
            ]
    cat_logical = ["slti",
            "sltiu",
            "xori",
            "ori",
            "andi",
            "c.slli",
            "slli",
            "srli",
            "srai",
            "sll",
            "slt",
            "sltu",
            "xor",
            "srl",
            "sra",
            "or",
            "and",
            "feq.s",
            "flt.s",
            "fle.s",
            "c.or",
            "c.and",
            "c.xor",
            "c.andi",
            "c.srai",
            "c.srli",
            "snez" 
            ] 

    cat_other = ["fsqrt.s",
            "fsgnj.s",
            "fsgnjn.s",
            "fsgnjx.s",
            "fmin.s",
            "fmax.s",
            "fcvt.w.s",
            "fcvt.wu.s",
            "fclass.s",
            "fcvt.s.w",
            "fcvt.s.wu",
            "ret",
            "fence",
            "ecall",
            "ebreak",
            "c.ebreak",
            "c.nop" 
            ]

    for inst, count in data.items():
        if inst in cat_load:
            count_load += count
        elif inst in cat_store:
            count_store += count
        elif inst in cat_add:
            count_add += count
        elif inst in cat_fadd:
            count_fadd += count
        elif inst in cat_sub:
            count_sub += count
        elif inst in cat_fsub:
            count_fsub += count
        elif inst in cat_addi:
            count_addi += count
        elif inst in cat_move:
            count_move += count
        elif inst in cat_fmove:
            count_fmove += count
        elif inst in cat_fmac:
            count_fmac += count
        elif inst in cat_mult_div:
            count_mult_div += count
        elif inst in cat_fmult_div:
            count_fmult_div += count
        elif inst in cat_branch:
            count_branch += count
        elif inst in cat_logical:
            count_logical += count
        elif inst in cat_other:
            count_other += count
        else:
            try:
                raise NameError('Instruction not in a category')
            except NameError:
                #print('Not defined instruction found.')
                raise


    labels = [
        "load", "store", "add" , "fadd", "sub",
        "fsub" , "addi", "move", "fmove", "fmac",
        "mult_div", "fmult_div", "branch", "logical", "other"
            ]

    categories = [ 
            count_load, count_store, count_add, 
            count_fadd, count_sub, count_fsub, 
            count_addi, count_move, count_fmove,
            count_fmac, count_mult_div, count_fmult_div,
            count_branch, count_logical, count_other
            ]

    tot = sum(categories)
    percent = [100 * x/tot for x in categories]
    y_pos = np.arange(len(labels))

    ### Plot results
    fig, ax = plt.subplots()
    ax.grid(axis='x', zorder=0)
    ax.barh(y_pos, percent, align='center', height=0.4, zorder=3)
    ax.set_yticks(y_pos, labels=labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Percent %')
    plt.xlim([0, 50])

    for index, value in enumerate(percent):
        plt.text(value, index, str("{:.2f}".format(value)))

    case_name = os.path.basename(file_prefix).removesuffix("-freq-instruct.csv")
    fig.suptitle(case_name)
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
