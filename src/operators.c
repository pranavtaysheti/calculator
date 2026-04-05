#include "operators.h"

#include "interpreter/interpreter.h"
#include "number.h"

Number add(Number n1, Number n2) {
    Number res;
    res.real = n1.real + n2.real;
    res.imag = n1.imag + n2.imag;

    return res;
}

Number substract(Number n1, Number n2) {
    Number res;
    res.real = n1.real - n2.real;
    res.imag = n1.imag - n2.imag;

    return res;
}
