#ifndef _NUMBER_H
#define _NUMBER_H

#include <math.h>

typedef struct Number {
    float real;
    float imag;
} Number;

bool isReal(Number n);
bool isWhole(Number n);

#endif