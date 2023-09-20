# Union and intersection implementation
I used merge sorting to sort a linked list. After that, it is relatively easy to process union and intersection operations with one pass.
I used merge sort because it is suitable for linked lists and takes O(nlogn), where n is several elements in the list.

I also need to write a list copy function to prevent mutation of original lists during merge sort. Its complexity is O(n)

I made the following assumptions about how to treat two different nodes with the same values for the operations:

For union operation:
    If there are two nodes with the same value, there will be only one value in the union. For example, list1 = [1, 1], list2= [1, 2]. The partnership will be [1, 2] <== That is how it was implemented.
    Another way of treating it is that these two 1s are different. In this case, the results will be [1, 1, 2]

For intersection:
    list1 = [1, 1, 5], list2 = [1, 1, 6].
    Implementation will produce [1, 1]

Time complexity:

    Union: O(nlogn)
        copying of the lists: O(n)
        sorting: O(nlogn)
        building union: O(n)

    Intersection: O(nlogn)
        copying of the lists: O(n)
        sorting: O(nlogn)
        building union: O(n)