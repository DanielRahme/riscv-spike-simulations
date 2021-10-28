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

def write_to_csv(freq_instructs, outfile):
    import csv
    output_filename = outfile
    with open(output_filename, 'w') as f:
        w = csv.writer(f)
        w.writerows(freq_instructs.items())

    print ("Created file " + output_filename)

def print_bar_chart(filepath, data):
    names = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(names, values)

    fig.suptitle('Instruction frequency')
    plt.xticks(rotation=90)
    ax.set_ylabel('Freq')
    ax.set_xlabel('Instruction')

    bar_chart_file = filepath + "_barchart.png"

    plt.tick_params(axis='x', which='major', labelsize=7)

    plt.savefig(bar_chart_file, dpi=300)
    #plt.show()

def print_pie_chart(filepath, data):
    labels = list(data.keys())
    sizes = list(data.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    pie_chart_file = filepath + "_piechart.png"
    plt.savefig(pie_chart_file, dpi=300)
    #plt.show()

def main(input_file, output_path):
    freq_instructs = dict(extract_instructions(input_file))
    write_to_csv(freq_instructs, output_path)
    print_bar_chart(output_path, freq_instructs)
    print_pie_chart(output_path, freq_instructs)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
