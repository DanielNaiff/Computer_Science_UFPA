#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
  int numeroProcessos;

  printf("Quanto processos voce quer criar? ");
  scanf("%d", &numeroProcessos);

  for (int i = 0; i < numeroProcessos - 1; i++) {
    pid_t pid;
    pid = fork();

    if (pid < 0) {
      printf("Fork falhou.\n");
      return 1;
    } else if (pid == 0) {    
      execl("./helloWorld", "./helloWorld", NULL); 
      printf("failed.\n");
      return 0;
    }
  }
  
  for (int i = 0; i < numeroProcessos; i++) {
    wait(NULL);
  }
  execl("./helloWorld", "./helloWorld", NULL);
  printf("Os processos terminaram.\n");

  return 0;
}
