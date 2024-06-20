// get_string and printf with %s

#include "cs50.c"
#include <stdio.h>

int main(void)
{
    string answer = get_string("","What's your name? "); // add "", to get around too few argument bug
    printf("hello, %s\n", answer);
}
