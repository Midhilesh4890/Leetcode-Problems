def schedule_meetings(meetings, dns):
    """
    Given a list of meeting intervals and one DNS interval,
    returns the list of meeting intervals (non-overlapping) after merging
    and subtracting out the DNS time.
    
    Each interval is a tuple (start, end) where the interval is closed on the left
    and open on the right: [start, end).
    """
    
    # Unpack the DNS interval for clarity.
    dns_start, dns_end = dns

    # 1. Sort the meetings by their start time.
    #    Sorting ensures that when we merge intervals, we process them in order.
    meetings.sort(key=lambda x: x[0])
    
    # 2. Merge overlapping meeting intervals.
    merged = []  # This list will hold the merged intervals.
    for meeting in meetings:
        # If merged is empty or the last merged meeting does not overlap the current one:
        if not merged or merged[-1][1] < meeting[0]:
            # No overlap: add this meeting as is.
            merged.append(list(meeting))  # using list so we can update end time easily.
        else:
            # There is an overlap: merge by extending the last meeting's end time if needed.
            merged[-1][1] = max(merged[-1][1], meeting[1])
    print(merged)
    # 3. Remove (cut out) the DNS portion from each merged meeting interval.
    result = []  # This will store our final meeting intervals after DNS removal.
    for interval in merged:
        start, end = interval
        
        # Check if the current meeting interval does not overlap the DNS slot at all.
        # There are two cases:
        #   a) The entire meeting is before the DNS starts.
        #   b) The entire meeting is after the DNS ends.
        if end <= dns_start or start >= dns_end:
            result.append((start, end))
        else:
            # The meeting interval overlaps with the DNS period.
            # There are several possibilities:
            
            # Case 1: Meeting starts before DNS, so we can keep the part before the DNS.
            if start < dns_start:
                # We add the interval from the start of the meeting until the DNS starts.
                result.append((start, dns_start))
            
            # Case 2: Meeting ends after DNS, so we can keep the part after the DNS.
            if end > dns_end:
                # We add the interval from the DNS end until the meeting's end.
                result.append((dns_end, end))
            # Note: If the meeting is completely within the DNS slot,
            # neither condition will be true and nothing is added.
    
    return result

# -------------------------------
# Example usage with the sample input:

meetings = [(1, 7), (5, 10), (12, 30), (22, 30), (40, 50), (60, 70)]
dns = (18, 25)
print(schedule_meetings(meetings, dns))
# Expected output: [(1, 10), (12, 18), (25, 30), (40, 50), (60, 70)]
