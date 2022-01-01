# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, route_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        for word in route_list:
            if word == '':
                continue
            if word in current.children:
                current = current.children[word]
            else:
                current.insert(word)
                current = current.children[word]
        current.handler = handler 


    def find(self, route_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for word in route_list:
            if word == '':
                continue
            if word in current.children:
                current = current.children[word]
            else:
                return None
        return current.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, word):
        # Insert the node as before
        self.children[word] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root=None, not_found=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(root)
        self.not_found = not_found

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route_list = self.split_path(path)
        self.trie.insert(route_list, handler) 
        

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        current = self.trie.root
        for word in self.split_path(path):
            if word == '':
                continue
            if word in current.children:
                current = current.children[word]
            else:
                return self.not_found
        if current.handler:
            return current.handler
        else:
            return self.not_found


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split("/")

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) 
#root handler

print(router.lookup("/home"))
#not found handler

print(router.lookup("/home/about")) 
#about handler

print(router.lookup("/home/about/")) 
#about handler

print(router.lookup("/home/about/me"))
#not found handler

print(router.lookup(" ")) #edge case
#not found handler\

print(router.lookup("")) #edge case
#root handler

emptyrouter = Router("root handler", "not found handler")
print(emptyrouter.lookup("/")) #edge case
#root handler


