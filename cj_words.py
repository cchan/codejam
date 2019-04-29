from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.endpoint = False
        self.children = defaultdict(TrieNode)
    def insert(self, s):
        if len(s):
            self.children[s[0]].insert(s[1:])
        else:
            self.endpoint=True
    def remove(self, s):
        if len(s):
            self.children[s[0]].remove(s[1:])
        else:
            self.endpoint=False
    def __len__(self):
        return int(self.endpoint) + sum(len(child) for child in self.children.values())
    def remove_pairs_at_depth(self, d):
        if d == 1:
            for char, child in self.children.items():
                l = len(child)
                if l >= 2:
                    child.children = defaultdict(TrieNode)
                    child.endpoint = l - 2
        else:
          for char, child in self.children.items():
              child.remove_pairs_at_depth(d-1)
    def __str__(self):
      s = "Node(\n"
      for char, child in self.children.items():
        s += char + ": " + str(child) + "\n"
      s += "\n"
      return s

T = int(input())

for testcase in range(T):
    N = int(input())
    trie = TrieNode()
    for i in range(N):
        trie.insert(input()[::-1])
    #print(str(trie))
    for d in range(50,0,-1):
        # print("Removing at depth " + str(d))
        trie.remove_pairs_at_depth(d)
    print("Case #{}: {}".format(testcase+1, N - len(trie)))
