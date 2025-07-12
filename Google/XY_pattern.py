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
    
    queue = deque([key for key in in_degree if in_degree[key] == 0])
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


from typing import Dict, List, Optional
from collections import deque

def resolve_string(input_string: str, mapping: Dict[str, str]) -> str:
    # Sort variables in topological order to resolve dependencies
    sorted_variables = topological_sort(mapping)
    if sorted_variables is None:
        return "-1"  # Cycle detected in variable dependencies
    
    # Resolve all variables in topological order
    resolved_values = {}
    for variable in sorted_variables:
        resolved_values[variable] = resolve_value(variable, mapping, resolved_values)
    
    # Replace all variables in the input string with their resolved values
    result = input_string
    for variable in find_variables(input_string):
        result = result.replace(variable, resolved_values[variable])
    
    return result

def find_variables(input_string: str) -> List[str]:
    variables = []
    index = 0
    
    # Scan through the string looking for pairs of '#' characters
    while (start := input_string.find("#", index)) != -1:
        end = input_string.find("#", start + 1)
        if end != -1:
            variables.append(input_string[start:end + 1])
            index = end + 1
        else:
            break
            
    return variables

def topological_sort(mapping: Dict[str, str]) -> Optional[List[str]]:
    # Initialize in-degree counter and adjacency graph
    in_degree = {key: 0 for key in mapping}
    graph = {key: [] for key in mapping}
    
    # Build dependency graph and calculate in-degrees
    for variable, value in mapping.items():
        for dependency in find_variables(value):
            if dependency in mapping:
                graph[dependency].append(variable)
                in_degree[variable] += 1
    
    # Queue for variables with no dependencies (in-degree = 0)
    queue = deque([variable for variable in in_degree if in_degree[variable] == 0])
    sorted_variables = []
    
    # Process nodes in topological order
    while queue:
        current = queue.popleft()
        sorted_variables.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we couldn't process all variables, there must be a cycle
    if len(sorted_variables) != len(mapping):
        return None  # Cycle detected
        
    return sorted_variables

def resolve_value(variable: str, mapping: Dict[str, str], resolved_values: Dict[str, str]) -> str:
    value = mapping.get(variable, "")
    
    for dependency in find_variables(value):
        if dependency in resolved_values:
            value = value.replace(dependency, resolved_values[dependency])
            
    return value

# Example usage
if __name__ == "__main__":
    mapping = {"#a#": "data#c#", "#b#": "#a#src", "#c#": "base"}
    input_string = "#b#"
    output = resolve_string(input_string, mapping)
    print(output)  # Expected: datasrcbase