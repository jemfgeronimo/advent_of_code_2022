#include <stdio.h>

int main() {
    int i;
    int num;
    FILE *fp = NULL;

    fp = fopen("input.txt", "r");

    for (i=0; i<10; i++){
        fscanf(fp, "%d", num);
        printf("num = ""%d""", num);
    }

    fclose(fp);

    return 0;
}