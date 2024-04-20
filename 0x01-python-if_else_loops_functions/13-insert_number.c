#include "lists.h"
/**
 * *insert_node - this function inserts a node
 * @head: is the head of the node.
 * @number: is the element of that node.
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next->n < number && current->next != NULL)
		{
			current = current->next;
		}
			new->next = current->next;
			current->next = new;
	}
	return (new);
}
