#include <stdio.h>
 
int main () {
   FILE * fp;
   int i;

   fp = fopen ("example.txt","wt");
 
   /* fprintf: */
   /* write 10 "log" lines */
   for(i=0;i<10;i++){
       fprintf(fp, "event [%d]: very critical hash detected[4b1ecb9072dfaefc199690c66e88b9b9]\n",i);
   }
 
   fclose (fp);

   return 0;
}
