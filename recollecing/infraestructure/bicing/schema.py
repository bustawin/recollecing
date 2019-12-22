from datetime import datetime, timedelta
from typing import List

import pydantic as p


class Update(p.BaseModel):
    station_id: p.conint(ge=0)
    updated: datetime = p.Field(..., alias="last_reported")
    bikes: int = p.Field(..., alias="num_bikes_available_types", ge=0)
    ebikes: int = p.Field(..., alias="num_bikes_available_types", ge=0)
    free: int = p.Field(..., alias="num_docks_available", ge=0)
    active: bool = p.Field(..., alias="status")

    @p.validator("active", pre=True)
    def parse_active(cls, v: str):
        return v == "IN_SERVICE"

    @p.validator("bikes", pre=True)
    def parse_bikes(cls, v: dict):
        return v["mechanical"]

    @p.validator("ebikes", pre=True)
    def parse_ebikes(cls, v: dict):
        return v["ebike"]


class Response(p.BaseModel):
    next_update: timedelta = p.Field(..., alias="ttl")
    updates: List[Update] = p.Field(..., alias="data")

    @p.validator("updates", pre=True)
    def coerce_updates(cls, data):
        return data["stations"]
