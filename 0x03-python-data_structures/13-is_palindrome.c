#include "lists.h"

/**
 * check_pal - Recursively checks if linked list is a palindrome
 * @start: Pointer to head of the linked list
 * @end: Pointer to last node
 * Return: 0 if not, 1 if palindrome
 */
int check_pal(listint_t **front, listint_t *back)
{
	if (back == NULL)
		return (1);
	else if (check_pal(front, back->next) && ((*front)->n == back->n))
	{
		*front = (*front)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - Check if singly linked list is palindrome
 * @head: Pointer to head of singly linked list
 * Return: 1 if true, 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = *head;
	listint_t *back = *head;

	if (head == NULL)
		return (0);
	else if (*head == NULL)
		return (1);
	return (check_pal(&front, back));
}
