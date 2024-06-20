// Declares a string without CS50 Library

#include <stdio.h>

int main(void)
{
    char *s = "HI!"; // c compiler interprets "" instead of & for char* 
    printf("%s\n", s);
}
