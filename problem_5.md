##Autocomplete with Tries

This is a Trie problem similar to the ones from the class. Each TrieNode contains two variables: one is a dictionary of which the key is the character saved and the value is another TrieNode, the other is a boolean which tells if whether the chain of characters from the rootnode to here refers to a word. Despite the normal insert function for the tree, the suffix function is realized by first finding the Trienode where the prefix refers to, and then recusively adding the character down through the tree. 

Time complexity:
O(N) for finding a node, where N is the length of the word as we traverse through the tree.
O(N) for inserting, where N is the length of the word as we traverse through the tree.
O(N) for suffix finding, where N is the length of all possible suffixes.

Space complexity:
O(1) for finding a node. No space required
O(N) for inserting, where N is the length of the word as we traverse through the tree.
O(N*M) for suffix finding in the worst case, where M is the number of suffixes, and N is the length of the suffixes. A list is created at each iteration step.