#ifndef _INTERPRETER_H
#define _INTERPRETER_H

#include "interpreter_config.h"

#ifndef INTERPRETER_TYPE
#error "INTERPRETER_TYPE must be defined"
#endif

#define BASE_OPERATOR int precedence;

typedef struct UnaryOperator {
    BASE_OPERATOR
    INTERPRETER_TYPE (*operation)(INTERPRETER_TYPE n1)
} Operator1;

typedef struct BinaryOperator {
    BASE_OPERATOR
    INTERPRETER_TYPE (*operation)(INTERPRETER_TYPE n1, INTERPRETER_TYPE n2)
} BinaryOperator;

#define DEF_OPERATOR(c, fn, precedence)

#endif
