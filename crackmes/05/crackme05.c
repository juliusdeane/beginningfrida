#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 

int main()  {
    char *father_str = "[FATHER]";
    char *child_str = "[CHILD]";
    char *who_ptr = NULL;

    if( fork() == 0){
    	printf("I'm the child: younger and handsome...\n");
	who_ptr = child_str;
    }
    else {
    	printf("I'm the father: older and astonishing...\n");
	who_ptr = father_str;
    }
  
    printf("\t%s: Hello family!\n", who_ptr); 

    return 0; 
} 
