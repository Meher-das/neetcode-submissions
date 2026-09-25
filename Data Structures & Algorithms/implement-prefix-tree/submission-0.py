class Node:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        head = self.root
        for letter in word:
            i = ord(letter) - ord("a")
            if head.children[i] == None:
                head.children[i] = Node()
            head = head.children[i]
        head.end = True

    def search(self, word: str) -> bool:
        head = self.root
        for letter in word:
            i = ord(letter) - ord("a")
            if head.children[i] == None:
                return False
            head = head.children[i]
        
        return head.end

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for letter in prefix:
            i = ord(letter) - ord("a")
            if head.children[i] == None:
                return False
            head = head.children[i]
        return True
        
        