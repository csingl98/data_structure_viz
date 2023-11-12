class Node():
    def __init__(self, value):
        ALPHABET_SIZE = 26
        self.value = value
        #letter : Node(value=letter)
        self.children = {}
        self.isEndOfWord = False

    def toString(self):
        return "value: " + self.value

    def hasChild(self, letter):
        return self.children.get(letter) != None

    def addChild(self, letter):
        self.children[letter] = Node(letter)

    def getChild(self, letter):
        return self.children.get(letter)

    def removeChild(self, letter):
        self.children.pop(letter)

    def getChildren(self):
        return list(self.children.values())

    def hasChildren(self):
        return len(self.children) != 0

    # def isEndOfWord(self):
    #     return self.isEndOfWord


class Trie():

    def __init__(self) -> None:
        self.root = Node(None)

    def insert(self, word):

        current_node = self.root
        for letter in word:
            if  current_node.hasChild(letter) == False:
                current_node.addChild(letter)

            current_node = current_node.getChild(letter)

        current_node.isEndOfWord = True

    def contains(self, word):
        current_node = self.root

        if word == None:
            return False

        for letter in word:
            if current_node.hasChild(letter):
                current_node = current_node.getChild(letter)
            else:
                return False

        return current_node.isEndOfWord

    def traverse(self):
        self.traverse_nodes(self.root)

    def traverse_nodes(self, root):
        #Pre Order - Print value, then traverse
        #Post Order - Traverse, then print values
        print(root.value)

        for node in root.getChildren():
            self.traverse_nodes(node)

    def remove(self, word):
        if word == None:
            return
        #check first if tree contains word
        self.remove_letter(self.root, word, 0)


    def remove_letter(self, current_node, word, index):
        if index == len(word):
            current_node.isEndOfWord = False
            return

        letter = word[index]
        child = current_node.getChild(letter)

        if child == None:
            return 

        self.remove_letter(child, word, index + 1)

        if child.isEndOfWord == False and child.hasChildren == False:
            current_node.removeChild(letter)

    def findLastNodeOf(self, prefix):
        current_node = self.root
        for letter in prefix:
            if current_node == None:
                return

            current_node = current_node.getChild(letter)
        return current_node

    def findWords(self, prefix):
        if prefix == None:
            return
        
        last_node = self.findLastNodeOf(prefix)
        if last_node == None:
            return

        words = self.find_words(last_node, prefix, [])
        return words

    def find_words(self, root, word, words):
        if root.isEndOfWord:
            words.append(word)
 
        #loop through children
        for child in root.getChildren():
            words = self.find_words(child, word + child.value, words)
        
        return words







def main():
    trie = Trie()
    trie.insert('car')
    trie.insert('card')
    trie.insert('care')
    trie.insert('careful')
    trie.insert('egg')
    words = trie.findWords('cargo')
    print(words)
    print("Done!")
    

if __name__ == '__main__':
    main()