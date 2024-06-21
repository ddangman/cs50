// Dangerously gets a string from user using scanf with array

#include <stdio.h>

int main(void)
{
    // only enough memory allocated for "HI!"
    // at most 3 char and NUL can be inputted
    char s[4]; // address of 1st char in String
    printf("s: ");
    scanf("%s", s); // char* is already an address reference
    printf("s: %s\n", s);
}
// Segmentation fault (core dumped)