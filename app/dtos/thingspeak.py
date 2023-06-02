from typing import List
from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, Undefined, config


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=False)
class FeedBase:
    temperature_dht: float = field(metadata=config(field_name="field1"), default=float)
    humidity_dht: float = field(metadata=config(field_name="field2"), default=float)
    temperature_ext: float = field(metadata=config(field_name="field3"), default=float)
    temperature_int: float = field(metadata=config(field_name="field4"), default=float)
    temperature_bmp: float = field(metadata=config(field_name="field5"), default=float)
    airpreassure: float = field(metadata=config(field_name="field6"), default=float)
    ligth_infrared: float = field(metadata=config(field_name="field7"), default=float)
    ligth_lux: float = field(metadata=config(field_name="field8"), default=float)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass(frozen=False)
class ThingspeakResponse:
    feeds: List[FeedBase] = field(default=None)
