#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer value stored in the node
 * @next: points to the next node in the list
 *
 * Description: Defines a singly linked list node structure
 *              for a Holberton project.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *insert_node(listint_t **head, int number);
listint_t *add_nodeint_end(listint_t **head, const int n);



#endif /* LISTS_H */
