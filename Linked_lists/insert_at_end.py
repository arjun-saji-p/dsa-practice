class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)

new_node = Node(30)

temp = head

while temp.next:
    temp = temp.next

temp.next = new_node

current = head

while current:
    print(current.data)
    current = current.next
