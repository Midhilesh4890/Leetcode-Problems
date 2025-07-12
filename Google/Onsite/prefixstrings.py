class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Number of words passing through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increment count at each node
    
    def count_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0  # Prefix not found
            node = node.children[char]
        return node.count  # Return count at last character

# Example usage:
trie = Trie()
words = ["apple", "apply", "apricot", "banana", "blueberry"]
for word in words:
    trie.insert(word)

print(trie.count_prefix("ap"))  # Output: 3
print(trie.count_prefix("b"))   # Output: 2
print(trie.count_prefix("z"))   # Output: 0


class PrefixCounter:
    def __init__(self):
        self.words = []
        
    def insert(self, word):
        # Insert and keep the list sorted
        self.words.append(word)
        self.words.sort()
    
    def count_prefix(self, prefix):
        # Find the first word that has the prefix
        left = 0
        right = len(self.words) - 1
        first_occurrence = -1
        
        # Binary search to find the first occurrence
        while left <= right:
            mid = (left + right) // 2
            if self.words[mid].startswith(prefix):
                first_occurrence = mid
                right = mid - 1  # Look in the left half to find the first occurrence
            elif self.words[mid] < prefix:
                left = mid + 1
            else:
                right = mid - 1
        
        # If no match found, return 0
        if first_occurrence == -1:
            return 0
            
        # Find the last word that has the prefix
        left = 0
        right = len(self.words) - 1
        last_occurrence = -1
        
        # Binary search to find the last occurrence
        while left <= right:
            mid = (left + right) // 2
            if self.words[mid].startswith(prefix):
                last_occurrence = mid
                left = mid + 1  # Look in the right half to find the last occurrence
            elif self.words[mid] < prefix:
                left = mid + 1
            else:
                right = mid - 1
                
        # Return the count of words with the prefix
        return last_occurrence - first_occurrence + 1

# Example usage:
counter = PrefixCounter()
words = ["apple", "apply", "apricot", "banana", "blueberry"]
for word in words:
    counter.insert(word)
print(counter.count_prefix("ap"))  # Output: 3
print(counter.count_prefix("b"))   # Output: 2
print(counter.count_prefix("z"))   # Output: 0