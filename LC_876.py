def middle_linked_list (head):
	hare = tort = head  # Both hare and tort pointer start at the head

	while (hare!= None and hare.next!= None): #As long as hare and the next hare dont point at Null do:
		hare= hare.next.next # hare moves by skip 1
		tort = tort.next  # Tort moves by no skip

	return tort 