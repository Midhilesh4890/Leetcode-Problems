
# given a string s and a list of strings st.


# A string is special if its length >= 3 and it is a subsequence of the string s, and the string should be present in st.


# given a string s and st, return true if all the subsequences(length >= 3) are special words. else return false.

class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        # Create 26 buckets—one for each lowercase letter.
        buckets = [[] for _ in range(26)]
        
        # For each word in words, only consider it if its length is >= 3.
        # Instead of an iterator, we store a tuple (word, pointer) where
        # pointer is the index of the next character we need to match.
        for word in words:
            if len(word) >= 3:
                # Place the word into the bucket corresponding to its first character.
                buckets[ord(word[0]) - ord('a')].append((word, 0))
        
        # Process each character in S.
        for c in S:
            bucket_index = ord(c) - ord('a')
            current_bucket = buckets[bucket_index]
            # Clear the current bucket (we'll reassign its entries as needed).
            buckets[bucket_index] = []
            
            # Process each (word, pointer) pair waiting for the current character.
            while current_bucket:
                word, pointer = current_bucket.pop()
                pointer += 1  # Move to the next character in the word.
                
                if pointer == len(word):
                    # Finished matching the word.
                    ans += 1
                else:
                    # Put the word into the bucket for its next required character.
                    next_char = word[pointer]
                    buckets[ord(next_char) - ord('a')].append((word, pointer))
                    
        return ans
