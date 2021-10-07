#include <stdlib.h>
#include <math.h>
#include "distance.h"

int main()
{
    const float float_max = 2.0f;
    
    float a = ((float)rand()/(float)(RAND_MAX)) * float_max;
    float b = ((float)rand()/(float)(RAND_MAX)) * float_max;

    volatile const float res = distance(a, b);
    return 0;
}
