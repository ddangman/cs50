// Division with longs, demonstrating double
// x=1, y=3 will be 0.33333333333333331483

#include "cs50.c"
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    long x = get_long("x: ");

    // Prompt user for y
    long y = get_long("y: ");

    // Divide x by y
    double z = (double) x / (double) y;
    printf("%.20f\n", z);
}
