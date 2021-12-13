
#include <stdlib.h>
#include <math.h>
#include <riscv_dsp/riscv_math.h>
#include <riscv_dsp/riscv_const_structs.h>
#include <fft_input_array.h>

uint32_t fftSize = 64;
uint32_t ifftFlag = 0;
uint32_t doBitReverse = 0;

int main()
{
    riscv_cfft_q31(&riscv_cfft_sR_q31_len64, input_q31_fft_64, ifftFlag, doBitReverse);

    return 0;
}

