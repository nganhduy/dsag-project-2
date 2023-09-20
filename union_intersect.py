class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, pylist = None):
        self.head = None
        if pylist is not None:
            for e in pylist:
                self.append(e)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        
        if len(out_string) == 0:
            return "<empty>"
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def get_middle(head):
    if head is None:
        return head
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def sorted_merge(left, right):
    if left is None:
        return right

    if right is None:
        return left

    node_left = left
    node_right = right

    new_head = None

    if node_left.value <= node_right.value:
        node = Node(node_left.value)
        new_head = node
        node_left = node_left.next
    else:
        node = Node(node_right.value)
        new_head = node
        node_right = node_right.next
    
    new_tail = new_head

    while node_left is not None and node_right is not None:
        if node_left.value <= node_right.value:
            node = Node(node_left.value)
            node_left = node_left.next
        else:
            node = Node(node_right.value)
            node_right = node_right.next
        
        new_tail.next = node
        new_tail = new_tail.next

    if node_left is None:
        new_tail.next = node_right
    else:
        new_tail.next = node_left
    
    return new_head

# modifies original list and return the new one
def mergeSort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    #split the list into two halves
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(next_to_middle)

    sorted_list_head = sorted_merge(left, right)

    return sorted_list_head


def copy_list(list):
    if list is None or list.head is None :
        return list

    node = list.head
    new_head = None
    new_tail = new_head
    while node is not None:
        new_node = Node(node.value)
        if node == list.head:
            new_head = new_node
            new_tail = new_head
        else:
            new_tail.next = new_node
            new_tail = new_tail.next
        node = node.next

    new_list = LinkedList()
    new_list.head = new_head
    return new_list


def union(llist_1, llist_2):

    if llist_1.head == None:
        return llist_2
    
    if llist_2.head == None:
        return llist_1

    sorted_list_1_head = mergeSort(copy_list(llist_1).head)
    sorted_list_2_head = mergeSort(copy_list(llist_2).head)
 
    
    # run through the list and remove duplicates
    node = sorted_merge(sorted_list_1_head, sorted_list_2_head)
    while node is not None and node.next is not None:
        if node.value == node.next.value:
            current_node = node
            while node.next is not None and node.value == node.next.value:
                node = node.next
            current_node.next = node.next
        node = node.next

    union_list = LinkedList()
    union_list.head = sorted_merge(sorted_list_1_head, sorted_list_2_head)
    return union_list


def intersection(llist_1, llist_2):
    if llist_1.head is None or llist_2.head is None:
        return LinkedList()

    copy_list_1 = copy_list(llist_1)
    copy_list_2 = copy_list(llist_2)

    list_1_node = mergeSort(copy_list_1.head)
    list_2_node = mergeSort(copy_list_2.head)

    new_head = None
    new_tail = None

    # run through the list and pick those which are the same
    # duplicates are allowed
    while list_1_node is not None and list_2_node is not None:
        if list_1_node.value < list_2_node.value:
            list_1_node = list_1_node.next
        elif list_1_node.value > list_2_node.value:
            list_2_node = list_2_node.next
        else:
            node = Node(list_1_node.value)
            if new_head is None:
                new_head = node
                new_tail = new_head
            else:
                new_tail.next = node
                new_tail = new_tail.next
            list_1_node = list_1_node.next
            list_2_node = list_2_node.next

    intersection_list = LinkedList()
    intersection_list.head = new_head
    return intersection_list


# Test case 0
print("Test case 0")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
print(union(linked_list_1,linked_list_2))          # expected empty
print(intersection(linked_list_1,linked_list_2))   # expected empty

# Test case 1
print("Test case 1")
linked_list_1 = LinkedList([])
linked_list_2 = LinkedList([])
print(union(linked_list_1,linked_list_2))          # expected empty
print(intersection(linked_list_1,linked_list_2))   # expected empty

# Test case 2
print("Test case 2")
linked_list_1 = LinkedList([1])
linked_list_2 = LinkedList([])
print(union(linked_list_1,linked_list_2))          # expected 1
print(intersection(linked_list_1,linked_list_2))   # expected empty

# Test case 3
print("Test case 3")
linked_list_1 = LinkedList([])
linked_list_2 = LinkedList([1])
print (union(linked_list_1,linked_list_2))          # expected 1
print (intersection(linked_list_1,linked_list_2))   # expected empty

# Test case 4
print("Test case 6")
linked_list_1 = LinkedList([1, 1])
linked_list_2 = LinkedList([1, 1, 2])
print (union(linked_list_1,linked_list_2))          # expected 1->2
print (intersection(linked_list_1,linked_list_2))   # expected 1->1

# Test case 5
print("Test case 4")
linked_list_1 = LinkedList([1])
linked_list_2 = LinkedList([1])
print (union(linked_list_1,linked_list_2))          # expected 1
print (intersection(linked_list_1,linked_list_2))   # expected 1

# Test case 6
print("Test case 8")
linked_list_3 = LinkedList([3,2,4,35,6,65,6,4,3,23])
linked_list_4 = LinkedList([1,7,8,9,11,21,1])
print (union(linked_list_3,linked_list_4))          # expected 1->2->3->4->6->7->8->9->11->21->23->35->65
print (intersection(linked_list_3,linked_list_4))   # expected empty