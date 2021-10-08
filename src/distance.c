#include <math.h>

#include <distance/distance.h>

float distance(const float x, const float y)
{
    return sqrtf(x*x + y*y);
}
