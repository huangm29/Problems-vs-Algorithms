##Request Routing in a Web Server with a Trie
This is a also trie problem. The difference between this one and problem 5 is that (1) the key of dictionary is not a charcter but a word; (2)no end_of_word boolean is needed. The path to word separation is realized by the split() function from python. 

Time complexity:
O(N) for finding a node, where N is the number of subdirectories as we traverse through the tree.
O(N) for inserting a path, where N is the number of subdirectories as we traverse through the tree.

Space complexity:
O(1) for finding a node. No space required
O(N) for inserting, where N is the number of subdirectories as we traverse through the tree.