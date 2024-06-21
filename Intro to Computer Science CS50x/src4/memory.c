#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int *x = malloc(3 * sizeof(int)); // failed to free allocated memory
    x[1] = 72; // should start at 0
    x[2] = 73;
    x[3] = 33;

    return 0;
}
// valgrind not supported on Windows
// valgrind ./memory