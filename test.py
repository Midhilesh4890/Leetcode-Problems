first  = [11, 12, 13, 14, 15, 16]
second = [71, 77, 89, 51, 90, 59]
# Add two lists element-wise using zip() & sum()
final_list = [abs(a - b) for a,b in zip(first, second)]
print(final_list)
