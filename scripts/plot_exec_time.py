import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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

cat_lui = [ "lui", "c.lui" ]

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

# Read innput
def read_instruct_csv_to_frame():
    instructs = pd.read_csv(sys.stdin, names=["Instruct", "Cycles"])
    return instructs


def calc_instr_cycle(instr, cycles):
    time = 0
    if instr not in cpi_list:
        time = cycles
    else:
        cpi = cpi_list.get(instr)
        time = cpi * cycles

    return time

def calc_instruction_time(instr_frame):

    exec_times = []

    for idx, row in instr_frame.iterrows():
        exec_times.append(calc_instr_cycle(row["Instruct"], row["Cycles"]))

    instr_frame["Exec time"] = exec_times

    return instr_frame


def create_categories(df):
    df.loc[df["Instruct"].isin(cat_load), "Category"] = "load"
    df.loc[df["Instruct"].isin(cat_fload), "Category"] = "fload"
    df.loc[df["Instruct"].isin(cat_store), "Category"] = "store"
    df.loc[df["Instruct"].isin(cat_fstore), "Category"] = "fstore"
    df.loc[df["Instruct"].isin(cat_add), "Category"] = "add"
    df.loc[df["Instruct"].isin(cat_fadd), "Category"] = "fadd"
    df.loc[df["Instruct"].isin(cat_sub), "Category"] = "sub"
    df.loc[df["Instruct"].isin(cat_fsub), "Category"] = "fsub"
    df.loc[df["Instruct"].isin(cat_addi), "Category"] = "addi"
    df.loc[df["Instruct"].isin(cat_lui), "Category"] = "lui"
    df.loc[df["Instruct"].isin(cat_fmove), "Category"] = "fmove"
    df.loc[df["Instruct"].isin(cat_fmac), "Category"] = "fmac"
    df.loc[df["Instruct"].isin(cat_mult_div), "Category"] = "mult_div"
    df.loc[df["Instruct"].isin(cat_fmult_div), "Category"] = "fmult_div"
    df.loc[df["Instruct"].isin(cat_branch), "Category"] = "branch"
    df.loc[df["Instruct"].isin(cat_logical), "Category"] = "logical"
    df.loc[df["Instruct"].isin(cat_other), "Category"] = "other"
    return df

def filter_categories(df):
    cat_labels = ["load", "fload", "store", "fstore", "add", "fadd", "sub", "fsub", "addi", "lui",
"fmove", "fmac", "mult_div", "fmult_div", "branch", "logical", "other"
]

    cat_total_cycles = []
    cat_total_exec = []

    for label in cat_labels:
        current_cat = df[df["Category"] == label]
        cat_total_cycles.append(current_cat["Cycles"].sum())
        cat_total_exec.append(current_cat["Exec time"].sum())
        

    df_cat = {
            "Category" : cat_labels,
            "Cycles" : cat_total_cycles,
            "Exec time" : cat_total_exec
            }

    df_cat = pd.DataFrame(df_cat)
    return df_cat


def plot_exec_time(case_name, save_path, df):
    df = df.sort_values(by=['Exec time'], ascending=False)
    exec_time = df['Exec time']
    total_exec_time = df['Exec time'].sum()

    labels = df['Category']

    percent = 100 * exec_time / total_exec_time
    y_pos = np.arange(len(exec_time))


    #### Plot results
    fig, ax = plt.subplots()
    ax.grid(axis='x', zorder=0)
    ax.barh(y_pos, percent, align='center', height=0.4, zorder=3)
    ax.set_yticks(y_pos, labels=labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Percent %')
    plt.xlim([0, 40])

    for index, value in enumerate(percent):
        plt.text(value, index, str("{:.2f}".format(value)))

    fig.suptitle("Execution time per instruction category")
    ax.set_title(case_name)

    plt.show()
    #suffix = "-exec-time.png"
    #file_name = save_path + case_name + suffix
    #plt.savefig(file_name, dpi=300, bbox_inches='tight')




def main(case_name, save_path):
    clock_freq_mhz = 200 

    data_frame = read_instruct_csv_to_frame()
    data_frame = calc_instruction_time(data_frame)
    data_frame = create_categories(data_frame)
    cat_frame = filter_categories(data_frame)

    #plot_category_cycles(case_name, save_path, cat_frame)
    plot_exec_time(case_name, save_path, cat_frame)


if __name__ == "__main__":
    import sys
    main(sys.argv[1],sys.argv[2])
