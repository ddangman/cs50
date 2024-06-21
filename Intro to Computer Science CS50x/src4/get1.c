// Incorrectly gets a string from user using scanf; compile with -Wno-uninitialized

#include <stdio.h>

int main(void)
{
    char *s; // address of 1st char in String. Uninitialized
    printf("s: ");
    scanf("%s", s); // char* is already an address reference
    printf("s: %s\n", s);
}
// Segmentation fault (core dumped)