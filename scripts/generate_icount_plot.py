import sys
import matplotlib.pyplot as plt

def read_instruct_csv():
    instruction_count = {}
    for line in sys.stdin:
        instr, count = line.split(",")
        instruction_count[instr] = int(count)

    return instruction_count


def plot_icount(case_name, save_path, data):
    names = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(names, values)
    fig.suptitle('Instruction count')
    ax.set_title(case_name)
    plt.xticks(rotation=90)
    plt.tick_params(axis='x', which='major', labelsize=7)
    ax.set_ylabel('Count')
    ax.set_xlabel('Instruction')

    file_name = save_path + case_name + "-icount.png"
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def main(case_name, save_path):
    instructs = read_instruct_csv()
    plot_icount(case_name, save_path, instructs)


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
