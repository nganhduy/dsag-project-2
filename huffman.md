# Huffman coding implementation
There is a beautiful way to generate a list of tree nodes with symbols and their frequencies in one line on Python using list comprehension with itertoools' group by function.

To build a Huffman tree, I used heaps from collections. That is min heap. To use stacks with TreeNodes, I redefined compare methods in TreeNode class.

The time complexity of the Huffman function that builds the tree is O(nlogn):
* Sorting takes O(nlogn)
* Count frequencies O(n)
* Min heap takes O(logn), where n already several unique letters
* While loop itself takes Theta(n)

Space complexity is O(n), where n is the number of unique letters.

In the huffman_encoding function for encoding, I used recursion to traverse the tree. I used Hash Map to code all letters with one traversal of the tree. While traveling, I also remove unnecessary fields from the tree to reduce its size.

The time complexity of huffman_encoding is O(n) because there is one traversal of the entire tree.
Also, to convert Hash Map into a list of codes, a loop takes Theta(n) complexity.

Space complexity is O(n) for Hash Map.

Huffman decoding takes O(blog) where n is the length of the encoded message, and m is the number of unique letters since for each symbol in the encoded message, we should go down to the level of the tree.

For debugging purposes, there are print_tree functions.

If an empty string is passed for encoding, the blank encoded message is returned, and the root of the tree is None.
