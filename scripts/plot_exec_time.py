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
    instructs = pd.read_csv(sys.stdin, names=["Instruct", "Count"])
    return instructs


def calc_instr_cycle(instr, cycles):
    time = 0
    if instr not in cpi_list:
        time = cycles
    else:
        cpi = cpi_list.get(instr)
        time = cpi * cycles

    return time

def calc_cycles(instr_frame):

    instruction_cycles = []

    for idx, row in instr_frame.iterrows():
        instruction_cycles.append(calc_instr_cycle(row["Instruct"], row["Count"]))

    return instruction_cycles


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
    limit = 0.04
    time_limit = total_exec_time * limit


    df_req = df.loc[
            (df['Category'] == 'load')    |
            (df['Category'] == 'store')   |
            (df['Category'] == 'addi')    |
            (df['Category'] == 'branch')
            ]

    df_res = df[df['Exec time'] > time_limit]
    df_res = df_res.append(df_req)
    df_res = df_res.drop_duplicates()
    df_res = df_res.sort_values(by=['Exec time'], ascending=False)
    df_res['Percent'] = 100 * df_res['Exec time'] / total_exec_time

    #### Plot results
    labels = df_res['Category']
    percent = df_res['Percent']
    y_pos = np.arange(len(df_res['Exec time']))

    fig, ax = plt.subplots()
    ax.grid(axis='x', zorder=0)
    ax.barh(y_pos, percent, align='center', height=0.4, zorder=3, color='Red')
    ax.set_yticks(y_pos, labels=labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Execution time [%]')
    ax.set_ylabel('Instruction type')
    plt.xlim([0, 40])

    for index, value in enumerate(percent):
        plt.text(value, index, str("{:.2f}".format(value)))

    fig.suptitle("Dynamic Execution Time Per Instruction Type")
    ax.set_title(case_name)

    #plt.show()
    suffix = "-exec-time.png"
    file_name = save_path + case_name + suffix
    plt.savefig(file_name, dpi=300, bbox_inches='tight')



def main(case_name, save_path):
    clock_freq_mhz = 200 

    data_frame = read_instruct_csv_to_frame()
    data_frame["Cycles"] = calc_cycles(data_frame)
    data_frame["Exec time"] = data_frame['Cycles'] / clock_freq_mhz
    data_frame = create_categories(data_frame)
    cat_frame = filter_categories(data_frame)
    plot_exec_time(case_name, save_path, cat_frame)


if __name__ == "__main__":
    import sys
    main(sys.argv[1],sys.argv[2])
