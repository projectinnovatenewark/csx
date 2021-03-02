class Node:
  def __init__(self):
    self.child = {}
    self.end = False

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, listy):
    curr_node = self.root

    for word in listy:
        for char in word:
            if char not in curr_node.child:
                curr_node.child[char] = Node()
            curr_node = curr_node.child[char]
        curr_node.end = True

  def search(self, word):
    curr_node = self.root

    for char in word:
        if char not in curr_node.child:
            return False
        curr_node = curr_node.child[char]
    if (curr_node.end):
        return True
    else:
        return False

  def startsWith(self, prefix):
    curr_node = self.root

    for char in prefix:
        if char not in curr_node.child:
            return False
        curr_node = curr_node.child[char]
    return True

trie = Trie()
trie.insert(["kbd", "kbs", "lnop", "dumb"])
child1 = trie.printChild("lnop")
search1 = trie.search("kbd")
search2 = trie.search("lnop")
search3 = trie.search("smart")

prefix1 = trie.startsWith("du")
prefix2 = trie.startsWith("lm")

print(f"search1: {search1}\nsearch2: {search2}\nsearch3: {search3}")
print(f"prefix1: {prefix1}\nprefix2: {prefix2}")
print(trie.root)
