# Basically I needed to implement cli.


# I was given (as strings) as directories e.g.
# /a/b/x.txt
# /a/b/p.txt
# /a/c
# /a/d/y.txt
# /a/d/z.txt


# Also, I was given the selected directories e.g.
# /a/d/y.txt
# /a/d/z.txt
# /a/b/p.txt


# My output should be
# /a/d
# /a/b/p.txt


# /a/d
# is the answer because it has 2 txt files (y and z), and both are selected.
# /a/b/p.txt
# is the answer because another file in the directory i.e. /a/b/x.txt is not selected, if it was selected, answer would have been /a/b


# Basically, if all items are selected in a particular directory, we need to return the just prev directory.


# I tried solving it, assuming the directories to be a tree, and used dfs. I messed up really bad.
# How can we solve this problem? If possible, can someone code it up?
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.children_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words):
        ws = self.root
        for word in words:
            ws.children_count += 1
            if word not in ws.children:
                ws.children[word] = TrieNode()
            ws = ws.children[word]
        ws.is_file = True

    def decrement_children(self, words):
        ws = self.root
        for word in words:
            if word not in ws.children:
                return
            ws.children_count -= 1
            ws = ws.children[word]

    def search(self, words):
        ws = self.root
        for word in words:
            if word not in ws.children:
                return
            ws = ws.children[word]

    def get_path(self, words):
        ws = self.root
        path = []
        for word in words:
            ws = ws.children[word]
            if ws.children_count == 0 or ws.is_file:
                path.append(word)
                return "/".join(path)
            path.append(word)
        return ""

def compress_input(all_files, selected_files):
    trie = Trie()

    for file_path in all_files:
        words = file_path.split("/")
        trie.insert(words)

    for file_path in all_files:
        words = file_path.split("/")
        trie.search(words)

    for file_path in selected_files:
        words = file_path.split("/")
        trie.decrement_children(words)

    for file_path in selected_files:
        words = file_path.split("/")
        trie.search(words)

    result = []
    for file_path in selected_files:
        words = file_path.split("/")
        final_path = trie.get_path(words)
        if final_path and final_path not in result:
            result.append(final_path)

    return result

if __name__ == "__main__":
    all_files = ["a/b.txt", "b/c.txt", "b/d.txt", "c/e.txt", "c/f/a.txt", "c/f/b.txt", "c/g.txt", "d/a/b.txt"]
    selected_files = ["b/c.txt", "b/d.txt", "c/e.txt", "c/f/a.txt", "c/f/b.txt", "d/a/b.txt"]

    print(compress_input(all_files, selected_files))