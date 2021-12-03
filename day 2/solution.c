#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct policy {
    int min;
    int max;
    char * letter;
};

typedef struct policy policy;

struct password {
    policy * policy;
    char * password;
};

typedef struct password password;

int main(void) {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    int i = 0;

    fp = fopen("input.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    password passwords[1000];

    while ((read = getline(&line, &len, fp)) != -1) {
        passwords[i] = malloc(sizeof(password));
        
        char delim[] = ":";
        char *ls = strtok(line, delim);
        char *p = strtok(NULL, delim);
        if (p[0] == ' ') p++;
        char dash[] = "-";
        char *min = strtok(ls, dash);
        policy pol;
        pol.min = atoi(min);
        char *uhh = strtok(NULL, dash);
        char space[] = " ";
        char *max = strtok(uhh, space);
        char *letter = strtok(NULL, space);
        pol->letter = letter;
        pol->max = atoi(max);
        pw->policy = &pol;
        passwords[i] = pw;
        i++;
    }

    for(i = 0; i < sizeof(passwords) / sizeof(password); i++)
    {
        password * pw = passwords[i];
        int j, count;
        // for (j=0, count=0; pw->password[j]; j++)
        //     count += (pw->password[j] == *pw->policy->letter);
        // printf("%i", count);
    }
    

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
};