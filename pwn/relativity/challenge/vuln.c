#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int vuln() {
  char *buf = malloc(0x100);

  setvbuf(stdout,NULL,2,0);
  setvbuf(stdin,NULL,2,0);

  puts("Would you like to say anything before I scream into the void? ");
  fgets(buf, 0x100, stdin);

  if (strchr(buf, 'n'))
    if (strchr(strchr(buf, 'n')+1, 'n'))
      if (strchr(strchr(strchr(buf, 'n')+1, 'n')+1, 'n'))
        _Exit(0);
  printf(buf);
  free(buf);
  __asm__("push %rax");
  _Exit(0);
}

int main() {
  vuln();
}
