from collections import deque

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() == 0:
            return None
        
        return self.storage.popleft()

    def size(self):
        return len(self.storage)


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        return False

    q = Queue()
    q.enqueue(group)
    while q.size() > 0:
        group = q.dequeue()

        if user in group.get_users():
            return True
        
        for g in group.get_groups():
            q.enqueue(g)

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test 1
print(is_user_in_group("sub_child_user", parent))  #  True

# Test 2
print(is_user_in_group("sub_child", parent))       #  False

# Test 3
parent = Group("empty_parent")                    
print(is_user_in_group("sub_child_user", parent))  #  False

# Test 4
parent = None
print(is_user_in_group("sub_child_user", parent))  #  False