def check_pattern(cards):
    if len(cards) != 3:
        return False
    
    # Extract colors and counts
    colors = [card[0] for card in cards]
    counts = [card[1] for card in cards]
    
    # Check if all cards have the same color
    if len(set(colors)) != 1:
        return False
    
    # If all cards have the same color, check counts
    count_set = set(counts)
    
    # Case 1: All counts are the same
    if len(count_set) == 1:
        return True
    
    # Case 2: Three different counts in consecutive order
    if len(count_set) == 3:
        sorted_counts = sorted(counts)
        if sorted_counts[1] - sorted_counts[0] == 1 and sorted_counts[2] - sorted_counts[1] == 1:
            return True
    
    return False

def can_divide_into_patterns_optimized(cards):
    if len(cards) != 12:
        return False
    
    # Count frequencies of each card
    from collections import Counter
    card_counter = Counter(cards)
    
    # First, try to form sets of identical cards (more efficient)
    # Create a copy of card_counter to keep track of remaining cards
    remaining_counter = card_counter.copy()
    patterns_found = 0
    
    # Look for sets of identical cards first (3 of the same card)
    for card, count in card_counter.items():
        if count >= 3:
            patterns_found += count // 3
            remaining_counter[card] -= (count // 3) * 3
    
    # If we've already found 4 patterns, return True
    if patterns_found >= 4:
        return True
    
    # Convert remaining counter back to a list of cards
    remaining_cards = []
    for card, count in remaining_counter.items():
        remaining_cards.extend([card] * count)
    
    # Group cards by color for easier sequential pattern matching
    cards_by_color = {}
    for card in remaining_cards:
        color, count = card
        if color not in cards_by_color:
            cards_by_color[color] = []
        cards_by_color[color].append(count)
    
    # For each color, try to form sequential patterns
    for color, counts in cards_by_color.items():
        # Sort counts for each color
        counts.sort()
        
        # Continue looking for patterns until we can't find any more
        i = 0
        while i <= len(counts) - 3:
            # Check if we have three consecutive numbers
            if counts[i+1] == counts[i] + 1 and counts[i+2] == counts[i] + 2:
                patterns_found += 1
                # Remove these counts
                counts.pop(i+2)
                counts.pop(i+1)
                counts.pop(i)
                # Reset i since we've modified the list
                i = 0
            else:
                i += 1
    
    # If we've found 4 patterns in total, return True
    return patterns_found >= 4

# Test cases
def test_optimized_solution():
    # Test patterns
    pattern1 = [("Black", 1), ("Black", 2), ("Black", 3)]  # Valid (same color, incremental)
    pattern2 = [("Red", 5), ("Red", 5), ("Red", 5)]  # Valid (all identical)
    pattern3 = [("Green", 1), ("Red", 2), ("Black", 3)]  # Invalid (different colors)
    
    print("Testing pattern checking:")
    print(f"Pattern 1: {check_pattern(pattern1)}")  # True
    print(f"Pattern 2: {check_pattern(pattern2)}")  # True
    print(f"Pattern 3: {check_pattern(pattern3)}")  # False
    
    # Test case where cards can be divided into 4 patterns
    cards1 = [
        ("Red", 1), ("Red", 2), ("Red", 3),
        ("Green", 5), ("Green", 5), ("Green", 5),
        ("Black", 1), ("Black", 2), ("Black", 3),
        ("Red", 7), ("Red", 8), ("Red", 9)
    ]
    
    # Test case where cards cannot be divided into 4 patterns
    cards2 = [
        ("Red", 1), ("Red", 2), ("Red", 4),  # Not a valid pattern
        ("Green", 5), ("Green", 5), ("Green", 5),
        ("Black", 1), ("Black", 2), ("Black", 3),
        ("Red", 7), ("Red", 8), ("Red", 9)
    ]
    
    print("\nTesting full solution:")
    print(f"Cards can be divided (should be True): {can_divide_into_patterns_optimized(cards1)}")
    print(f"Cards cannot be divided (should be False): {can_divide_into_patterns_optimized(cards2)}")

# Run tests
test_optimized_solution()