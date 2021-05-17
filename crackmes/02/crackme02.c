#include <stdio.h>
#include <string.h>


int check_password(const char *secret_password, const char *user_password) {
    int i = 0;

    while(secret_password[i] != 0 && user_password[i] != 0) {
        if (secret_password[i] != user_password[i]) {
            printf("[%s] is not a valid password.\n", user_password);
            return 0;
        }
        i++;
    }

    return 1;
}

int main(int argc, char *argv[], char *envp[]) {
    int is_valid_password = 0;
    char *the_password = "verysecret";

    if (argc != 2) {
        printf("One argument that is the password to unlock the crackme.\n");
        return -1;
    }

    is_valid_password = check_password(the_password, argv[1]);
    if(is_valid_password != 0) {
    	printf("[%s] was the right password, you win! Perfect!\n", argv[1]);
	return 0;
    }

    return 1;

}
