
#include <stdlib.h>
#include <math.h>
#include <riscv_dsp/riscv_math.h>
#include <riscv_dsp/riscv_const_structs.h>
#include <fft_input_array.h>

#define FFT_SIZE 8192
#define INPUT_LENGTH 2*FFT_SIZE

uint32_t fftSize = FFT_SIZE;
uint32_t ifftFlag = 0;
uint32_t doBitReverse = 0;

static riscv_rfft_instance_q15 S;
static q15_t output[INPUT_LENGTH];


int main()
{
    riscv_rfft_init_q15(&S, fftSize, ifftFlag, doBitReverse);
    riscv_rfft_q15(&S, input_q15_fft_8192, output);

    return 0;
}

