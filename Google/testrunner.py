# There is a testRunner funtion that takes multiple unit test and returns if those uts are executed together & then there is some error or not. If no error then return true other wise false. You have been given N unit tests, and you know that when you run all test cases at a time then it fails. Now you need to find at least one pair of UTs, which fails when executed at the same time using the test runner.

# Its easy when we assume that the testRunner takes O(1) to execute any number of test cases. But for the case when the test runner takes O(n) time to execute n test cases at a time then find the optimal way to find one pair of failed UTs.

# Note there may be multiple pairs that fail with each other, but need to report only one. Also all the UTs are running ok when executed individaullay.

# Any suggestion on how to solve this with optimal manner?

from typing import List, Optional

def test_runner(tests: List[int]) -> bool:
    """
    Simulates the test execution and determines if the test set passes.
    Returns True if the test set runs successfully, False if it fails.
    
    Assumed failure condition: Running test 7 and test 10 together causes a failure.
    """
    first = False
    second = False
    for test in tests:
        if test == 7:
            first = True
        if test == 10:
            second = True
    return not (first and second)  # Returns False if both 7 and 10 are in the set (failure case)

def find_faulty_pair(tests: List[int]) -> Optional[List[int]]:
    """
    Identifies at least one pair of tests that fail when run together using a divide-and-conquer approach.
    
    Steps:
    1. Narrow down the failing subset using binary search.
    2. Once isolated, systematically test pairs with the found faulty test.
    
    :param tests: List of unit test IDs.
    :return: A list containing one failing pair of tests.
    """

    left, right = 0, len(tests) - 1

    # Step 1: Find a minimal failing subset using binary search
    while left < right:
        mid = (left + right) // 2
        subset = tests[left:mid + 1]  # Take the left half
        
        if not test_runner(subset):  # If this subset fails, the faulty pair must be here
            right = mid  # Reduce the search space to the failing subset
        else:
            left = mid + 1  # Move to the right half

    # After binary search, left index should contain one faulty test
    faulty_test = tests[left]

    # Step 2: Find another test that, when run with the faulty test, causes a failure
    for test in tests:
        if test != faulty_test and not test_runner([test, faulty_test]):
            return [test, faulty_test]  # Return the first failing pair found

    return None  # Should not reach here under given assumptions

# Example usage
tests = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_faulty_pair(tests))
