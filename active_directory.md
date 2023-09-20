# Active directory lookup implementation

The structure is a general tree structure.
I decided to use BFS traversing using Queue as a helper data structure.

The time complexity of the traversal is O(m*n), where m is the number of users and n is the number of groups.

Space complexity is O(n) where n is max(of groups on levels) since, on each level, we queue all groups of the next level.