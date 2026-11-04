from collections import defaultdict
import csv
import os


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find file: {csv_path}")

    rides_list = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rides_list.append(
                {
                    "ride_id": row["ride_id"],
                    "start_station": row["start_station"],
                    "end_station": row["end_station"],
                    "duration_min": float(row["duration_min"]),
                    "rider_type": row["rider_type"],
                }
            )
    return rides_list


def average_duration(rides: list[dict[str, object]]) -> float:
    """Return the average ride duration in minutes."""
    if not rides:
        return 0.0
    total = sum(float(ride["duration_min"]) for ride in rides)
    return total / len(rides)


def count_by_rider_type(rides: list[dict[str, object]]) -> dict[str, int]:
    """Count rides for each rider type."""
    counts: dict[str, int] = defaultdict(int)
    for ride in rides:
        counts[str(ride["rider_type"])] += 1
    return dict(counts)


def busiest_start_station(rides: list[dict[str, object]]) -> str:
    """Return the start station with the most rides."""
    if rides is None:
        raise ValueError("rides must not be None")
    if not rides:
        raise ValueError("rides must not be empty")

    counts: dict[str, int] = {}
    for ride in rides:
        station = str(ride["start_station"])
        counts[station] = counts.get(station, 0) + 1
    return max(counts, key=counts.get)


def filter_long_rides(
    rides: list[dict[str, object]], min_duration: float = 30
) -> list[dict[str, object]]:
    """Return all rides with duration greater than or equal to min_duration minutes."""
    return [ride for ride in rides if float(ride["duration_min"]) >= min_duration]