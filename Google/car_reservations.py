import heapq


def assign_cars(reservations):
    sorted_reservations = sorted(enumerate(reservations), key=lambda x: x[1][0])

    # Tracks available cars (min heap of end times)
    available_cars = []

    car_assignments = [0] * len(reservations)

    # Tracks total number of unique cars used
    max_cars = 0

    for original_index, (start, end) in sorted_reservations:
        # Remove cars that are now available before the current reservation
        while available_cars and available_cars[0][0] <= start:
            # Heappop the end time and push back the car number to reuse
            _, car_num = heapq.heappop(available_cars)
            car_assignments[original_index] = car_num
            car_assigned = True
            break
        else:
            # If no available cars, create a new car
            car_assigned = False

        if not car_assigned:
            # Assign a new car
            car_num = max_cars
            max_cars += 1
            car_assignments[original_index] = car_num

        # Add this reservation's end time to the heap
        heapq.heappush(available_cars, (end, car_assignments[original_index]))

    return car_assignments


def main():
    reservations = [
        [1, 4],
        [10, 12],
        [2, 5],
        [5, 8],
        [3, 6],
        [7, 9],
    ]

    car_assignments = assign_cars(reservations)

    print("Reservations:", reservations)
    print("Car Assignments:", car_assignments)
    print("Minimum number of cars needed:", len(set(car_assignments)))


if __name__ == "__main__":
    main()