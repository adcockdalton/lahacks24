from uagents import Agent, Context

from multiagency.message_models import NewRepresentative, NewOrganizer, QueryEvents, QueryStudents, \
    QueryEventsResponse, QueryStudentsResponse
from multiagency.models import Event, Student


# agent1qflnnpk47zfu8gxc3p8hpdwtr0ajl754ruhp2kg2q4x6nutvuzpdyrsu242
lib = Agent(name="librarian", seed = "librarian")


@lib.on_event("startup")
async def init(ctx: Context):  # singleton sort-of
    ctx.logger.info(f"Librarian initiated: {ctx.address}")

    ctx.storage.set("organizers", [])
    ctx.storage.set("representatives", [])


@lib.on_message(model = NewOrganizer)
async def add_organizer(ctx: Context, sender: str, msg: NewOrganizer):
    organizers: list[Event] = ctx.storage.get("organizers")
    organizers.append(msg.event)
    ctx.storage.set("organizers", organizers)


@lib.on_message(model = NewRepresentative)
async def add_representative(ctx: Context, sender: str, msg: NewRepresentative):
    representatives: list[Student] = ctx.storage.get("representatives")
    representatives.append(msg.student)
    ctx.storage.set("representatives", representatives)


@lib.on_query(model = QueryEvents, replies = {QueryEventsResponse})
async def query_events_embedding(ctx: Context, sender: str, msg: QueryEvents):
    await ctx.send(sender, QueryEventsResponse(events = ctx.storage.get("organizers")))


@lib.on_query(model = QueryStudents, replies = {QueryStudentsResponse})
async def query_students_embedding(ctx: Context, sender: str, msg: QueryStudents):
    await ctx.send(sender, QueryEventsResponse(events = ctx.storage.get("representatives")))



