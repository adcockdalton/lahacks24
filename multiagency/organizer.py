import datetime

from uagents import Context, Protocol
from uagents.query import query

from multiagency.message_models import OrgJoinSuccess, RepJoinRequest, RepJoinSuccess, \
    OrgJoinRequest, InitAgent, NewOrganizer, QueryStudents
from multiagency.models import Event


# this will be per (active) event

LIBRARIAN_ADDRESS = "agent1qflnnpk47zfu8gxc3p8hpdwtr0ajl754ruhp2kg2q4x6nutvuzpdyrsu242"
WEATHERMAN_ADDRESS = "agent1qv7h7t3fxqpkxvnzuy5yh4a8z4jd5tvlv7s7hnxyxxwgglrzn4cgxnwt970"

org_ptc = Protocol(name="representative", version = "0.1")


@org_ptc.on_message(model = InitAgent)
async def init(ctx: Context, _sender: str, _msg: InitAgent):  # create upon a creation of new event
    ctx.logger.info(f"Organizer initiated: {ctx.address}")

    # add itself to the vector embedding  (mainly to store the address id)

    await ctx.send(
        LIBRARIAN_ADDRESS,
        NewOrganizer(event = Event(event = "LA Hakcs", description = "Developing next generation ideas and products", agent_address = ctx.address))
    )

    for destinations in await query(LIBRARIAN_ADDRESS, QueryStudents(query_embeddings = [0.0], n_results = 1)):
        print("event destinations:", destinations)

    # request multiple compatible students

    # await ctx.send(
    #     "agent1q2r39kn8tam8zxknjjhxnndgvu9wef6d9e0nmdxl9hz6lhqyk466ch97mcz",
    #     OrgJoinRequest(
    #         event = "Super cool event! II",
    #         description = "Super duper long description",
    #         location = "1032 Bryan Ave. Irvine, CA",
    #         start = datetime.datetime.today(),
    #     )
    # )


@org_ptc.on_message(model = RepJoinRequest)
async def request_by_representative(ctx: Context, sender: str, msg: RepJoinRequest):
    ctx.logger.info(f"Received message from {sender}: {msg}")

    if True:
        await ctx.send(
            "agent1q2r39kn8tam8zxknjjhxnndgvu9wef6d9e0nmdxl9hz6lhqyk466ch97mcz",
            RepJoinSuccess(
                event = "Super cool event!",
                description = "Super duper long description",
                location = "1032 Bryan Ave. Irvine, CA",
                start = datetime.datetime.today(),
            )
        )

        print("ADD GUEST TO EVENT!")


@org_ptc.on_message(model = OrgJoinSuccess)
async def response_by_representative(ctx: Context, sender: str, msg: OrgJoinSuccess):
    ctx.logger.info(f"Received message from {sender}: {msg}")

    # add this user to the guest list

    print("ADD GUEST TO EVENT!")

