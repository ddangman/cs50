// Floating-point imprecision
// x=1, y=3 will be 0.33333334326744079590

#include "cs50.c"
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("x: ");

    // Prompt user for y
    int y = get_int("y: ");

    // Divide x by y
    float z = (float) x / (float) y;
    printf("%.20f\n", z);
}
