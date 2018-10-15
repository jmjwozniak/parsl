
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>

int
main(int argc, char* argv[])
{
  if (argc < 2)
  {
    printf("provide a child program!\n");
    return EXIT_FAILURE;
  }

  struct rlimit memory = { .rlim_cur=0 , .rlim_max=16*1000*1000 };
  setrlimit(RLIMIT_DATA, &memory);
  
  printf("running: %s\n", argv[1]);
  execvp(argv[1], &argv[1]);
  printf("FAILED!\n");
  return EXIT_FAILURE;
}
