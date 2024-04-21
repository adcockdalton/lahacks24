from dataclasses import dataclass
from datetime import datetime

from uagents import Model

from multiagency.models import Event, Student


@dataclass(kw_only = True, frozen = True)
class InitAgent(Model):
    pass


@dataclass(kw_only = True, frozen = True)
class OrgJoinRequest(Model):  # org wants to add a rep
    event: str
    description: str
    location: str
    start: datetime


@dataclass(kw_only = True, frozen = True)
class OrgJoinSuccess(Model):  # org successfully added a rep
    persona: str
    age: int
    bio: str
    gender: str


@dataclass(kw_only = True, frozen = True)
class RepJoinRequest(Model):  # rep wants to join a specific event
    persona: str
    age: int
    bio: str
    gender: str


@dataclass(kw_only = True, frozen = True)
class RepJoinSuccess(Model):  # rep successfully joined a specific event
    event: str
    description: str
    location: str
    start: datetime


@dataclass(kw_only = True, frozen = True)
class WeatherRequest(Model):
    location: str
    when: str
    intended_activity: str


@dataclass(kw_only = True, frozen = True)
class WeatherReport(Model):
    condition: str


@dataclass(kw_only = True, frozen = True)
class NewOrganizer(Model):
    event: Event


@dataclass(kw_only = True, frozen = True)
class NewRepresentative(Model):
    student: Student


@dataclass(kw_only = True, frozen = True)
class QueryEvents(Model):
    query_embeddings: list[float]
    n_results: int


@dataclass(kw_only = True, frozen = True)
class QueryStudents(Model):
    query_embeddings: list[float]
    n_results: int


@dataclass(kw_only = True, frozen = True)
class QueryEventsResponse(Model):
    events: list[Event]


@dataclass(kw_only = True, frozen = True)
class QueryStudentsResponse(Model):
    students: list[Student]

