#include <unistd.h>
#include <stdlib.h>
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
int main(void)
{
	int count = 0, fork_call, zombie_pid;

	while (count < 5)
	{
		fork_call = fork();
		if (fork_call == -1)
			return (1);
		zombie_pid = getpid();
		printf("Zombie process created, PID: %d\n", zombie_pid);
		infinite_while();
		count++;
	}
}
