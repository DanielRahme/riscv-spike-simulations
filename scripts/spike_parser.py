# Extract instructions from tracelog generated from Spike.
# Output the frequency of instructions used. 
import collections

def extract_instructions(filename):

    instructs = []

    with open(filename) as f:
        for line in f:
            instructs.append(line.split()[4])
    #c = collections.Counter(instructs)
    #print(dict(c))
    return collections.Counter(instructs)

def write_to_csv(freq_instructs, outfile):
    import csv
    output_filename = outfile
    with open(output_filename, 'w') as f:
        w = csv.writer(f)
        w.writerows(freq_instructs.items())

    print ("Created file " + output_filename)


def main(filename, output_name):
    freq_instructs = extract_instructions(filename)
    write_to_csv(dict(freq_instructs), output_name)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
