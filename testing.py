import sys
import os

# Get the current directory (where the test.py file is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the root directory (two levels up from current_dir)
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))

print(os.pardir)
