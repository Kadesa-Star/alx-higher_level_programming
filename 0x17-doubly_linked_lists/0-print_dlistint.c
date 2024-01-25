#include "lists.h"
/**
 * print_dlistint - prints all elements of a DLL
 * @h: pointer to the head of the list
 *
 * Return: the number of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *current = h;
	size_t nodes_number = 0;

	while (current != NULL)
	{
		printf("%d\n", current->n);
		current = current->next;
		nodes_number++;
	}
	printf("\n");
	return (nodes_number);
}
