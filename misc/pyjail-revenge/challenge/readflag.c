#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  if(!argv[1]) {
    puts("Please provide the password");
    return 1;
  };
  if(strcmp(argv[1], "giveflag")) {
    puts("Incorrect password!");
    return 1;
  };
  char flag[256] = {0};
  FILE* fp = fopen("/flag", "r");
  if (!fp) {
    perror("fopen");
    return 1;
  }
  if (fread(flag, 1, 256, fp) < 0) {
    perror("fread");
    return 1;
  }
  puts(flag);
  fclose(fp);
  return 0;
}
