
#include <stdlib.h>
#include <math.h>

float distance(const float x, const float y)
{
    return sqrtf(x*x + y*y);
}


int main()
{
    const float float_max = 2.0f;
    
    float a = ((float)rand()/(float)(RAND_MAX)) * float_max;
    float b = ((float)rand()/(float)(RAND_MAX)) * float_max;

    return distance(a, b);
}
