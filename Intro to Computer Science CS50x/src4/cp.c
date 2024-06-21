// Copies a file

#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    FILE *src = fopen(argv[1], "rb"); // read binary
    FILE *dst = fopen(argv[2], "wb"); // write binary

    BYTE b;

    // read and write 1 BYTE at a time
    // fread(BYTE) returns number of BYTE read
    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }

    fclose(dst);
    fclose(src);
}

// ./cp cat.jpg copy_cat.jpg
