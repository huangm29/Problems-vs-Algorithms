## Autocomplete with Tries

This is a Trie problem similar to the ones from the class. Each TrieNode contains two variables: one is a dictionary of which the key is the character saved and the value is another TrieNode, the other is a boolean which tells if whether the chain of characters from the rootnode to here refers to a word. Despite the normal insert function for the tree, the suffix function is realized by first finding the Trienode where the prefix refers to, and then recusively adding the character down through the tree.    

Modular Complexity Analysis:   

TrieNode constructor: (TrieNode.__init__):
Time Complexity: O(1)  
Space complexity: O(1), constant space required  

Trie constructor: (Trie.__init__):  
create a new TrieNode.   
Time Complexity: O(1)  
Space complexity: O(1), constant space required  

Insert a character in a trienode: (TrieNode.insert)  
Insert one element in the node of a tire.
Time Complexity: O(1)
Space complexity: O(1)

Insert a word in a trie: (Trie.insert)  
Time Complexity: O(N), where N is the length of the word as we traverse through the tree.
Space complexity: O(N) for inserting, where N is the length of the word as we traverse through the tree.

Find a word in a tire (Trie.find):
Time Complexity: O(N) for finding a node, where N is the length of the word to search for. 
Space complexity: O(1), no additional space required

Suffix collection (TrieNode.suffixes): 
This suffix collection iterate down through the entire trie after the current trienode. 
Time Complexity: O(N), where N is the length of the longest suffixes.   
Space complexity: O(N*M), where N is the length of the longest suffixes, and M is the number of suffixes.   
