#include "list.h"
/**
*check_cycle - checks whether the linked list has a loop
*@list: the list to be checked
*Return: 0 if no loop is found , 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *CurHead, *NxtHead;
	CurHead = NxtHead = list;

	if (list == NULL)
		return (0);

	while (CurHead && NxtHead && NxtHead->next)
	{
		CurHead = CurHead->next;
		NxtHead = NxtHead->next;
		
		if (CurHead == NxtHead)
			return (1);

	}
	return (0);
}
