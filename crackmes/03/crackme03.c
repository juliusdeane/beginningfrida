#include <sys/types.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <semaphore.h>
#include <unistd.h>
#include <fcntl.h>


#define SEM_NAME	"/fridasem"


int main (int argc, char *argv[], char *envp[]) {
	sem_t *sem_item;
	int sem_value = 0;

	if ((sem_item = sem_open (SEM_NAME, O_CREAT, 0660, 1)) == SEM_FAILED) {
		printf("sem_open: error cannot open [%s]", SEM_NAME);
		exit (1);
	}

	if (sem_getvalue (sem_item, &sem_value)== -1) {
		printf("sem_getvalue: error cannot get value.");
		exit(2);
	}
	else {
		printf("Sem value right now is = [%d]\n", sem_value);
	}

	if(sem_value == 31337) {
		printf("You reached victory and glory, you are da'Hacker!\n");
	}
	else {
		printf("Not achieved mere mortal...\n");
	}

	return 0;
}
