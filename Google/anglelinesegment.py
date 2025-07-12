import math

def angle_from_origin(x, y):
    # Calculate the angle in radians between the positive x-axis and the point (x, y)
    # atan2 returns a value in the range [-π, π]
    return math.atan2(y, x)

def does_not_intersect(origin_x, origin_y, target_x, target_y, line_segments):
    # Check if a line from (origin_x, origin_y) to (target_x, target_y) intersects with any line segments
    # Returns True if there is NO intersection, False if there IS an intersection
    
    # If origin and target are the same point, no meaningful line exists
    if origin_x == target_x and origin_y == target_y:
        return True
    
    # Calculate angles of all line segments as seen from the origin
    angles = []
    for x1, y1, x2, y2 in line_segments:
        # Translate points relative to our origin point
        rel_x1, rel_y1 = x1 - origin_x, y1 - origin_y
        rel_x2, rel_y2 = x2 - origin_x, y2 - origin_y
        
        # Skip degenerate line segments (points)
        if rel_x1 == rel_x2 and rel_y1 == rel_y2:
            continue
            
        # Calculate angles for both endpoints of the segment
        angle1 = angle_from_origin(rel_x1, rel_y1)
        angle2 = angle_from_origin(rel_x2, rel_y2)
        
        # Ensure angle1 <= angle2, but preserve the correct arc
        if abs(angle1 - angle2) > math.pi:
            # If the difference is more than π, we need to adjust to get the smaller arc
            if angle1 < angle2:
                angle1 += 2 * math.pi
            else:
                angle2 += 2 * math.pi
                
        # Now ensure angle1 <= angle2 for consistency
        if angle1 > angle2:
            angle1, angle2 = angle2, angle1
            
        # Add this angle range to our list
        angles.append((angle1, angle2))
    
    # Sort angles by their starting angle
    angles.sort()
    
    # Calculate target angle from origin
    target_angle = angle_from_origin(target_x - origin_x, target_y - origin_y)
    
    # Check if target_angle falls within any of the angle ranges
    for start_angle, end_angle in angles:
        if start_angle <= target_angle <= end_angle:
            # The target angle is blocked by a line segment
            return False
    
    # No intersection found
    return True

# Example usage
line_segments = [
    (1, 1, 2, 2),     # Line from (1, 1) to (2, 2)
    (-1, 1, 1, -1),   # Line from (-1, 1) to (1, -1)
]

# Testing a line from origin (0,0) to point (3,3)
result = does_not_intersect(0, 0, 3, 3, line_segments)
print(result)  # Should print whether the line does not intersect with any segments