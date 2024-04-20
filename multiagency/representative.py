from datetime import datetime

from uagents import Agent, Context, Model

from multiagency.organizer import OrgJoinRequest


# this will be per user


class RepJoinRequest(Model):  # rep wants to join a specific event
    persona: str
    age: int
    bio: str
    gender: str


class RepJoinSuccess(Model):  # rep successfully joined a specific event
    event: str
    description: str
    location: str
    start: datetime



rep = Agent(name="representative", seed = "rep1")


@rep.on_event("startup")
async def init(ctx: Context):  # for each new user created
    """ for each new user created
    - get event rec. from static event data (base) from vector db & embeddings (top 5?)
    - request [Weatherman] to check the weather condition at the event location if OUTDOORS for the ACTIVITY along the ROUTE
    - request each plausible [Organizer] to check if the rep itself should join (pass some basic info of itself)
    :param ctx:
    :return:
    """
    ctx.logger.info(f"Representative initiated: {ctx.address}")

    # to find and match event
    # vector database to find the top 5 events based off static information (personality, etc.)

    # await ctx.send(RECIPIENT_ADDRESS, Message(message = "hello there slaanesh"))


@rep.on_message(model = OrgJoinRequest)
async def request_by_organizer(ctx: Context, sender: str, msg: OrgJoinRequest):
    ctx.logger.info(f"Received message from {sender}: {msg}")


@rep.on_message(model = RepJoinSuccess)
async def response_by_organizer(ctx: Context, sender: str, msg: RepJoinSuccess):
    ctx.logger.info(f"Received message from {sender}: {msg}")

