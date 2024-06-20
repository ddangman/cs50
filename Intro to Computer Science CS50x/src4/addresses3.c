// Stores and prints an integer via its address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n; // declare pointer to n
    printf("%i\n", *p); // print n using its address pointer
}
