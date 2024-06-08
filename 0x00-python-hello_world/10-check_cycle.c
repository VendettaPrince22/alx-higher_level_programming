#include "lists.h"
#include <stdbool.h>

int distance(listint_t *first, listint_t *last);

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * 
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
        listint_t *first;
        listint_t *last;
        /*current_length stores no. of nodes between current position of first and last*/
        int current_length;
        /*prev_length stores no. of nodes between previous position of first and last*/
        int prev_length;

        /* first points to head, last pointer initially points to head */
        first = list;
        last = list;
        
        current_length = 0;
        prev_length = -1;

        while (current_length > prev_length && last != NULL)
        {
                /* set prev_length to current_length then update current_length */
                prev_length = current_length;
                current_length = distance(first, last);
                /* last node points the next node */
                last = last->next;
        }

        if (last == NULL)
        {
                return (0);
        }
        else
        {
                return (1);
        }
}

/**
 * distance - gets distance between first and last node every time last node moves forward
 * @first: first node in list
 * @last: last node in list
 * 
 * Return: distance
 */
int distance(listint_t *first, listint_t *last)
{
        int counter;
        listint_t *curr;

        counter = 0;
        curr = first;

        while (curr != last)
        {
                counter += 1;
                curr = curr->next;
        }
        return (counter + 1);
}
