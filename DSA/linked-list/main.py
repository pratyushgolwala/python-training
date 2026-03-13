from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None


def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def insert_in_between(node, data):
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
    return new_node

    

def insert_at_tail(head, data):
    new_node = Node(data)
    temp = head
    
    while temp.next:
        temp = temp.next
        
    temp.next = new_node
    new_node.next = None
    return head
    

def delete_from_head(head):
    if head is None:
        return None
    head = head.next
    return head

def delete_from_tail(head):
    if head is None:
        return None
    
    temp = head
    while temp.next.next:
        temp = temp.next
        
    temp.next = None
    
    return head

def delete_from_between(node):
    node.next = node.next.next


node1 = Node(10)
node2 = Node(20)

node1.next = node2

head = node1

head = insert_at_head(head, 5)
tail = insert_at_tail(head, 30)
anywhere = insert_in_between(node1,15)
# head = delete_from_head(head)
# delete_from_tail(head)
delete_from_between(node1)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")