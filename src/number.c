#include "number.h"

bool isReal(Number n) {
    return n.imag == 0;
}

bool isWhole(Number n) {
    if (!isReal(n)) {
        return false;
    }

    return floorf(n.real) == n.real;
}