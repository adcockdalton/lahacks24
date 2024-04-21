import json
import os

from uagents import Context, Protocol, Agent

from multiagency2.embedder import EventEmbedder
from multiagency2.vector_db import VectorDB


student_manager = Agent(name = "student")
eb = EventEmbedder()
vdb = VectorDB(local = True)


def find_similarity(*, request: str, n_results: int):
    return vdb.query(query_embeddings = eb.get_embeddings([request])[0], n_results = n_results)


@student_manager.on_event("start")
async def init(ctx: Context):
    # initialize vector db (with a local path to load/save datas)
    pass


@student_manager.on_interval(period = 15.0)
async def check_new_student(ctx: Context):  # for each new student created
    """ for each new user created
    - get event rec. from static event data (base) from vector db & embeddings (top 5?)
    - request [Weatherman] to check the weather condition at the event location if OUTDOORS for the ACTIVITY along the ROUTE
    - request each plausible [Organizer] to check if the rep itself should join (pass some basic info of itself)
    """
    ctx.logger.info(f"Students initiated: {ctx.address}")

    # manage file data

    with open("../data/user.json", "r") as fobj:
        user_data: dict = json.load(fobj)

    with open("../data/context.json", "r") as fobj:
        context_data: dict = json.load(fobj)

    # TODO
    # os.remove("../data/user.json")
    # os.remove("../data/context.json")


    # add itself to the vector embedding (mainly to store the address id)

    for uuid, data in user_data.items():
        primary_answers = " ".join(context_data[uuid]["initial"])
        contextual_answers = " ".join(context_data[uuid]["context_question"])
        persona = primary_answers+" "+contextual_answers
        events = find_similarity(request = persona, n_results = 3)

        print(uuid, persona, events)
        # print(uuid, data, " ".join(context_data[uuid]["initial"]), " ".join(context_data[uuid]["context_question"]))

    # vector embed and request the most similar events for each user
    # request weather data? alongside


if __name__ == '__main__':
    # with open("../data/events.json", "r") as fobj:
    #     events_data: dict = json.load(fobj)
    #
    # for event in events_data:
    #     print("Embedding")
    #     vdb.add(
    #         embeddings = eb.get_embeddings([event["texts"]]),
    #         documents = [event["title"]],
    #         metadatas = [event["metadatas"]],
    #         ids = [event["ids"]]
    #     )

    student_manager.run()
