
import numpy as np
import random

### C float min: 1.175494351e-38
### C float max: 3.402823466e+38

# Constants
fmin = -1e+2
fmax = 1e+2


def generate_floats(fft_size):
    array_len = 2*fft_size
    # Arr_size is twice the size arr_size = (2*size)
    return np.random.uniform(low=fmin, high=fmax, size=array_len)

def generate_int16(fft_size):
    array_len = 2*fft_size
    # Arr_size is twice the size arr_size = (2*size)
    return random.sample(range(-32768, 32767), array_len)

def generate_int32(fft_size):
    array_len = 2*fft_size
    # Arr_size is twice the size arr_size = (2*size)
    return random.sample(range( -2147483648,2147483647), array_len)


def create_h_file(outfile_path):
    outfile = outfile_path + "fft_input_array.h"

    with open(outfile, 'w') as f:
        ## Headers and definition
        f.writelines("#ifndef FFT_INPUT_ARRAY_H") 
        f.write('\n')
        f.writelines("#define FFT_INPUT_ARRAY_H") 
        f.write('\n')
        f.writelines("#include <stdint.h>") 
        f.write('\n')

        fft_points = list(2**x for x in range(6, 14))

        for fp in fft_points:
            f.writelines("extern float input_f32_fft_" + str(fp) + "[" +
                    str(2 * fp) + "];")
            f.write('\n')
        f.write('\n')

        for fp in fft_points:
            f.writelines("extern int16_t input_q15_fft_" + str(fp) + "[" +
                    str(2 * fp) + "];")
            f.write('\n')
        f.write('\n')

        for fp in fft_points: # power of 2
            f.writelines("extern int32_t input_q31_fft_" + str(fp) + "[" +
                    str(2 * fp) + "];")
            f.write('\n')
        f.write('\n')

        f.write('\n')
        f.writelines("#endif")


def create_c_file(outfile_path):
    outfile = outfile_path + "fft_input_array.c"
    fft_points = list(2**x for x in range(6, 14))

    with open(outfile, 'w') as f:
        ## Headers and definition
        f.write('\n')
        f.writelines("#include <fft_input_array.h>") 
        f.write('\n')
        f.write('\n')
        f.write('\n')

        # Float32 generation
        for fft_size in fft_points:
            samples = generate_floats(fft_size)
            f.writelines("float input_f32_fft_" + str(fft_size) + "[" + str(2*fft_size) + "] = {")
            f.write('\n')

            for s in samples:
                f.writelines("    " + str(s) + "f,")
                f.write('\n')

            f.writelines("};")
            f.write('\n')
        f.write('\n')

        # int16 (q15) generation
        for fft_size in fft_points:
            samples = generate_int16(fft_size)
            f.writelines("int16_t input_q15_fft_" + str(fft_size) + "[" + str(2*fft_size) + "] = {")
            f.write('\n')

            for s in samples:
                f.writelines("    " + str(s) + ",")
                f.write('\n')

            f.writelines("};")
            f.write('\n')
        f.write('\n')

        # int32 (q31) generation
        for fft_size in fft_points:
            samples = generate_int32(fft_size)
            f.writelines("int32_t input_q31_fft_" + str(fft_size) + "[" + str(2*fft_size) + "] = {")
            f.write('\n')

            for s in samples:
                f.writelines("    " + str(s) + ",")
                f.write('\n')

            f.writelines("};")
            f.write('\n')
        f.write('\n')


def main(outfile_path):
    create_c_file(outfile_path)
    create_h_file(outfile_path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
