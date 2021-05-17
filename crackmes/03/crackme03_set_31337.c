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
	if ((sem_item = sem_open (SEM_NAME, O_CREAT, 0660, 31337)) == SEM_FAILED) {
		printf("sem_open: error cannot open [%s]", SEM_NAME);
		exit (1);
	}

	int sem_value = 0;
	while(sem_value != 31337) {
		sem_post(sem_item);

		if (sem_getvalue (sem_item, &sem_value)== -1) {
                	printf("sem_getvalue: error cannot get value.");
                	exit(2);
        	}
	}
	return 0;
}
