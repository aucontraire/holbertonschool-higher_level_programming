#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * list - linked list
 *
 * Return: 0 if cycle, 1 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	while (tortoise && hare)
	{
		if (hare->next == NULL)
			return (0);
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
