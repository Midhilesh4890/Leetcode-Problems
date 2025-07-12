import ipaddress

class IPToCountryMapper:
    def __init__(self, ip_ranges):
        """
        Initializes the IP to Country mapping.
        :param ip_ranges: List of tuples (start_ip, end_ip, country)
        """
        self.ranges = [(int(ipaddress.IPv4Address(start)), int(ipaddress.IPv4Address(end)), country) 
                       for start, end, country in ip_ranges]
        # Sorting for efficient searching
        self.ranges.sort()

    def find_country(self, ip):
        """
        Finds the country for a given IP.
        :param ip: IP address as a string
        :return: Country name or 'Not Found'
        """
        ip_int = int(ipaddress.IPv4Address(ip))
        
        # Binary Search for faster lookup
        left, right = 0, len(self.ranges) - 1
        while left <= right:
            mid = (left + right) // 2
            start, end, country = self.ranges[mid]
            
            if start <= ip_int <= end:
                return country
            elif ip_int < start:
                right = mid - 1
            else:
                left = mid + 1
        
        return "Not Found"

# Example usage
ip_ranges = [
    ("1.1.0.1", "1.1.0.10", "IND"),
    ("1.1.0.20", "1.1.0.30", "FR"),
    ("2.2.2.1", "2.2.2.5", "US")
]

mapper = IPToCountryMapper(ip_ranges)

# Test Case
print(mapper.find_country("1.1.0.5"))  # Output: IND
print(mapper.find_country("1.1.0.25")) # Output: FR
print(mapper.find_country("2.2.2.3"))  # Output: US
print(mapper.find_country("3.3.3.3"))  # Output: Not Found
