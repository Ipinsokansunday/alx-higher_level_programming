#include "lists.h"

/**
 * reverse_listint - Reverses a linked list.
 * @head: Pointer to the first node in the list.
 *
 * Return: Pointer to the first node in the new list.
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Double pointer to the linked list.
 *
 * Return: 1 if it is, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *reversed = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	reverse_listint(&slow);
	reversed = slow;

	while (reversed && temp)
	{
		if (temp->n == reversed->n)
		{
			reversed = reversed->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	return (1);
}
