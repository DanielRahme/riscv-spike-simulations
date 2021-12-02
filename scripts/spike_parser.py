# Extract instructions from tracelog generated from Spike.
# Output the frequency of instructions used. 
# Create bar chart and pie chart
import collections

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


def main(input_file):
    freq_instructs = dict(extract_instructions(input_file))
    print_results(freq_instructs)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
