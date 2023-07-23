# Compiling C

[CS50](https://cs50.harvard.edu/x/2023/notes/2/#compiling)

A `compiler` is a specialized computer program that converts source code into machine code that can be understood by a computer.

In CS50, we use a compiler called `clang` (which stands for *c language*) to compile our C code. Say we have a source code file called `hello.c`. Running `make hello` in CS50's Codespace dev environment executes `clang` to create an executable that we can run: `./hello`.

The process of going from source code files to an executable is called the `build` step:

1. `preprocessing` is where the header files (like `#include <cs50.h>`) are copied into the file.
2. `compiling` is where the program is converted into assembly code.
3. `assembling` involves the compiler converting the assembly code into machine code.
4. `linking` converts code from included libraries and then combines it with our code to make the executable file.
