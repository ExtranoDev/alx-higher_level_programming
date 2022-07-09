#include "lists.h"

/**
 * print_dlistint - prints elemets of a double linked list
 * @h - head of list
 *
 * Return: size of list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t i;
	const dlistint_t *hold = h;

	if (!h)
		return (0);
	for (i = 0; hold; i++)
	{
		printf("%d\n", hold->n);
		hold = hold->next;
	}
	return (i);
}
