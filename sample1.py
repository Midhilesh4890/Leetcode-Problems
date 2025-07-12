# You are given a list of transaction records in the form of dictionaries. Each transaction includes:
# customer_id: Unique ID of the customer (string)
# amount: Amount of transaction (string or float)
# date: Date of transaction (string in varying formats)
# Implement a solution in class structure with the following responsibilities:
# Clean Data
# Convert amount to float, and ignore invalid or missing values.
# Standardize date to Python datetime.date.
# Ignore records with missing customer_id.

# Extra Analysis required:
# get_total_spent(customer_id) → total amount spent by a specific customer -> df.groupby(customer_id).agg{''}
# get_top_customers(n=3) → return top n customers by total spend  --> heapq.nlargest()
# get_daily_summary() → total spend per day
 
sample_data = [
   {"customer_id": "C1", "amount": "100", "date": "2023-01-01"},
   {"customer_id": "C2", "amount": "abc", "date": "2023-01-01"},   
   {"customer_id": "C3", "amount": "200", "date": "2023/01/02"},
   {"customer_id": "C1", "amount": 150.5, "date": "02-01-2023"},   
   {"customer_id": None, "amount": "120", "date": "2023-01-03"}]

from datetime import datetime

class DataPreprocess:
   def __init__(self, data):
      self.data = self.clean_data(data)

   def preprocess_amount(self, amount):
      if isinstance(amount, str):
         return None 

      return float(amount)

   def clean_data(self, data):
      cleaned_data = []

      for row in data:
         if row.get('customer_id') is None:
            continue
         format_string = "%Y-%m-%d"

         date = datetime.strptime(row.get('date'), format_string)
         amount = self.preprocess_amount(row.get('amount'))

         if not amount:
            continue




# Input is two columns
 
# Seat ID, Available - 1 if available, and 0 if booked
 
# Write a python method that would consume this dataset and provide us
# with all the seat number combinations
# that are consecutively available.


seat = [1, 2, 3, 4, 5]

available = [1, 0, 1, 0, 1]


def solve(S, A):
   res = []

   n = len(A)

   for i in range(n - 1):
      if A[i] == 1 and  A[i + 1] == 1:
         res.append((S[i], S[i + 1]))

   return res 

print(solve(seat, available))







 







