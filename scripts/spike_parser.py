# Extract instructions from tracelog generated from Spike.
# Output the frequency of instructions used. 
# Create bar chart and pie chart
import collections
import matplotlib.pyplot as plt

def extract_instructions(filename):
    exception_found = False
    instructs = []

    with open(filename) as f:
        for line in f:
            words = line.split()

            if (words[2] != "exception" and not(exception_found)):
                instructs.append(words[4])

            elif (words[2] == "exception"):
                exception_found = True

            # Handles the tval instruction
            elif (len(words) < 5 and exception_found):  
                pass

            elif (exception_found):
                if (words[4] == "sret"):
                    exception_found = False

    return collections.Counter(instructs)

def print_results(freq_instructs):
    for op, count in freq_instructs.items():
        print(op + "," + str(count))

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
    #plt.show()

def print_pie_chart(file_prefix, data):
    labels = list(data.keys())
    sizes = list(data.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    pie_chart_file = file_prefix + "-piechart.png"
    plt.savefig(pie_chart_file, dpi=300)
    #plt.show()

def main(input_file, output_prefix):
    freq_instructs = dict(extract_instructions(input_file))
    print_results(freq_instructs)
    print_bar_chart(output_prefix, freq_instructs)
    print_pie_chart(output_prefix, freq_instructs)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
