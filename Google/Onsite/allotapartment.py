# Your organization has hired interns who need to relocate for the summer. 
# You are in charge of assigning apartments to them. 
# Each intern will get their own room. 
# They can choose whether they prefer to share a 2+ room apartment or get a 
# one-bedroom to themselves.
# Note that they may not get what they want because the apartments vary in the 
# number of rooms that they have.


# You have the following data structures:


# public class Apartment {
#     public int aptNumber;
#     public int numRooms;
# }

# public class Person {
#     public String name; #Unique ID, ex: Sam
#     public boolean wants_housemates
# }

# public Map<Integer, Collection<String>> assignApartmentsToPeople(
#     Collection<Apartment> apartments, #List of Apartment
#     Collection<Person> people){
#     // return apartment to people  map
#     }

from collections import deque
from typing import List, Dict

class Apartment:
    def __init__(self, apt_number: int, num_rooms: int):
        self.apt_number = apt_number
        self.num_rooms = num_rooms

    def __repr__(self):
        return f"Apartment({self.apt_number}, {self.num_rooms})"

class Person:
    def __init__(self, name: str, wants_housemates: bool):
        self.name = name
        self.wants_housemates = wants_housemates

def assign_apartments_to_people(apartments: List[Apartment], people: List[Person]) -> Dict[int, List[str]]:
    # The resulting mapping: apartment number -> list of intern names
    assignment = {}

    # Separate apartments into one-bedroom and multi-bedroom lists
    one_bedroom = []
    multi_bedroom = []
    for apt in apartments:
        if apt.num_rooms == 1:
            one_bedroom.append(apt)
        else:
            multi_bedroom.append(apt)
    
    # Separate people by their preference:
    # - prefer_alone: those who do NOT want housemates (wants_housemates == False)
    # - prefer_share: those who are okay with sharing (wants_housemates == True)
    prefer_alone = deque([p for p in people if not p.wants_housemates])
    prefer_share = deque([p for p in people if p.wants_housemates])
    
    # First, assign one-bedroom apartments:
    # Ideally, give these to interns who want to live alone.
    for apt in one_bedroom:
        if prefer_alone:
            person = prefer_alone.popleft()
            assignment[apt.apt_number] = [person.name]
        elif prefer_share:
            # If no one prefers to live alone, assign an intern who is okay with sharing.
            person = prefer_share.popleft()
            assignment[apt.apt_number] = [person.name]
    
    # Next, assign multi-bedroom apartments.
    # Each apartment can accommodate 'num_rooms' interns.
    # Fill each apartment first with those who want to share, then use remaining capacity for those who want to live alone.
    for apt in multi_bedroom:
        occupants = []
        capacity = apt.num_rooms
        
        # Fill with interns who prefer sharing
        while capacity > 0 and prefer_share:
            person = prefer_share.popleft()
            occupants.append(person.name)
            capacity -= 1
        
        # If there is still capacity, assign interns who prefer living alone.
        while capacity > 0 and prefer_alone:
            person = prefer_alone.popleft()
            occupants.append(person.name)
            capacity -= 1
        
        if occupants:
            assignment[apt.apt_number] = occupants

    # Note: If any interns remain unassigned, it means there wasn't enough total room capacity.
    return assignment

# --- Test Case ---

def main():
    # Create some sample apartments:
    apartments = [
        Apartment(apt_number=101, num_rooms=1),  # one-bedroom
        Apartment(apt_number=102, num_rooms=3),  # multi-bedroom with 3 rooms
        Apartment(apt_number=103, num_rooms=2)   # multi-bedroom with 2 rooms
    ]
    
    # Create a list of interns with their preferences:
    people = [
        Person("Sam", wants_housemates=False),   # prefers to live alone
        Person("Alex", wants_housemates=True),     # okay with sharing
        Person("Chris", wants_housemates=False),   # prefers to live alone
        Person("Pat", wants_housemates=True)         # okay with sharing
    ]
    
    assignment = assign_apartments_to_people(apartments, people)
    print("Apartment Assignments:")
    for apt_number, occupants in assignment.items():
        print(f"Apartment {apt_number}: {occupants}")

if __name__ == "__main__":
    main()
