#include "distance.h"
#include <math.h>

float distance(const float x, const float y)
{
    return sqrtf(x*x + y*y);
}
