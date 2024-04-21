from dataclasses import dataclass


@dataclass
class Event:
    event: str
    description: str
    agent_address: str


@dataclass
class Student:
    persona: str
    bio: str
    agent_address: str


