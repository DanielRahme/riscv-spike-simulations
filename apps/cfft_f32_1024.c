
#include <stdlib.h>
#include <math.h>
#include <riscv_dsp/riscv_math.h>
#include <riscv_dsp/riscv_const_structs.h>
#include <fft_input_array.h>

uint32_t fftSize = 1024;
uint32_t ifftFlag = 0;
uint32_t doBitReverse = 0;

int main()
{
    riscv_cfft_f32(&riscv_cfft_sR_f32_len1024, input_f32_fft_1024, ifftFlag, doBitReverse);

    return 0;
}
