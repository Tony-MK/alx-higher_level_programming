#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a linked list
 * @head: double pointer to the head of the list
 * @number: value to be added to node
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *temp = *head, *new = NULL;

	if (!(*head))
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}

	new = malloc(sizeof(listint_t));
	if (!(new))
		return (NULL);
	else if (!(temp))
		return (NULL);
	else if (temp->n >= number)
	{
		new->n = number;
		new->next = temp;
		*head = new;
		return (new);
	}
	while (node->next)
	{
		node = node->next;
		if (node->n >= number)
		{
			new->n = number;
			new->next = node;
			temp->next = new;
			return (new);
		}
		else
			temp = temp->next;
	}
	return (add_nodeint_end(head, number));
}
