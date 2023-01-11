#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win(char a, char b, char c) {
    char fname[10] = {a, b, c, 'g', '.', 't', 'x', 't', 0};
    FILE *fd;
    if (!(fd = fopen(&fname[0], "r"))) {
        printf("Error opening flag file.\n");
        exit(1);
    }
    char buf[0x30] = {0};
    fgets(&buf[0], 0x20, fd);
    printf("%s\n", buf);
}

void getFeedback() {
    char buf[10] = {0};
    printf("Do you like ctf?\n");
    read(0, &buf, 30);
    printf("You said: %s\n", buf);
    if (buf[0] == 'y') {
        printf("That's great! ");
    } else {
        printf("Aww :( ");
    }
    printf("Can you provide some extra feedback?\n");
    read(0, &buf, 90);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    while (puts("Do you want to complete a survey?") && getchar() == 'y') {
        getchar(); // Clear the newline
        getFeedback();
    }
    return 0;
}