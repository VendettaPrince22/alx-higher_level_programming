#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: head node of list
 * 
 * Return: 0 if its not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
        listint_t *current;
        int count;
        int ptr[100];
        int ptr2[100];
        int new_count;
        int i;
        int x;
        int j;
        int data;
        int k;

        current = *head;
        count = 0;
        while (current != NULL)
        {
                current = current->next;
                count++;
        }

        new_count = count / 2;
        /***
        ptr = malloc(new_count * sizeof(ptr));
        ptr2 = malloc(new_count * sizeof(ptr2));
        */

        i = 0;
        while (i < new_count)
        {
                ptr[i] = current->n;
                current = current->next;
                i++;
        }

        i = 0;
        while (i < new_count)
        {
                x = 0;
                j = count;
                while(x < j)
                {
                        data = current->n;
                        current = current->next;
                        x++;
                }
                ptr2[i] = data;
                i++;
                j--;
        }

        /* Linearly compare if both arrays have same values */
        for (k = 0; k < new_count; k++)
        {
                if (ptr[k] != ptr2[k])
                {
                        return (0);
                }
                /**
                else
                {
                        return (1);
                }
                */
        }
        /**
        free(ptr);
        free(ptr2);
        */

        return (1);
}

/**
void free_ptrs()
{
        free(ptr);
        free(ptr2);
}
*/
