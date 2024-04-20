from datetime import datetime

from uagents import Agent, Context, Model

from multiagency.representative import RepJoinRequest


# this will be per (active) event


class OrgJoinRequest(Model):  # org wants to add a rep
    event: str
    description: str
    location: str
    start: datetime


class OrgJoinSuccess(Model):  # org successfully added a rep
    persona: str
    age: int
    bio: str
    gender: str


org = Agent(name="organizer", seed = "org1")


@org.on_event("startup")
async def init(ctx: Context):  # create upon a creation of new event
    ctx.logger.info(f"Organizer initiated: {ctx.address}")


@org.on_message(model = RepJoinRequest)
async def request_by_representative(ctx: Context, sender: str, msg: RepJoinRequest):
    ctx.logger.info(f"Received message from {sender}: {msg}")


@org.on_message(model = OrgJoinSuccess)
async def response_by_representative(ctx: Context, sender: str, msg: OrgJoinSuccess):
    ctx.logger.info(f"Received message from {sender}: {msg}")

