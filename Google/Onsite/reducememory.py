# You have a backend system that stores all versions of a JSON object. 
# You need to reduce the amount of data stored, how would you design the API.
# I assumed they wanted to write a function to do a JSON diff of current state vs 
# new state so we only store the diff. Had no feedback whatsoever from the interviewer 
# while working on it, so I have no idea what they expected.


# Ended up creating a function that returns a diff give two json objects 
# and that's all I managed to do with the time I had. 
# Still waiting to hear back if its a pass or not.

class TrieNode:
  def __init__(self):
    self.children = {}  # Dictionary to store child nodes (key: value)
    self.is_end_of_word = False  # Flag to indicate a complete JSON object
    self.value_versions = {}  # Dictionary of versions and their values

class JsonTrie:
  def __init__(self):
    self.root = TrieNode()

  def insert_json(self, node, data, version):
    """
    Inserts a JSON object starting from the specified Trie node for a specific version.
    """
    current = node
    for key, value in data.items():
      if key not in current.children:
        current.children[key] = TrieNode()
      current = current.children[key]
      if isinstance(value, dict):
        self.insert_json(current, value, version)  # Pass the current node for nested insertion
      else:
        current.is_end_of_word = True  # Mark leaf node for complete JSON object
        current.value_versions[version] = value

  def get_version(self, node, version):
    """
    Retrieves the complete JSON object for a specific version by traversing the Trie.
    """
    result = {}
    def traverse(current):
      if not current:
        return
      for key, child in current.children.items():
        if version in child.value_versions:  # Check if this version has a value
          result[key] = child.value_versions[version]
        traverse(child)
    traverse(node)
    return result

# Example usage
data_v1 = {"name": "Alice", "address": {"street": "123 Main St"}}
data_v2 = {"name": "Bob", "address": {"street": "123 Main St", "city": "New York"}}

json_trie = JsonTrie()
json_trie.insert_json(json_trie.root, data_v1, 1)
json_trie.insert_json(json_trie.root, data_v2, 2)

version_1_data = json_trie.get_version(json_trie.root, 1)
version_2_data = json_trie.get_version(json_trie.root, 2)

print("Version 1:", version_1_data)
print("Version 2:", version_2_data)