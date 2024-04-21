import datetime

from uagents import Context, Protocol
from uagents.query import query

from multiagency.message_models import OrgJoinRequest, RepJoinSuccess, RepJoinRequest, \
    OrgJoinSuccess, InitAgent, NewRepresentative, QueryEvents
from multiagency.models import Student


# this will be per user

LIBRARIAN_ADDRESS = "agent1qflnnpk47zfu8gxc3p8hpdwtr0ajl754ruhp2kg2q4x6nutvuzpdyrsu242"
WEATHERMAN_ADDRESS = "agent1qv7h7t3fxqpkxvnzuy5yh4a8z4jd5tvlv7s7hnxyxxwgglrzn4cgxnwt970"

rep_ptc = Protocol(name="representative", version = "0.1")


@rep_ptc.on_message(model = InitAgent)
async def init(ctx: Context, _sender: str, _msg: InitAgent):  # for each new user created
    """ for each new user created
    - get event rec. from static event data (base) from vector db & embeddings (top 5?)
    - request [Weatherman] to check the weather condition at the event location if OUTDOORS for the ACTIVITY along the ROUTE
    - request each plausible [Organizer] to check if the rep itself should join (pass some basic info of itself)
    """
    ctx.logger.info(f"Representative initiated: {ctx.address}")

    # add itself to the vector embedding (mainly to store the address id)

    await ctx.send(
        LIBRARIAN_ADDRESS,
        NewRepresentative(student = Student(persona = "introvert", bio = "Love UCI", agent_address = ctx.address))
    )

    # to find and match event
    # vector database to find the top 5 events based off static information (personality, etc.)

    # request weather report

    for destinations in await query(LIBRARIAN_ADDRESS, QueryEvents(query_embeddings = [0.0], n_results = 1)):
        print("event destinations:", destinations)

    # request multiple compatible organizers

    # await ctx.send(
    #     "agent1qd9ehy0tdzryhyssyuehx55t06xz4hlhml7l3tugczkdkrv0yw85wj4urp7",
    #     RepJoinRequest(
    #         persona = "introvert",
    #         age = 23,
    #         bio = "I love food",
    #         gender = "Male",
    #     )
    # )


@rep_ptc.on_message(model = OrgJoinRequest)
async def request_by_organizer(ctx: Context, sender: str, msg: OrgJoinRequest):
    ctx.logger.info(f"Received message from {sender}: {msg}")

    if True:
        await ctx.send(
            "agent1qd9ehy0tdzryhyssyuehx55t06xz4hlhml7l3tugczkdkrv0yw85wj4urp7",
            OrgJoinSuccess(
                persona = "extrovert",
                age = 23,
                bio = "I love love love food",
                gender = "Female",
            )
        )

        # notify user upon successful entry of the event

        print("NOTIFY USER OF NEW EVENT!")



@rep_ptc.on_message(model = RepJoinSuccess)
async def response_by_organizer(ctx: Context, sender: str, msg: RepJoinSuccess):
    ctx.logger.info(f"Received message from {sender}: {msg}")

    # notify user upon successful entry of the event

    print("NOTIFY USER OF NEW EVENT!")


