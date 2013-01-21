#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	FILE* pFile;
	
	pFile = fopen("config","r");
	if(pFile == NULL)
	{
		fputs("File read error", stderr);
		exit(1);
	}
	else
	{
		char* in1 = (char* ) malloc((80*sizeof(char)) + 1);
		fgets(in1, 80, pFile);
		char* lqm = strstr(in1, "\"");
		printf("%s\n", in1);
		free(in1);
	}
	
		
	return 0;
}

