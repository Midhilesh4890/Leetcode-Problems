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
