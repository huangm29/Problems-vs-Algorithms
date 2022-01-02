##Request Routing in a Web Server with a Trie
This is a also trie problem. The difference between this one and problem 5 is that (1) the key of dictionary is not a charcter but a word; (2)no end_of_word boolean is needed. The path to word separation is realized by the split() function from python. 

Modular Complexity Analysis:

Add a handler for a path/ Insert a path in the Trie:

Time complexity: O(N), where N is the depth of the subdirectories as we traverse through the tree.
Space complexity: O(N), where N is the depth of the subdirectories as we traverse through the tree.

Finding a node/ Look up a path

Time complexity: O(N), where N is the height of subdirectories as we traverse through the tree.
Space complexity: O(1), no space required

Splitting the path:

Time complexity: O(1).
Space complexity: O(N),  where N is the height of subdirectories as we traverse through the tree.