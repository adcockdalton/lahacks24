import json
import os

from uagents import Context, Protocol, Agent, Bureau
from uagents.query import query

from multiagency2.embedder import EventEmbedder
from multiagency2.vector_db import VectorDB
from multiagency2.weatherman import WeatherRequest, weatherman


# WEATHERMAN = "agent1qv7h7t3fxqpkxvnzuy5yh4a8z4jd5tvlv7s7hnxyxxwgglrzn4cgxnwt970"

student_manager = Agent(name = "student manager", seed = "student")
eb = EventEmbedder()
vdb = VectorDB(local = True)


def find_similarity(*, request: str, n_results: int):
    return vdb.query(query_embeddings = eb.get_embeddings([request])[0], n_results = n_results)


@student_manager.on_event("startup")
async def init(ctx: Context):
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

    try:
        with open("../data/user.json", "r") as fobj:
            user_data: dict = json.load(fobj)

        with open("../data/context.json", "r") as fobj:
            context_data: dict = json.load(fobj)
    except FileNotFoundError:
        return

    # os.remove("../data/user.json")
    # os.remove("../data/context.json")


    # add itself to the vector embedding (mainly to store the address id)

    for uuid, data in user_data.items():
        try:
            primary_answers = " ".join(context_data[uuid]["initial"])
            contextual_answers = " ".join(context_data[uuid]["context_question"])
        except KeyError:
            continue
        persona = primary_answers+" "+contextual_answers
        events = find_similarity(request = persona, n_results = 3)

        print(uuid, persona, events)
        for county_state in events["metadatas"][0][0].values():
            county, state = county_state.split(" County, ")
            report = await query(destination = weatherman.address, message = WeatherRequest(county = county, state = state))
            print(report)
        # print(uuid, data, " ".join(context_data[uuid]["initial"]), " ".join(context_data[uuid]["context_question"]))

    with open("../data/event_result.json", "w") as fobj:
        json.dump({
            "title": "Cultural Diversity Day",
            "texts": "Celebrate the richness of cultural diversity in our school! Explore traditions, taste global cuisines, and participate in multicultural performances.",
            "metadatas": {
              "county": "New York County, New York"
            },
            "ids": "54"
          },
            fobj
        )

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

    b = Bureau()
    b.add(weatherman)
    b.add(student_manager)
    b.run()
