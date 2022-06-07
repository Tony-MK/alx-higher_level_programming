#include "lists.h"

int check_palindrome(listint_t *left, listint_t *right)
{
	if (!(right))
		return (1)
	else if (check_palindrome(left, right) && left-> n == right->n)
	{
		*left = (*left)->next;
		return (1);
	}
	return (0);

}

int is_palindrome(listint_t **head)
{
	listint_t *right;

	if (!(head))
		return (0);
	else if (*head && (*head)->next)
	{
		right = *head;
		return check_palindrome(*head, *right);
	}
	return (1);
}
