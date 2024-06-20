// Prints a string's address as well the addresses of its chars

#include "cs50.h"
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%p\n", s);     // show that string s is actually an address pointer to s[0]
    printf("%p\n", &s[0]); // show that string s is actually an address pointer to s[0]
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
}
