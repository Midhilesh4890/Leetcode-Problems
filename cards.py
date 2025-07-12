# Consider a deck of normal playing cards. A playing card is represented as a string, where the first part represents the rank one of Ace and the second part represents the suit (one of Clubs C. Diamonds D. Hearts H Spades 5).


# A valid set of playing cards is a set of playing cards that fulfills one of the two following criteria:


# Criterion 1: the set has 3 or more cards and all cards in the set have the same rank and any suit. Examples:


# "AC", "AD", "AS" (1.e. Ace of Clubs. Diamonds and Spades)
# "SC" "SD" "SH", "SS" (1.e. Five of Clubs, Diamonds, Spades and Hearts)


# Criterion 2: the set has 3 or more cards and all cards in the set have the same suit and consecutive ranks. Examples:


# "9H", "10H", "JH", "QH", "KH"


# Examples of invalid sets:


# "2C", "3C": only two cards are present but a minimum of 3 are required
# "2C", "3C","5C": missing the 4 of Clubs.
# "20", "3C", "4H": not all cards have the same suit (mix of Clubs and Hearts)


# Write a function that takes as input a list of cards, and determines if the input is a valid playing card set.


# Examples:


# Input: ["2C", "2S", "2H"], Function returns: true


# Input: ["2C", "3C", "4C"], Function returns: true


# Input: ["2C", "3C", "4H"], Function returns: false

# what is this code asking explain properly and provide soltuion as well

def is_valid_card_set(cards):
    if len(cards) < 3:
        return False  # Needs at least 3 cards

    # Mapping ranks to numerical values
    rank_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    rank_values.update({str(i): i for i in range(2, 11)})  # Adding 2-10
    
    # Extract ranks and suits from cards
    ranks = [card[:-1] for card in cards]  # Remove last character (suit)
    suits = [card[-1] for card in cards]   # Get last character (suit)
    
    # Check for Criterion 1: All cards have the same rank
    if len(set(ranks)) == 1:
        return True
    
    # Check for Criterion 2: All cards have the same suit and consecutive ranks
    if len(set(suits)) == 1:  # All suits are same
        rank_nums = sorted(rank_values[r] for r in ranks)  # Convert ranks to numbers and sort
        if all(rank_nums[i] + 1 == rank_nums[i + 1] for i in range(len(rank_nums) - 1)):
            return True

    return False  # Doesn't satisfy any criterion

# Test cases
print(is_valid_card_set(["2C", "2S", "2H"]))  # True (Same rank)
print(is_valid_card_set(["2C", "3C", "4C"]))  # True (Same suit, consecutive)
print(is_valid_card_set(["2C", "3C", "4H"]))  # False (Different suits)
print(is_valid_card_set(["9H", "10H", "JH", "QH", "KH"]))  # True (Consecutive same suit)
print(is_valid_card_set(["5D", "6D", "8D"]))  # False (Gap in sequence)
print(is_valid_card_set(["10S", "JS", "QS", "KS"]))  # True (Consecutive same suit)
