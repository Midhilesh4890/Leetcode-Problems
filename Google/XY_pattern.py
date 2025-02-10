from typing import Dict, List, Deque
from collections import deque

def find_value(input_string: str, mapping: Dict[str, str]) -> str:
    values_to_find = find_values(input_string)
    
    # Check if all values exist in the map; if not, return "-1"
    for key in values_to_find:
        if key not in mapping:
            return "-1"
    
    sorted_keys = topological_sort(mapping)
    if sorted_keys is None:
        return "-1"  # Cycle detected
    
    resolved_values = {}
    for key in sorted_keys:
        resolved_values[key] = resolve_value(key, mapping, resolved_values)
    
    for key in values_to_find:
        input_string = input_string.replace(key, resolved_values[key])
    
    return input_string

def topological_sort(mapping: Dict[str, str]) -> List[str]:
    in_degree = {key: 0 for key in mapping}
    graph = {key: [] for key in mapping}
    
    for key, value in mapping.items():
        for dep in find_values(value):
            if dep in mapping:
                graph[dep].append(key)
                in_degree[key] += 1
    
    queue: Deque[str] = deque([key for key in in_degree if in_degree[key] == 0])
    sorted_keys = []
    
    while queue:
        node = queue.popleft()
        sorted_keys.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(sorted_keys) != len(mapping):
        return None  # Cycle detected
    return sorted_keys

def resolve_value(key: str, mapping: Dict[str, str], resolved_values: Dict[str, str]) -> str:
    value = mapping.get(key, "")
    for dep in find_values(value):
        value = value.replace(dep, resolved_values.get(dep, ""))
    return value

def find_values(input_string: str) -> List[str]:
    values = []
    index = 0
    while (start := input_string.find("%", index)) != -1:
        end = input_string.find("%", start + 1)
        if end != -1:
            values.append(input_string[start:end + 1])
            index = end + 1
        else:
            break
    return values

# Example usage:
mapping = {"%X%": "123", "%Y%": "456_%X%"}
input_string = "%X%_%Y%"
output = find_value(input_string, mapping)
print(output)  # Expected output: "123_456_123"
