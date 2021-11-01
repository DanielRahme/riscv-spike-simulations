

#include <riscv_dsp/riscv_math.h>
#include <riscv_dsp/riscv_const_structs.h>

int main()
{
    float32_t A_f32_4_4[16] =
    {
        1.0,     25.1,      4.0,     8.0, 
        3.0,     5.0,     7.0,    -3.0,
        134.0,     1.5,      128.0,      14.0,
        0.0,     -16.0,     128.0,    123.5,
    };
    /*   4*4   */
    float32_t B_f32_4_4[16] =
    {
        20,     19.1,      94.0,     -31.0,
        513.2,    11.0,     57.0,    5.0,
        1.0,     12.5,      8.0,      3.0,
        -22.0,     19.0,     2.0,    0.5,
    };

    float32_t Result_f32_4_4[16];

    riscv_matrix_instance_f32 MatA_f32_4_4;     
    riscv_matrix_instance_f32 MatB_f32_4_4;      
    riscv_matrix_instance_f32 MatResult_f32_4_4;

    riscv_mat_init_f32(&MatA_f32_4_4, 4, 4, (float32_t *)A_f32_4_4);
    riscv_mat_init_f32(&MatB_f32_4_4, 4, 4, (float32_t *)B_f32_4_4);
    riscv_mat_init_f32(&MatResult_f32_4_4, 4, 4,(float32_t *)Result_f32_4_4 );

    riscv_mat_mult_f32(&MatA_f32_4_4, &MatB_f32_4_4, &MatResult_f32_4_4);

    return 0;
}
