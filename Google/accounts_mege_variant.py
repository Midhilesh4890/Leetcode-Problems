from collections import defaultdict

def find_similar_videos(videos, query_index):
    tag_to_videos = defaultdict(list)
    
    # Process all videos that come before the query video.
    # We only care about these because the problem states that we only compare with previous videos.
    for i in range(query_index):
        for tag in videos[i]:
            # Append the current video's index to the list for this tag.
            tag_to_videos[tag].append(i)
    
    # Initialize a set to store indices of videos that share at least one tag with the query video.
    # A set is used to avoid duplicate indices in case multiple tags match.
    similar_videos = set()
    
    # Look at each tag in the query video's tag list.
    for tag in videos[query_index]:
        # For the current tag, retrieve all videos (from the mapping) that have this tag.
        for vid in tag_to_videos[tag]:
            similar_videos.add(vid)
    
    # Return a sorted list of similar video indices for consistency in ordering.
    return sorted(similar_videos)

def main():
    # ---------------------------------------------------------
    # Example Test Case 1:
    # ---------------------------------------------------------
    # Videos with tags:
    # video1 -> ["tag1", "tag2"]
    # video2 -> ["tag2", "tag3"]
    # video3 -> ["tag3", "tag4"]
    #
    # Query: video3 (index 2)
    # Explanation:
    # - Compare video1 (["tag1", "tag2"]) and video2 (["tag2", "tag3"]) with video3 (["tag3", "tag4"]).
    # - video1 shares no common tag with video3.
    # - video2 shares "tag3" with video3, so video2 is considered similar.
    videos1 = [
        ["tag1", "tag2"],  # video1 (index 0)
        ["tag2", "tag3"],  # video2 (index 1)
        ["tag3", "tag4"]   # video3 (index 2)
    ]
    query_index1 = 2  # Choosing video3 as the query video.
    result1 = find_similar_videos(videos1, query_index1)
    
    print("Test Case 1:")
    print("Videos:")
    for idx, tags in enumerate(videos1):
        print(f"  video{idx+1}: {tags}")
    print(f"Query video: video{query_index1+1} with tags {videos1[query_index1]}")
    print("Similar videos (indices):", result1)
    print("Similar videos (names):", [f"video{i+1}" for i in result1])
    print("-" * 50)
    
    # ---------------------------------------------------------
    # Example Test Case 2:
    # ---------------------------------------------------------
    # Videos with tags:
    # video1 -> ["news", "politics"]
    # video2 -> ["sports", "health"]
    # video3 -> ["entertainment", "music"]
    # video4 -> ["politics", "economy"]
    #
    # Query: video4 (index 3)
    # Explanation:
    # - video1 shares "politics" with video4.
    # - video2 and video3 do not share any tags with video4.
    videos2 = [
        ["news", "politics"],      # video1 (index 0)
        ["sports", "health"],      # video2 (index 1)
        ["entertainment", "music"],# video3 (index 2)
        ["politics", "economy"]    # video4 (index 3)
    ]
    query_index2 = 3  # Choosing video4 as the query video.
    result2 = find_similar_videos(videos2, query_index2)
    
    print("Test Case 2:")
    print("Videos:")
    for idx, tags in enumerate(videos2):
        print(f"  video{idx+1}: {tags}")
    print(f"Query video: video{query_index2+1} with tags {videos2[query_index2]}")
    print("Similar videos (indices):", result2)
    print("Similar videos (names):", [f"video{i+1}" for i in result2])
    print("-" * 50)
    
    # ---------------------------------------------------------
    # Example Test Case 3:
    # ---------------------------------------------------------
    # Videos with tags:
    # video1 -> ["tutorial", "python"]
    # video2 -> ["tutorial", "java"]
    # video3 -> ["python", "coding"]
    #
    # Query: video1 (index 0)
    # Explanation:
    # - There are no videos before video1, so no similar videos are found.
    videos3 = [
        ["tutorial", "python"],  # video1 (index 0)
        ["tutorial", "java"],    # video2 (index 1)
        ["python", "coding"]     # video3 (index 2)
    ]
    query_index3 = 0  # Choosing video1 as the query video.
    result3 = find_similar_videos(videos3, query_index3)
    
    print("Test Case 3:")
    print("Videos:")
    for idx, tags in enumerate(videos3):
        print(f"  video{idx+1}: {tags}")
    print(f"Query video: video{query_index3+1} with tags {videos3[query_index3]}")
    print("Similar videos (indices):", result3)
    print("Similar videos (names):", [f"video{i+1}" for i in result3])
    print("-" * 50)

if __name__ == "__main__":
    main()
