# Given a set of jobs array and max number of cpus, where each job object contains 3 props {starttime,duration,numberofCpusNeeded}, write a function which returns true if the jobs can be executed with the given max cpus else return false even if one job can't be executed?
from collections import defaultdict

def can_execute_jobs(jobs, max_cpus):
    """
    Determines whether all jobs can be executed within the given max_cpus constraint.

    :param jobs: List of jobs, each represented as a dictionary with keys:
                 - "starttime": int
                 - "duration": int
                 - "numberofCpusNeeded": int
    :param max_cpus: Maximum CPUs available at any time.
    :return: True if all jobs can be executed without exceeding max_cpus, otherwise False.
    """
    timeline = defaultdict(int)

    # Populate the timeline
    for job in jobs:
        start_time = job["starttime"]
        end_time = start_time + job["duration"]
        cpus_needed = job["numberofCpusNeeded"]

        timeline[start_time] += cpus_needed  # CPUs required when job starts
        timeline[end_time] -= cpus_needed    # CPUs released when job ends

    # Sort time points and check CPU usage
    current_cpus = 0
    for time in sorted(timeline.keys()):
        current_cpus += timeline[time]
        if current_cpus > max_cpus:
            return False  # CPU limit exceeded

    return True  # All jobs can be scheduled within constraints


# Example Test Cases
jobs1 = [
    {"starttime": 1, "duration": 4, "numberofCpusNeeded": 2},  # Runs 1-5
    {"starttime": 2, "duration": 3, "numberofCpusNeeded": 3},  # Runs 2-5
    {"starttime": 5, "duration": 2, "numberofCpusNeeded": 2}   # Runs 5-7
]
max_cpus1 = 4
print(can_execute_jobs(jobs1, max_cpus1))  # Output: False (CPU demand at time 2-5 exceeds 4)

jobs2 = [
    {"starttime": 1, "duration": 3, "numberofCpusNeeded": 2},  # Runs 1-4
    {"starttime": 4, "duration": 2, "numberofCpusNeeded": 3},  # Runs 4-6
    {"starttime": 6, "duration": 1, "numberofCpusNeeded": 2}   # Runs 6-7
]
max_cpus2 = 3
print(can_execute_jobs(jobs2, max_cpus2))  # Output: True (No overlap exceeds max_cpus)
