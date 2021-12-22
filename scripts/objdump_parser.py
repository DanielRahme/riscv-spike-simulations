# Find start address of main
# and return address from main
import sys


def extract_address():
    main_found = False
    main_address = ""
    ret_address = ""

    for line in sys.stdin:
        if (line.find("<main>:") != -1):
            main_address = line.split()[0]
            main_found = True

        if (main_found and (line.find("ret") != -1)):
            linesplit = (line.split())
            ret_address = line.split()[0][:-1]
            break

    return (main_address, ret_address)


def print_spike_cmd(main_addr, ret_addr):
        print("until pc 0 " + str(main_addr))
        print("untiln pc 0 " + str(ret_addr))
        print("q")
    

def main():
    main_addr, ret_addr = extract_address() 
    if (main_addr == "" or ret_addr == ""):
        print("Warning: Invalid addresses. Check input file is correct!")
    else:
        print_spike_cmd(main_addr, ret_addr)

if __name__ == "__main__":
    import sys
    main()
