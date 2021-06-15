#include <stdlib.h>
#include<stdio.h>

char password[] = "verysecret";
int counter = 0;
const int max = 10;
int any_fail = 0;

int is_correct(const char c) {
	if(counter >= 10){
		return 0;
	}

	if(password[counter] == c) {
		counter++;
		return 1;
	}
	any_fail++;
	counter++;
	return 0;
}

int main() {
    char c;
    printf ("is_correct() at %p\n", is_correct);
    printf("Please, BE CAREFUL with ctrl-c as it will not return back your terminal (issue a stty cooked)\r\n");
    printf("Press keys to test the password: exit with Q.\r\n\r\n");
    /* Terminal to raw */
    system("stty raw");

    while(1) {
        c = getchar();
        if(c == 'Q') {
            printf("\r\n");
	    /* Terminal to cooked */
            system("stty cooked");
            return 0;
        }  
	printf("Key [%c] was pressed.\n\r", c);
	if(is_correct(c) == 1){
		printf("CORRECT!\r\n");
	}
	else{
		printf("WRONG!\r\n");
	}

	if(counter >= 10) {
		if(any_fail == 0) {
			printf("YOU WIN! PERFECT!\n\r\n\r");
			return 0;
		}
		printf("YOU FAIL! So sorry...\n\r\n\r");
            	system("stty cooked");
		return 1;
	}
    }

    system("stty cooked");
    return 0;
}
