## Request Routing in a Web Server with a Trie
This is a also trie problem. The difference between this one and problem 5 is that (1) the key of dictionary is not a charcter but a word; (2)no end_of_word boolean is needed. The path to word separation is realized by the split() function from python.  

Modular Complexity Analysis:  

RouteTrieNode constructor: (RouteTrieNode.__init__)
Time complexity: O(1).  
Space complexity: O(1), constant space required.

Add a single Node in the RouteTrie: (RouteTrieNode.insert)  
Time complexity: O(1).  
Space complexity: O(1).   

Insert a list of subdirectories in the RouteTrie: (RouteTrie. insert)   
Time complexity: O(N), where N is the depth of the subdirectories.    
Space complexity: O(N), where N is the depth of the subdirectories.   

RouteTrie constructor: (RouteTrie.__init__)
Create a new RouteTrieNode  
Time complexity: O(1).    
Space complexity: O(1), constant space required.  

Find a path in the RouteTrie: (RouteTrie.find)   
Time complexity: O(N), where N is the depth of the subdirectories as we traverse through the tree.   
Space complexity: O(1), no space required

Route constructor: (Route.__init__)
Create a new RouteTrie and set not_found:
Time complexity: O(1).    
Space complexity: O(1), constant space required.

Splitting the path: (Router.split_path)  
Time complexity: O(1)   
Space complexity: O(N),  where N is the height of subdirectories as we traverse through the tree.    

Add a handler for a path:  (Router.add_handler)   
This is (1) splitting the path into subdirectory string (2) insert the subdirectory list in the route trie.   
Time complexity: O(N), where N is the depth of the subdirectories as we traverse through the tree.  
Space complexity: O(N), where N is the depth of the subdirectories as we traverse through the tree.  

Look for a handler: (Router.lookup)   
Basically the same as find a path in the RouteTrie
Time complexity: O(N), where N is the height of subdirectories as we traverse through the tree.
Space complexity: O(1), no space required

