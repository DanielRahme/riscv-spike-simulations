
import numpy as np

### C float min: 1.175494351e-38
### C float max: 3.402823466e+38

# Constants
fmin = -1e+2
fmax = 1e+2

def generate_floats(fft_size):
    array_len = 2*fft_size
    # Arr_size is twice the size arr_size = (2*size)
    return np.random.uniform(low=fmin, high=fmax, size=array_len)

def create_h_file(outfile_path):
    outfile = outfile_path + "fft_input_array.h"

    with open(outfile, 'w') as f:
        ## Headers and definition
        f.writelines("#ifndef FFT_INPUT_ARRAY_H") 
        f.write('\n')
        f.writelines("#define FFT_INPUT_ARRAY_H") 
        f.write('\n')
        f.write('\n')
        f.write('\n')

        fft_points = list(2**x for x in range(6, 14))

        for fp in fft_points: # power of 2
            f.writelines("extern float input_f32_fft_" + str(fp) + "[" +
                    str(2 * fp) + "];")
            f.write('\n')

        f.write('\n')
        f.writelines("#endif")


def create_c_file(fft_size, outfile_path, samples):
    outfile = outfile_path + "fft_input_array.c"
    fft_points = list(2**x for x in range(6, 14))

    with open(outfile, 'w') as f:
        ## Headers and definition
        f.write('\n')
        f.writelines("#include <fft_input_array.h>") 
        f.write('\n')
        f.write('\n')
        f.write('\n')

        for fft_size in fft_points:
            f.writelines("float input_f32_fft_" + str(fft_size) + "[" + str(2*fft_size) + "] = {")
            f.write('\n')

            for s in samples:
                f.writelines("    " + str(s) + "f,")
                f.write('\n')

            f.writelines("};")
            f.write('\n')
            f.write('\n')


def main(outfile_path):
    fft_size = 64
    samples = generate_floats(fft_size)
    create_c_file(fft_size, outfile_path, samples)
    create_h_file(outfile_path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
