# Blockchain implementation
Since the requirements are very vague, there were many assumptions.

Also, nonce (proof) and the mining algorithm weren't implemented. It isn't required.

The linked list was implemented to chain Blocks.

A new block is added to the head.

During add, a new block validates the previous hash, and the league is not counted in case of a mismatch.

There is also a tail pointer in case we need access to Genesis.

Adding block time complexity is O(1)
Getting a block by index takes O(n)

Genesis block is created during Blockchain initialization.