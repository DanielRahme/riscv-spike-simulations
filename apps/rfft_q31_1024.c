
#include <stdlib.h>
#include <math.h>
#include <riscv_dsp/riscv_math.h>
#include <riscv_dsp/riscv_const_structs.h>
#include <fft_input_array.h>

#define FFT_SIZE 1024
#define INPUT_LENGTH 2*FFT_SIZE

uint32_t fftSize = FFT_SIZE;
uint32_t ifftFlag = 0;
uint32_t doBitReverse = 0;

static riscv_rfft_instance_q31 S;
static q31_t output[INPUT_LENGTH];


int main()
{
    riscv_rfft_init_q31(&S, fftSize, ifftFlag, doBitReverse);
    riscv_rfft_q31(&S, input_q31_fft_1024, output);

    return 0;
}

