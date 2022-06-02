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
	listint_t *temp = *head, *new = NULL;
	
	new = malloc(sizeof(listint_t));
	if (!(new))
		return (new);
	new->n = number;
	if (!(*head))
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	else if (!(temp))
		return (NULL);
	else if (temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next)
	{
		temp = temp->next;
		if (temp->n >= number)
		{
			new->next = temp;
			temp->next = new;
			return (new);
		}
	}
	free(new);
	return (add_nodeint_end(head, number));
}
