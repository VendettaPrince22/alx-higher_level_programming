#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of the list
 * @number: number to insert into head list
 * 
 * Return: address of the new node; NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new;
        listint_t *current;
        listint_t *next_node;

        current = *head;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        
        new->n = number;
        new->next = NULL;

        next_node = current->next;
        while (next_node->n < number)
        {
                current = next_node->next;
                next_node = current->next;
        }
        new->next = current->next;
        current->next = new;

        return (new);
}
