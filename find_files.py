from collections import deque
import os

class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        
        return self.storage.popleft()

    def is_empty(self):
        return len(self.storage) == 0


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = []

    if path is None or len(path) == 0:
        return []

    if os.path.isfile(path):
        if path.endswith(suffix):
            output.append(path)
        return output

    q = Queue()
    q.enqueue(path)

    while not q.is_empty():
        p = q.dequeue()

        subdirs = os.listdir(p)
        for d in subdirs:
            d = os.path.join(p, d)
            if os.path.isdir(d):
                q.enqueue(d)
            else:
                if d.endswith(suffix):
                    output.append(d)

    return output


# Tests
print(find_files('.c', './testdir'))
# ['./testdir/t1.c', './testdir/subdir5/a.c',
# './testdir/subdir5/b.c', './testdir/subdir1/a.c',
# './testdir/subdir3/subsubdir1/b.c']
print(find_files('.c', './testdir/t1.c'))
# ['./testdir/t1.c']
print(find_files('.c', '.'))
# ['./testdir/t1.c', './testdir/subdir5/a.c',
# './testdir/subdir5/b.c', './testdir/subdir1/a.c',
# './testdir/subdir3/subsubdir1/b.c']
print(find_files('.c', ''))
# []
print(find_files('.c', None))
# []
print(find_files('.c', './testdir/subdir2'))
# []
print(find_files('.c', './testdir/subdir1/a.h'))
# []
print(find_files('.c', './testdir/subdir2/.gitkeep'))
# []