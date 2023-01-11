#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define n 10

int size[n];
char *note[n];

int menu(){
    puts("Your options are:");
    puts("1) create episode");
    puts("2) remove episode");
    puts("3) display episode");
    puts("4) resurrect series");
    puts("5) end series\n");
    
    puts("What would you like to do?");
}

void invalid(char *mes){
    printf("Invalid %s.\n", mes);
    _exit(1);
}

int inidx(){
    int idx;
    scanf("%d", &idx);
    getchar();
    puts("");

    if(idx < 0 || idx >= n) invalid("index, out of bounds");

    return idx;
}

void create_episode(){
    puts("You get to create a episode of minky momo.\n");

    puts("Which index would you like to store the episode at?");
    int idx = inidx();

    if(note[idx]) invalid("index, already exists");

    puts("What size would you like your episode to be?");
    
    scanf("%d", &size[idx]);
    getchar();
    puts("");

    if(size[idx] <= 0 || size[idx] > 0x47) invalid("size, out of bounds");

    note[idx] = malloc(size[idx] + 1);

    puts("What you want the episode to be about?");
    note[idx][read(0, note[idx], size[idx] + 1) - 1] = '\0';
    puts("");

    puts("Episode created.\n");
}


void remove_episode(){
    puts("You get to delete an episode.\n");

    puts("Which index would you like to delete an episode from?");
    int idx = inidx();

    if(!note[idx]) invalid("index, does not exist");

    free(note[idx]);

    puts("Episode removed.\n");
}
    
void display_episode(){
    puts("You get to display an episode.\n");

    puts("Which index would you like to display an episode from?");
    int idx = inidx();

    if(!note[idx]) invalid("index, does not exist");

    printf("Episode plot: %s\n\n", note[idx]);

    puts("Episode displayed.\n");
}

void resurrect_series(){
    puts("Using your minky stick, you ressurrected as the parent's real child now!.\n");
    execv("./minkymomo", 0);
    _exit(1);
}

void end_series(){
    puts("Yeet lost ur magic and got ran over by a bus.");
    _exit(0);
}

int main(){
    puts("Welcome to Minky Momo Episode Creator.\n");

    while(1){
        menu();
        
        char buf[0x10];
        gets(buf);
        puts("");

        int x = atoi(buf);

        switch(x){
            case 1:
                create_episode();
                break;
            case 2:
                remove_episode();
                break;
            case 3:
                display_episode();
                break;
            case 4:
                resurrect_series();
                break;
            case 5:
                end_series();
                break;
            default:
                invalid("option, does not exist");
                break;
        }
    }

    _exit(0);
    
    return 0;
}
