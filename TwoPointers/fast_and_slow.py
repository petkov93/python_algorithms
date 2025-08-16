"""
Fast & Slow Pointers (Cycle Detection)
One pointer moves 1 step, the other moves 2 steps.
Used in linked list cycle detection, middle node.
Example: Detect cycle in linked list (Floyd’s Tortoise and Hare)"""

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

"""
✅ Used in: “Linked List Cycle”, “Find Middle of Linked List”.
"""
