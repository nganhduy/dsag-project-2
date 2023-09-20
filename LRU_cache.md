# LRU_cache implementation explanation

The requirements:
* get operation of time O(1)
* set operation of time O(1)
* cache has a fixed size of 5
* if the cache is full, the least recent value is removed.
* Since set time complexity should be O(1), remove also should be O(1)

The following data structures were used:
* Double-linked list
*  Dictionary (Hash Map)

The double-linked list gives us O(1) insertion to the head or tail. In my code, I selected to insert to the head (prepend) = most recent element.

The double-linked list also gives us O(1) removal
in case we already point to the node in question.

A hash map is used to provide access to O(1)

Dictionary keys are mapped to the nodes of a double-linked list.

I store keys with values in the nodes as well because while removing an element from the tail of the list, I also need to remove the key from the Hash map and know the component's legend.

For debugging purposes, I redefined __repr__ functions.

Summary of complexities:
get operation O(1)
set operation O(1)

Space complexity is O(n), but if to look into details, we need to store 2n keys + n values, so roughly, we get O(3n)


