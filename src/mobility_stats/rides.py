import csv
import os
from collections import defaultdict


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    rides_list = []
    if os.path.exists(csv_path) == False:
        raise FileNotFoundError(f"Could not find file: {csv_path}")
    with open(csv_path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for rides in r:
            rides.copy()
            rides_list.append(
                {
                    "ride_id": rides["ride_id"],
                    "start_station": rides["start_station"],
                    "end_station": rides["end_station"],
                    "duration_min": float(rides["duration_min"]),
                    "rider_type": rides["rider_type"],
                }
            )
    return rides_list


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    counts = 0.0
    for ride in rides:
        counts += ride["duration_min"]
    return counts / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    counts = defaultdict(int)
    for ride in rides:
        counts[ride["rider_type"]] += 1
    return dict(counts)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides == None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    counts = {}
    for ride in rides:
        d = ride["start_station"]
        counts[d] = counts.get(d, 0) + 1
    return max(counts, key=counts.get)


def filter_long_rides(rides, counts=30):
    """Return all rides with duration greater than or equal to counts minutes."""
    long_rides = []
    for ride in rides:
        if ride["duration_min"] >= counts:
            long_rides.append(ride)
    return long_rides
