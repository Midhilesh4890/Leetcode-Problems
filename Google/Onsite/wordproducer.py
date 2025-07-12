from collections import Counter
from typing import Optional, Iterable

class MyWordProducer:
    def __init__(self, words: Iterable[str]):
        # Preserve insertion order for word priority
        self.words = list(words)
        # Buffer to store characters seen so far
        self.buffer = Counter()
        # Precompute the frequency count for each word
        self.word_freqs = {word: Counter(word) for word in self.words}
    
    def produce_word(self, c: str) -> Optional[str]:
        # Add the new character to our buffer
        self.buffer[c] += 1

        # Iterate over each word in the defined order
        for word in self.words:
            needed = self.word_freqs[word]
            # Check if the buffer has all required characters for the word
            if self._can_produce(needed):
                # Consume the letters of the word from the buffer
                for ch, count in needed.items():
                    self.buffer[ch] -= count
                    if self.buffer[ch] <= 0:
                        del self.buffer[ch]
                return word
        # Return None if no word can be produced
        return None

    def _can_produce(self, needed: Counter) -> bool:
        # Verify that every character required is in the buffer in the needed amount
        for ch, req_count in needed.items():
            if self.buffer.get(ch, 0) < req_count:
                return False
        return True

if __name__ == "__main__":
    # Create a MyWordProducer with the words: "foo", "bar", "fan"
    producer = MyWordProducer({"foo", "bar", "fan"})
    
    # Define the stream of characters
    stream = ['a', 'b', 'c', 'f', 'n', 'd', 'r', 'o', 'r', 'o', 'a','f', 'o']
    
    # Process each character in the stream and print the result of produce_word
    for char in stream:
        result = producer.produce_word(char)
        print(f"produce_word('{char}') -> {result}")

print('#################################################################')
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class MyWordProducerTrie:
    def __init__(self, words):
        # Build a trie for the reversed words
        self.root = TrieNode()
        self.buffer = []  # buffer for characters from the stream
        self.max_len = 0  # track the length of the longest word
        for word in words:
            self.max_len = max(self.max_len, len(word))
            self._insert(word)
    
    def _insert(self, word):
        # Insert the word in reverse order into the trie.
        node = self.root
        for c in reversed(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
    
    def produce_word(self, c):
        # Append the new character to the stream buffer.
        self.buffer.append(c)
        node = self.root
        # Only check the last `max_len` characters since no word is longer than that.
        # We iterate from the end of the buffer backwards.
        for i in range(len(self.buffer) - 1, max(-1, len(self.buffer) - self.max_len - 1), -1):
            char = self.buffer[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_word:
                # A match is found. Remove the matched characters from the buffer.
                matched_length = len(node.word)
                self.buffer = self.buffer[:-matched_length]
                return node.word
        return None

# Example usage:
if __name__ == "__main__":
    producer = MyWordProducerTrie({"foo", "bar", "fan"})
    stream = ['a', 'b', 'c', 'f', 'n', 'd', 'r', 'o', 'r', 'o', 'a']
    for char in stream:
        result = producer.produce_word(char)
        print(f"produce_word('{char}') -> {result}")
