// Gets an int from user using scanf

#include <stdio.h>

int main(void)
{
    int n; // integer value
    printf("n: ");
    scanf("%i", &n); // pass by reference address
    printf("n: %i\n", n);
}
