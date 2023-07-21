#include <stdio.h>

/**
 * https://courses.washington.edu/css342/zander/css332/passby.html
 *
 * One reason to use pointers is so that
 * a variable or an object can be modified in a called function.
 */
int main() {
    int number = 0;
    printf("Before: %d\n", number);
    increment_bad(number);
    printf("After increment_bad: %d\n", number);
    increment(&number);
    printf("After increment: %d\n", number);
    return 0;
}

/**
 * By definition, pass by value means you are
 * making a copy in memory of the actual parameter's value
 * that is passed in, a copy of the contents of the actual parameter.
 * Use pass by value when when you are only
 * "using" the parameter for some computation,
 * not changing it for the client program.
 */
void increment_bad(int number)
{
    // this only increments a copy of number,
    // not the one back in main
    number++;
}

/**
 * In pass by reference (also called pass by address),
 * a copy of the address of the actual parameter is stored.
 * Use pass by reference when you are changing the parameter
 * passed in by the client program.
 */
void increment(int *p_number)
{
    (*p_number)++;
}
