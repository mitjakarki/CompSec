// filereader
/*
    The file contains two and only tokens that are separated with a space
    First token is an integer
    Second token is a string
    If the content of the text file is as specified above, return 1, otherwise 0
*/

/* Standard headers */
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

#define MAXCHAR 1000

int main(int argc, char *argv[]) {
    if( argc == 2 ) {
      printf("Checking file %s\n", argv[1]);
    }
    else if( argc > 2 ) {
      printf("Too many arguments supplied.\n");
      return 0;
    }
    else {
      printf("One argument expected.\n");
      return 0;
    }

    FILE *fp;
    char str[MAXCHAR];
    char* filename = argv[1];
 
    fp = fopen(filename, "r");
    if (fp == NULL){
        printf("Could not open file %s", filename);
        fclose(fp);
        return 0;
    }
    // read file contents to str
    while (fgets(str, MAXCHAR, fp) != NULL)
        printf("%s", str);
    fclose(fp);
    // check if there is a space and only one space
    char space = " ";
    char *str_ending;
    str_ending = strchr(str, space);
    if (str_ending == NULL) {
        printf("No spaces found")
        return 0;
    }
    else {

    }
    // NOTE: PROGRAM UNFINISHED

    return 1;
}
