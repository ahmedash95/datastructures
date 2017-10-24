import Trie

t = Trie.Trie()
# Load Data
print "Loading Data ..."
f = open("names.txt")
for name in f:
    t.add(name.lower())

query = raw_input("Enter Name Prefix : ")

i = 0
for match in t.get_by_prefix(query):
    print "[{}] {}".format(i,match)
    i+=1