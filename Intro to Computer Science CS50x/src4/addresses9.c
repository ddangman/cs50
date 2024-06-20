// Prints a string's chars via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "HI!";

    printf("%c", s[0]);
    printf("%c", *(s + 1));
    printf("%c\n\n", *(s + 2));

    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
}
