from dataclasses import dataclass
from datetime import datetime


@dataclass
class Update:
    station_id: int
    """The ID of the station, as for the Bicing service."""
    updated: datetime
    """The last time this was updated."""

    bikes: int
    """The number of bikes."""
    ebikes: int
    """The number of electrical bikes."""
    free: int
    """The available docks."""
    active: bool
    """Whether the station is working (vs closed)."""

    def __hash__(self) -> int:
        return hash((self.station_id, self.updated))

    def __eq__(self, other):
        return self.station_id == other.station_id and self.updated == other.updated
