from mobility_stats.rides import (
    average_duration,
    busiest_start_station,
    count_by_rider_type,
)


def build_summary(rides: list[dict[str, object]]) -> dict[str, object]:
    """Build a compact dictionary with headline statistics."""
    return {
        "ride_count": len(rides),
        "average_duration": average_duration(rides),
        "rider_types": count_by_rider_type(rides),
        "busiest_start_station": busiest_start_station(rides) if rides else None,
    }


def format_summary(summary: dict[str, object]) -> str:
    """Create a human-readable text summary."""
    return (
        "Mobility summary\n"
        f"Rides: {summary['ride_count']}\n"
        f"Average duration: {summary['average_duration']:.1f} min\n"
        f"Busiest start: {summary['busiest_start_station']}"
    )