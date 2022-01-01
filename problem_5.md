##Autocomplete with Tries

This is a Trie problem similar to the ones from the class. Each TrieNode contains two variables: one is a dictionary of which the key is the character saved and the value is another TrieNode, the other is a boolean which tells if whether the chain of characters from the rootnode to here refers to a word. Despite the normal insert function for the tree, the suffix function is realized by first finding the Trienode where the prefix refers to, and then recusively adding the character down through the tree. 
