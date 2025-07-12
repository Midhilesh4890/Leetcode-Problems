from typing import List, Dict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False  # Marks the end of a valid word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True  # Mark the end of a word

    def search_prefix(self, prefix: str):
        """Returns the node if prefix exists, else None"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

def find_valid_sentences(s: str, dictionary: List[str]) -> List[str]:
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    results = []
    s = list(s)  # Convert string to list for mutability
    n = len(s)

    def dfs(index: int, current_sentence: List[str], word_so_far: str, node: TrieNode):
        if index == n:
            if node and node.is_word:  # Ensure last word is valid
                results.append(" ".join(current_sentence + [word_so_far]))
            return

        char = s[index]

        # Option 1: If it's a space (wildcard), we can replace it with any letter OR keep it
        if char == ' ':
            # Keep the space if the current word is valid
            if node and node.is_word:
                dfs(index + 1, current_sentence + [word_so_far], "", trie.root)

            # Replace space with a letter (Try 'a' to 'z')
            for ch in "abcdefghijklmnopqrstuvwxyz":
                next_node = node.children.get(ch) if node else None
                if next_node:
                    dfs(index + 1, current_sentence, word_so_far + ch, next_node)

        else:
            # If it's a letter, move forward only if it's in the Trie
            next_node = node.children.get(char) if node else None
            if next_node:
                dfs(index + 1, current_sentence, word_so_far + char, next_node)

    dfs(0, [], "", trie.root)
    return results

# Example usage:
dictionary = ["hello", "from", "the", "other", "side", "he"]
s = "h llo from he oth r sid "
print(find_valid_sentences(s, dictionary))
