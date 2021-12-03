
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

static riscv_rfft_fast_instance_f32 S;
static float output[INPUT_LENGTH];

int main()
{
    riscv_rfft_fast_init_f32(&S, FFT_SIZE);
    riscv_rfft_fast_f32(&S, input_f32_fft_1024, output, ifftFlag);

    return 0;
}

