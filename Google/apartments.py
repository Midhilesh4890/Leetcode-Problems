from collections import defaultdict

class Apartment:
    def __init__(self, aptNumber, numRooms):
        self.aptNumber = aptNumber
        self.numRooms = numRooms

class Person:
    def __init__(self, name, wants_housemates):
        self.name = name        # Unique ID (e.g., "Sam")
        self.wants_housemates = wants_housemates

def assign_apartments_to_people(apartments, people):
    """
    A direct assignment of interns to apartments under the rules:
      - If an intern does NOT want housemates, try to put them in a 1-room apt.
        If none left, put them alone in a 2+ room apt (using up that entire apt).
      - If an intern is OK with housemates, place them in any multi-room apt that still has free rooms.
      - Return a dict: aptNumber -> list of intern names assigned.
      - Some interns may remain unassigned if we run out of suitable apartments.
    """

    # Convert to lists (if not already) so we can sort/mutate.
    apartments = list(apartments)
    people = list(people)

    # Separate apartments by capacity
    single_room_apts = [a for a in apartments if a.numRooms == 1]
    multi_room_apts = [a for a in apartments if a.numRooms >= 2]

    # For convenience, track how many free rooms each apartment has left
    # and which interns are assigned. We'll use a dictionary keyed by aptNumber.
    free_rooms = {}
    assigned_interns = defaultdict(list)

    for apt in apartments:
        free_rooms[apt.aptNumber] = apt.numRooms

    # Separate people by preference
    alone_list = [p for p in people if not p.wants_housemates]
    share_list = [p for p in people if p.wants_housemates]

    # Sort apartments in a stable order if you wish; here we just keep them as given.
    # For single-room apts, no special sorting needed.
    # For multi-room apts, you could sort by capacity ascending or descending
    # if you want a particular strategy.

    # 1) Assign "no-housemate" interns
    #    First try single-room apartments, then if needed use an entire multi-room apt for one intern.
    #    We'll remove or mark apartments as 'used up' once assigned in these ways.
    used_single_room = 0
    used_multi_room = 0

    for intern in alone_list:
        # Try to find an unused single-room apt first
        single_assigned = False
        while used_single_room < len(single_room_apts):
            apt = single_room_apts[used_single_room]
            if free_rooms[apt.aptNumber] > 0:
                # Place this intern here
                assigned_interns[apt.aptNumber].append(intern.name)
                free_rooms[apt.aptNumber] = 0  # 1-room apt fully used
                used_single_room += 1         # Move on to next single-room apt
                single_assigned = True
                break
            else:
                # This single-room apt is somehow used, move on
                used_single_room += 1

        if single_assigned:
            continue

        # If no single-room apt is available, try to put them alone in a multi-room
        multi_assigned = False
        while used_multi_room < len(multi_room_apts):
            apt = multi_room_apts[used_multi_room]
            if free_rooms[apt.aptNumber] == apt.numRooms:
                # Not used yet. Put intern here alone, use up entire apt
                assigned_interns[apt.aptNumber].append(intern.name)
                free_rooms[apt.aptNumber] = 0  # all rooms blocked
                used_multi_room += 1          # move on to next multi-room apt
                multi_assigned = True
                break
            else:
                # This multi-room apt might be partially used or already used, skip it
                used_multi_room += 1

        # If we still couldn't assign this intern, they remain unassigned

    # 2) Assign "housemate" interns
    #    We'll fill each multi-room apt that isn't fully used, as far as it has capacity left.
    m_idx = 0
    for intern in share_list:
        assigned = False
        while m_idx < len(multi_room_apts):
            apt = multi_room_apts[m_idx]
            if free_rooms[apt.aptNumber] > 0:
                # Put this intern here
                assigned_interns[apt.aptNumber].append(intern.name)
                free_rooms[apt.aptNumber] -= 1
                assigned = True
                break
            else:
                # This apartment is fully used, move on
                m_idx += 1

        # if assigned = False after the while loop, no multi-room apt has space left
        # We could consider single-room leftover if the person doesn't mind living alone,
        # but the problem statement implies they'd prefer 2+ if "wants_housemates".
        # The problem also states "they may not get what they want"; if you want
        # to place them in leftover single-room, you could do so here. That is optional.

    # Build final dictionary: aptNumber -> list of occupant names
    return dict(assigned_interns)

# ---------------------------------------------------------------------------
# Example usage:

if __name__ == "__main__":
    apartments = [
        Apartment(101, 1),  # single-room
        Apartment(102, 3),  # multi-room
        Apartment(103, 2),  # multi-room
        Apartment(104, 1)   # single-room
    ]

    interns = [
        Person("Alice", False),   # doesn't want housemates
        Person("Bob", True),      # wants housemates
        Person("Charlie", True),  # wants housemates
        Person("Diana", False),   # doesn't want housemates
        Person("Ellen", True)     # wants housemates
    ]

    assigned_map = assign_apartments_to_people(apartments, interns)

    for apt_num in sorted(assigned_map.keys()):
        print(f"Apartment {apt_num} -> {assigned_map[apt_num]}")
