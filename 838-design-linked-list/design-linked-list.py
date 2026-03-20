class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)  # dummy-голова
        self.size = 0

    def get(self, index: int) -> int:
        # если индекс некорректный
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index < 0:
            index = 0
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        node = ListNode(val)
        node.next = prev.next
        prev.next = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        prev.next = prev.next.next
        self.size -= 1