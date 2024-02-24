#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * infinite_while - infinite while loop
 * Return: always zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates zombies
 * Return: zero on success or 1 on failure
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void)
{
	pid_t pid;
	int status, count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid)
			printf("Zombie process created, PID: %u\n", pid);
		else
			exit(0);
		count++;
	}
	infinite_while();
	return (0);
}
