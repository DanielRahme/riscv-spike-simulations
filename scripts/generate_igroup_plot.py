import sys
import matplotlib.pyplot as plt
import numpy as np

def read_instruct_csv():
    instruction_count = {}
    for line in sys.stdin:
        instr, count = line.split(",")
        instruction_count[instr] = int(count)

    return instruction_count


def plot_igroup(case_name, save_path, data):
    count_load = count_fload = count_store = count_fstore = count_add = 0
    count_fadd = count_sub = count_fsub = count_addi = count_move = 0
    count_fmove = count_fmac = count_mult_div = count_fmult_div = 0
    count_branch = count_logical = count_other = 0

    ## The categories
    cat_load = [ "c.lwsp", "c.lw", "lb", "lh", "lw", "lbu", "lhu" ]

    cat_fload = [ "flw", "c.flw", "c.flwsp" ]

    cat_store = [ "c.sw", "c.swsp", "sb", "sh", "sw" ]

    cat_fstore = [ "c.fsw", "c.fswsp", "fsw" ]

    cat_add = [ "c.mv", "c.add", "add" ]

    cat_fadd = [ "fadd.s", ]

    cat_sub = [ "c.sub", "sub" ]

    cat_fsub = [ "fsub.s" ]

    cat_addi = [ "c.li", "li", "mv", "c.addi", "addi", "c.addi16sp", "auipc", "c.addi4spn" ]

    cat_move = [ "lui", "c.lui" ]

    cat_fmove = [ "fmv.x.w", "fmv.w.x" ]

    cat_fmac = [ "fmadd.s", "fmsub.s", "fnmsub.s", "fnmadd.s" ]

    cat_mult_div = [ "mul", "mulh", "mulhsu", "mulhu", "div", "divu", "rem", "remu" ]

    cat_fmult_div = [ "fmul.s", "fdiv.s" ]

    cat_branch = ["c.bnz", "c.j", "beqz", "c.jal", "jal", "jalr", "beq", "bne",
            "blt", "bge", "bltu", "bgeu", "c.jalr", "c.jr", "c.beqz", "bnez", "c.bnez" ]

    cat_logical = ["slti", "sltiu", "xori", "ori", "andi", "c.slli", "slli", "srli",
            "srai", "sll", "slt", "sltu", "xor", "srl", "sra", "or", "and", "feq.s",
            "flt.s", "fle.s", "c.or", "c.and", "c.xor", "c.andi", "c.srai", "c.srli",
            "snez" ] 

    cat_other = ["fsqrt.s", "fsgnj.s", "fsgnjn.s", "fsgnjx.s", "fmin.s", "fmax.s",
            "fcvt.w.s", "fcvt.wu.s", "fclass.s", "fcvt.s.w", "fcvt.s.wu", "ret",
            "fence", "ecall", "ebreak", "c.ebreak", "c.nop" ]

    for inst, count in data.items():
        if inst in cat_load:
            count_load += count
        elif inst in cat_fload:
            count_fload += count
        elif inst in cat_store:
            count_store += count
        elif inst in cat_fstore:
            count_fstore += count
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


    labels_req = ["load", "store", "branch", "addi"]
    categories_req = [count_load, count_store, count_branch, count_addi]

    labels_rest = [
        "f.load","f.store", "add" , "f.add", "sub",
        "f.sub", "move", "f.move", "f.mac",
        "mult_div", "f.mult_div", "logical", "other"
            ]

    categories_rest = [ 
            count_fload, count_fstore, count_add, 
            count_fadd, count_sub, count_fsub, 
            count_move, count_fmove,
            count_fmac, count_mult_div, count_fmult_div,
            count_logical, count_other
            ]

    tot = sum(categories_rest) + sum(categories_req)
    percent_rest = [100 * x/tot for x in categories_rest]

    labels = labels_req
    percent = [100 * x/tot for x in categories_req]
    threshold = 6.0

    ### Filter out categories below threshold limit
    for i in range(len(categories_rest)):
        if (percent_rest[i] >= threshold):
            labels.append(labels_rest[i])
            percent.append(percent_rest[i])


    ### Plot results
    y_pos = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.grid(axis='x', zorder=0)
    ax.barh(y_pos, percent, align='center', height=0.4, zorder=3)
    ax.set_yticks(y_pos, labels=labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Percent %')
    plt.xlim([0, 40])

    for index, value in enumerate(percent):
        plt.text(value, index, str("{:.2f}".format(value)))

    fig.suptitle("Instruction count proportion by groups")
    ax.set_title(case_name)

    file_name = save_path + case_name + "-igroup-percent.png"
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def main(case_name, save_path):
    instructs = read_instruct_csv()
    plot_igroup(case_name, save_path, instructs)


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
