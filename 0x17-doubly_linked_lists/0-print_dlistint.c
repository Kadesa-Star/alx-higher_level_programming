#include "lists.h"
/**
 * print_dlistint - prints all elements of a DLL
 * @h: pointer to the head of the list
 *
 * Return: the number of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	int nodes_number = 0;

	while (h == NULL)
		return (nodes_number);

	if (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		nodes_number++;
		h = h->next;
	}
	return (nodes_number);
}
