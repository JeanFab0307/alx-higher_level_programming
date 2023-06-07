#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the singly linked list
 *
 * Return: 0 if there is no cycle
 * Or 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list;
	while (list != NULL)
	{
		list = list->next;
		if (list == tmp)
		return (1);
	}
	return (0);
}
