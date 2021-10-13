# Find start address of main
# and return address from main


def extract_address(filename):
    main_found = False
    main_address = ""
    ret_address = ""

    #with open('objdump.txt') as f:
    with open(filename) as f:
        for line in f:
            if (line.find("<main>:") != -1):
                main_address = line.split()[0]
                main_found = True

            if (main_found and (line.find("ret") != -1)):
                linesplit = (line.split())
                ret_address = line.split()[0][:-1]
                break

    return (main_address, ret_address)



def create_spike_cmd(addr_main, addr_ret):
    with open('spike-cmd.txt', 'w') as f:
        f.write("until pc 0 " + str(addr_main))
        f.write('\n')
        f.write("untiln pc 0 " + str(addr_ret))
        f.write('\n')
        f.write("q")
        f.write('\n')
    

def main(filename):
    addresses = extract_address(filename) 
    if (addresses[0] == "" or addresses[1] == ""):
        print("Warning: Invalid addresses. Check input file is correct!")
    else:
        create_spike_cmd(addresses[0], addresses[1])
        print("File: spike-cmd.txt created")

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
    #main()
