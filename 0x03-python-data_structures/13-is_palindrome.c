#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to pointer to the head of the linked list
* Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast)
		slow = slow->next;

	while (prev)
	{
		if (prev->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}

	return (is_palindrome);
}
