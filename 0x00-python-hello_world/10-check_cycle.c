#include "lists.h"

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
