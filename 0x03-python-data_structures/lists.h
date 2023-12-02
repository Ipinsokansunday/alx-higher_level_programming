#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>

/**
 * struct listint_s - Defines a node in a singly linked list
 * @n: An integer value stored in the node
 * @next: Pointer to the next node in the list
 *
 * Description: Defines the structure of a singly linked
 * list node for the project.
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif /* LISTS_H */
