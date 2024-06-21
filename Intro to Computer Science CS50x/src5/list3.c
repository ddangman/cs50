// Prepends numbers to start of linked list, using while loop to print

#include "cs50.c"
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(int argc, char *argv[])
{
    // Memory for numbers
    node *list = NULL;

    // For each command-line argument
    for (int i = 1; i < argc; i++)
    {
        // Convert argument to int
        int number = atoi(argv[i]); // ASCII to Integer

        // Allocate node for number
        node *n = malloc(sizeof(node)); // n only exist in this scope. no need to free
        if (n == NULL) // check NULL pointer
        {
            // if memory is allocated, free it here
            return 1; // exit not successful
        }
        n->number = number;
        // not necessary since node.next will point to list, whose end is already NULL
        //n->next = NULL; 

        // Prepend node to list
        n->next = list;
        list = n;
    }

    // Print numbers
    node *ptr = list;
    while (ptr != NULL)
    {
        printf("%i\n", ptr->number);
        ptr = ptr->next;
    }

    // Free memory
    ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
}
// ./list3 1 2 3