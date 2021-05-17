#include <stdio.h>
#include <string.h>


int main(int argc, char *argv[], char *envp[]) {
    int do_wait = 1;
    int is_valid = 0;
    char longer_password[15];
    /* 0x7ffeb7f47399 */
    char variable_location[15];

    memset(longer_password, 0, 15);
    memset(variable_location, 0, 15);

    strcpy(longer_password, "veryverysecret");

    sprintf(variable_location, "%p", longer_password);
    printf("Variable location: [%s]\n", variable_location);

    if (argc != 2) {
        printf("One argument that is the address of the password to unlock the crackme.\n");
        return -1;
    }

    if( strcmp(variable_location, argv[1]) == 0) {
    	printf("[%s] was the right address, you win! Perfect!\n", argv[1]);
	return 0;
    }

    printf("[%s] was NOT the right address. You failed.\n", argv[1]);
    return 1;

}
