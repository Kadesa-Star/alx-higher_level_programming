#ifndef LISTS_H
#define LISTS_H

#include<stdlib.h>

/**
 * stuct listint - singly linked list
 * @data: the data in the list
 * @next: pointer to next node
 *
 * Description: this is the struct of a singly linked list
 */
typedef struct listint {
	int data;
	struct listint *next;
} listint_t

listint_t *insert_node(listint_t **head, const int m);
size_t print_list(listint_t, *head);
void free_list(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif
