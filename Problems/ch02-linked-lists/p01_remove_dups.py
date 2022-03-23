from linked_list import LinkedList, Node

# algo expert has a sorted linkedList, this example is unsorted. solves in O(n) time
def remove_dups(linkedList):
  current = linkedList.head
  previous = None
  seen = set()

  while current:
    if current.value in seen:
      previous.next = current.next
    else:
      seen.add(current.value)
      previous = current
    current = current.next
  linkedList.tail = previous
  return linkedList
