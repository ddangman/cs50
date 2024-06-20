// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n; // declare pointer to n
    printf("%p\n", p); // print pointer address to n
}
