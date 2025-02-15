def find_maximum_matching(questions, volunteers):
    # Step 1: Construct the bipartite graph
    # Each question maps to a list of volunteers who share at least one tag
    graph = {}

    for question in questions:
        question_id = question['id']
        question_tags = set(question['tags'])  # Convert tags to a set for quick lookup
        graph[question_id] = []  # Initialize adjacency list

        for volunteer in volunteers:
            volunteer_id = volunteer['id']
            volunteer_tags = set(volunteer['tags'])  # Convert volunteer tags to a set

            # If there is at least one common tag, create an edge
            if question_tags & volunteer_tags:
                graph[question_id].append(volunteer_id)

    # Step 2: Function to find an augmenting path using DFS
    def bpm(u, match_r, seen):
        for v in graph[u]:  # Iterate over volunteers who can take question 'u'
            if not seen[v]:  # Check if the volunteer is already considered
                seen[v] = True  # Mark volunteer as seen
                
                # If the volunteer is unassigned or can be reassigned to another question
                if v not in match_r or bpm(match_r[v], match_r, seen):
                    match_r[v] = u  # Assign question 'u' to volunteer 'v'
                    return True
        return False

    # Step 3: Perform matching using DFS
    match_r = {}  # Stores {volunteer_id: assigned_question_id}

    for question_id in graph:
        seen = {volunteer['id']: False for volunteer in volunteers}  # Track visited volunteers in each iteration
        bpm(question_id, match_r, seen)  # Try to assign this question

    # Step 4: Prepare the result mapping
    assigned_questions = {}
    
    for volunteer_id, question_id in match_r.items():
        volunteer_name = next(volunteer['name'] for volunteer in volunteers if volunteer['id'] == volunteer_id)
        assigned_questions[question_id] = volunteer_name

    return assigned_questions


# Example usage
questions = [
    {"id": 1, "tags": ["MAC", "VSCODE"]},
    {"id": 2, "tags": ["PY", "AI"]},
    {"id": 3, "tags": ["JAVA", "OS"]},
    {"id": 4, "tags": ["PY", "NW"]}
]

volunteers = [
    {"id": "1", "tags": ["PY", "NW"], "name": "A"},
    {"id": "2", "tags": ["AI"], "name": "B"},
    {"id": "3", "tags": ["JAVA", "NW"], "name": "C"},
    {"id": "4", "tags": ["JAVA", "NW"], "name": "D"}
]

assigned = find_maximum_matching(questions, volunteers)

for question_id, volunteer_name in assigned.items():
    print(f"Question {question_id} is assigned to volunteer {volunteer_name}")


from collections import defaultdict, deque

def find_maximum_matching_bfs(questions, volunteers):
    """
    Implements Maximum Bipartite Matching using BFS (Hopcroft-Karp Algorithm).
    Uses BFS to find shortest augmenting paths and DFS to augment matches.
    """

    # Step 1: Construct the bipartite graph (Adjacency List)
    graph = defaultdict(list)

    for question in questions:
        question_id = question['id']
        question_tags = set(question['tags'])

        for volunteer in volunteers:
            volunteer_id = volunteer['id']
            volunteer_tags = set(volunteer['tags'])

            if question_tags & volunteer_tags:  # If at least one tag matches
                graph[question_id].append(volunteer_id)

    # Step 2: BFS Function to build level graph
    def bfs(pair_u, pair_v, dist):
        """
        Breadth-First Search (BFS) to find shortest augmenting paths.
        Assigns distances and prepares for DFS augmentation.
        """
        queue = deque()
        for question_id in graph:
            if pair_u[question_id] == 0:  # If `question_id` is unassigned
                dist[question_id] = 0
                queue.append(question_id)
            else:
                dist[question_id] = float('inf')

        dist[0] = float('inf')

        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:  # If there's a possible match
                for v in graph[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])

        return dist[0] != float('inf')

    # Step 3: DFS Function to augment matches
    def dfs(u, pair_u, pair_v, dist):
        """
        Depth-First Search (DFS) to augment paths found by BFS.
        Assigns `u` to a volunteer and finds augmenting paths recursively.
        """
        if u != 0:
            for v in graph[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v], pair_u, pair_v, dist):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True

    # Step 4: Run Hopcroft-Karp Algorithm
    pair_u = {q["id"]: 0 for q in questions}  # Question -> Volunteer
    pair_v = {v["id"]: 0 for v in volunteers}  # Volunteer -> Question
    dist = {}

    matching = 0  # Count of matches

    while bfs(pair_u, pair_v, dist):  # BFS to find augmenting paths
        for u in graph:
            if pair_u[u] == 0 and dfs(u, pair_u, pair_v, dist):
                matching += 1  # Increase match count

    # Step 5: Prepare the result mapping
    assigned_questions = {
        q_id: next(v["name"] for v in volunteers if v["id"] == v_id)
        for v_id, q_id in pair_v.items() if v_id != 0
    }

    return assigned_questions


# Example usage
assigned_bfs = find_maximum_matching_bfs(questions, volunteers)

print("\nBFS-Based Hopcroft-Karp Maximum Matching Result:")
for question_id, volunteer_name in assigned_bfs.items():
    print(f"Question {question_id} is assigned to volunteer {volunteer_name}")

from collections import *

question = [
    {"id": 1, "tags": ["MAC", "VSCODE"]},
    {"id": 2, "tags": ["PY", "AI"]},
    {"id": 3, "tags": ["JAVA", "OS"]},
    {"id": 4, "tags": ["PY", "NW"]},
]

volunteers = [
    {"id": "1", "tags": ["PY", "NW"], "name": "A"},
    {"id": "2", "tags": ["AI"], "name": "B"},
    {"id": "3", "tags": ["JAVA", "NW"], "name": "C"},
    {"id": "4", "tags": ["JAVA", "NW"], "name": "D"},
]


def solve(question, volunteers):
    total_questions = len(question)
    total_volunteers = len(volunteers)

    grid = [[0 for i in range(total_questions)] for j in range(total_volunteers)]
    for i in range(total_volunteers):
        for j in range(total_questions):
            grid[i][j] = (
                1
                if len(set(volunteers[i]["tags"]).intersection(question[j]["tags"]))
                else 0
            )

    matches = defaultdict(str)

    def dfs(volunteer, visited):
        for question in range(total_questions):
            if grid[volunteer][question] and question not in visited:
                visited.add(question)
                if question not in matches or dfs(matches[question], visited):
                    matches[question] = volunteer
                    return True

        return None

    for volunteer in range(total_volunteers):
        dfs(volunteer, set())

    for question, volunteer in matches.items():
        print(f"{volunteers[volunteer]['name']} matched with {question}")


solve(question, volunteers)