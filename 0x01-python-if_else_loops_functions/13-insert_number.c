#include "lists.h"

/**
 * insert_node - inserts a number into a singly list
 * @head: pointer to head
 * @number: number to insert
 * Return: pointer to new node or null incase of failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->m = number;

	if (node == NULL || node->m >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
