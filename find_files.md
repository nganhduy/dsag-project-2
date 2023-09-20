# File recursion implementation explanation

Since the file system is a tree, we can use a tree traversal algorithm for searching files that satisfy our input requirements (in this case, it matches with the suffix).

There was a requirement that there is no limit to the depth of the subdirectories. Unfortunately, this requirement means we can't use recursion to implement the traversal.

We still can use DFS with stack, but I selected BFS only because I get used to implementing DFS using recursion and BFS using the queue.

The algorithm's time complexity is O(n), where n is all directories and files because we need to traverse all these.

The space complexity is O(m), where m is the number of sibling directories or files within a level.