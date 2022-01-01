## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.end_of_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.insert(char)
                current = current.children[char]
        current.end_of_word = True
            
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return None
        return current


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.end_of_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes_list = []
        ## Return if there is no children
        if not bool(self.children):
            return [suffix]
        ## If it is a word, add a new element in the list
        if self.end_of_word:
            suffixes_list.append(suffix)
        # Recursion
        for char in self.children.keys():
            children_suffixes_list = self.children[char].suffixes(char)
            for child_suffix in children_suffixes_list:
                child_suffix = suffix + child_suffix
                suffixes_list.append(child_suffix)
        return suffixes_list



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)    

def find_prefix(trie, prefix):
    if prefix != '':
        prefixNode = trie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

EmptyTrie = Trie()

find_prefix(MyTrie,'f')
#un
#unction
#actory

find_prefix(MyTrie,'k')
#k not found

find_prefix(MyTrie,' ') #edge case
#  not found 

find_prefix(MyTrie,'') #edge case
#

find_prefix(EmptyTrie,' ') #edge case
#  not found 