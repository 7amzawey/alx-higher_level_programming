#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: is the head of the list
 * Return: 0 if it's palindrome 1 if it's not.
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j;
	int *arr;
	listint_t *copy = *head;

	while (copy != NULL)
	{
		len++;
		copy = copy->next;
	}
	arr = malloc(len * sizeof(int));
	if (arr == NULL)
	{
		return (0);
	}
	copy = *head;

	while (copy != NULL)
	{
		arr[i] = copy->n;
		copy = copy->next;
		i++;
	}
	for (i = 0, j = len - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
