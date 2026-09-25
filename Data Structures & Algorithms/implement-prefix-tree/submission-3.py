class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()      

    def insert(self, word: str) -> None:
        head = self.root
        for c in word:
            if not c in head.children:
                head.children[c] = Node()
            head = head.children[c]
        head.end = True

    def search(self, word: str) -> bool:
        head = self.root
        for c in word:
            if not c in head.children:
                return False
            head = head.children[c]
        return head.end

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for c in prefix:
            if not c in head.children:
                return False
            head = head.children[c]
        return True
        
        