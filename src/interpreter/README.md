# Interpreter

This module contains abstract interpreter that converts given string to Abstract 
Syntax Tree (AST).

## Working and Deisgn Goals

Interpreter should be initialized with symbol table, the symbol table should contain
enough data for interpreter to build AST. 

### Example of `struct Symbol`

```C
struct Symbol {
    
}
```
Once the AST is built. the process command goes through the tree from least significant
branch to most significant one.

- `TODO:` Explore possiblity of "processing" the tree concurrently.

Since the interpreter is abstract, it should not limit the type of result of an 
"Operation", but each "Operation" should take in either 1 or 2 operand of 
(lets say: type "N") and return the result in the same type "N".

### Example of `struct N`

```C
struct N {
    float real;
    float imag;
}
```

if the operator needs only one struct, the "Interpreter" should still add the garbage N 
into the tree, this may take slightly more memory, but will reduce the "if.. else" 
branching required when 

## Structure

- ### parse.c
    - responsible for taking in a string and converting to AST.
