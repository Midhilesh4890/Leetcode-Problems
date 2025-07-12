from sortedcontainers import SortedList
from itertools import pairwise

def calculate_unique_masks(s):
    last_seen = {}  # Track the last position of each character
    sorted_chars = SortedList()  # Ordered list of characters based on last seen position
    result_masks = []

    for idx, char in enumerate(s):
        # Update the last seen position of the character
        if char in last_seen:
            sorted_chars.remove((-last_seen[char], char))
        last_seen[char] = idx
        sorted_chars.add((-idx, char))

        # Generate masks and counts for unique characters up to the current position
        masks_counts = []
        mask = 0  # Initialize mask as 0
        for (pos1, char1), (pos2, char2) in pairwise(sorted_chars):
            mask |= 1 << char1  # Corrected: Update mask using character index
            masks_counts.append((mask, pos2 - pos1))

        # Update mask for the last character in sorted_chars
        if sorted_chars:
            mask |= 1 << sorted_chars[-1][1]
            masks_counts.append((mask, 1 - sorted_chars[-1][0]))

        result_masks.append(masks_counts)

    return result_masks


def count_triplets_with_matching_masks(s):
    # Convert string to integer representation for bitmask manipulation
    char_indices = [ord(char) - ord("a") for char in s]

    # Calculate unique masks for substrings ending at each position and starting at each position
    left_masks = calculate_unique_masks(char_indices)
    right_masks = calculate_unique_masks(char_indices[::-1])[::-1]

    # Count matching triplets based on mask comparison
    triplet_count = 0
    for j in range(1, len(char_indices)):
        left_mask_counts = {}
        right_mask_counts = {}

        # Count frequency of each mask on the left side
        for mask, count in left_masks[j - 1]:
            if mask in left_mask_counts:
                left_mask_counts[mask] += count
            else:
                left_mask_counts[mask] = count

        # Count matching triplets using right side masks
        for mask, count in right_masks[j]:
            if mask in left_mask_counts:
                triplet_count += left_mask_counts[mask] * count

    return triplet_count


# Example usage
s1 = "ababab"
print(count_triplets_with_matching_masks(s1))  # Expected output: 4

s2 = "abccab"
print(count_triplets_with_matching_masks(s2))  # Expected output: 3
