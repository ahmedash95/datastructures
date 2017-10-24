# Defining the node object
class Node:
    def __init__(self,label=None,data=None):
        self.label = label
        self.data = data
        self.children = dict()

    def add_child(self,key,data=None):
        # If the key not instance of node lets create a node object for it
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)

        # If not lets add it direct
        else:
            self.children[key.label] = key


    def __getitem__(self, key):
        return self.children[key]

class Trie:
    def __init__(self):
        self.head = Node()

    def add(self,word):
        current_node = self.head

        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                current_node.add_child(letter)
                current_node = current_node.children[letter]

        current_node.data = word

    def has_word(self,word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')

        # Starting from root
        current_node = self.head
        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
        # Validate if it's just a letter or a full word
        # If it's just a letter we will return false
        if exists:
            if current_node.data == None:
                exists = False

        return exists

    def start_with_prefix(self,word,node=None):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')

        if node != None:
            current_node = node
        else:
            # Starting from root
            current_node = self.head

        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False

        return exists


    def get_by_prefix(self,prefix):
        node = self.head
        matches = list()
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return list()

        if(self.has_word(prefix)):
            matches.append(prefix)
        for c,child in node.children.iteritems():
            if child.data != None:
                matches += self.get_by_prefix(child.data)
            else:
                matches += self.get_by_prefix(prefix + child.label)
        return matches