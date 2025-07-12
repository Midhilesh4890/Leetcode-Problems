# You are given a address list like


# addressList=[(1,"A","AZ","AZZ"),(2,"B","AZ","ADD"),(1,"B","AZ","AZZ"),(1,"A","AZ","ADD"),(2,"B","AZ","QAA")]

# We have a query of form (1,"null","AZ","ADD") which can have null at any entry and 
# can have multiple nulls also, you need to give an algo that given true or false of 
# if this exists in addressList in O(1)


# i gave an hashamp and set approch to check this

class AddressChecker:
    def __init__(self, address_list):
        self.address_map = {}

        # Insert each address along with its wildcard variations
        for address in address_list:
            for wildcard_address in self.generate_wildcard_variations(address):
                self.address_map[wildcard_address] = True

    def generate_wildcard_variations(self, address):
        """Generate all possible wildcard variations using bitwise operations."""
        variations = set()
        n = len(address)

        # Iterate over all 2^n bit patterns
        for mask in range(1 << n):  # 2^n combinations
            temp = list(address)
            for i in range(n):
                if mask & (1 << i):  # If the i-th bit is set, replace with "null"
                    temp[i] = "null"
            variations.add(tuple(temp))

        return variations

    def query_exists(self, query):
        """Check if the query exists in O(1) time."""
        return tuple(query) in self.address_map


# Example Usage
address_list = [(1, "A", "AZ", "AZZ"), (2, "B", "AZ", "ADD"), (1, "B", "AZ", "AZZ"),
                (1, "A", "AZ", "ADD"), (2, "B", "AZ", "QAA")]

checker = AddressChecker(address_list)

queries = [
    (1, "null", "AZ", "ADD"),  # Should return True
    (2, "B", "AZ", "QAA"),     # Should return True
    (1, "C", "AZ", "ADD"),     # Should return False
    (1, 'A', 'null', "null")
]

for query in queries:
    print(f"Query {query} -> {checker.query_exists(query)}")

