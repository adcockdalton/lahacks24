import asyncio
import logging
from multiprocessing import Process, log_to_stderr

from uagents import Bureau, Agent

from multiagency.librarian import lib
from multiagency.organizer import org_ptc
from multiagency.representative import rep_ptc
from multiagency.weatherman import wm


class MatcherUniverse:
    REPRESENTATIVE_COUNTER = 0
    ORGANIZER_COUNTER = 0

    def __init__(self):
        log_to_stderr(logging.DEBUG)

        self._procs: list[Process] = []

        # self.loop = asyncio.get_event_loop()

        self.run(wm)
        self.run(lib)

    def add_representative(self):
        # agent1q2r39kn8tam8zxknjjhxnndgvu9wef6d9e0nmdxl9hz6lhqyk466ch97mcz
        rep = Agent(name="representative", seed = f"rep{self.REPRESENTATIVE_COUNTER}")
        rep.include(rep_ptc)

        self.REPRESENTATIVE_COUNTER += 1

        self.run(rep)

    def add_organizer(self):
        # agent1qd9ehy0tdzryhyssyuehx55t06xz4hlhml7l3tugczkdkrv0yw85wj4urp7
        org = Agent(name="organizer", seed = f"org{self.ORGANIZER_COUNTER}")
        org.include(org_ptc)

        self.ORGANIZER_COUNTER += 1

        self.run(org)


    def run(self, agent):
        async def inner_main():
            async def inner():
                agent.run()

            # loop = asyncio.get_running_loop()
            asyncio.create_task(inner())

        asyncio.run(inner_main())

        # self.loop.run_forever()

        # self.agent = agent.run

        # proc = Process(target = agent.run)
        # proc.start()

        # self._procs.append(proc)

    def exit(self):
        pass


def add_representative(seed: str):
    rep = Agent(name="representative", seed = seed)
    rep.include(rep_ptc)

    asyncio.create_task(rep.run())

def add_organizer(seed: str):
    org = Agent(name="organizer", seed = seed)
    org.include(org_ptc)

    asyncio.create_task(org.run())

async def main():
    loop = asyncio.get_running_loop()
    loop.create_task(wm.run())
    loop.create_task(lib.run())

    rep_counter = 0
    org_counter = 0

    while (inp := input(">>>")):
        match inp:
            case "O":
                add_organizer(f"org{org_counter}")
                org_counter += 1
            case "R":
                add_representative(f"rep{rep_counter}")
                rep_counter += 1
            case "Q":
                break



    # rep = Agent(name = "representative", seed = f"rep{self.REPRESENTATIVE_COUNTER}")
    # rep.include(rep_ptc)
    #
    # self.REPRESENTATIVE_COUNTER += 1
    #
    # self.run(rep)
    #
    # org = Agent(name = "organizer", seed = f"org{self.ORGANIZER_COUNTER}")
    # org.include(org_ptc)
    #
    # self.ORGANIZER_COUNTER += 1
    #
    # self.run(org)



if __name__ == "__main__":
    asyncio.run(main())

# if __name__ == '__main__':
#     matching = MatcherUniverse()
#     while (inp := input(">>>")):
#         match inp:
#             case "O":
#                 matching.add_organizer()
#             case "R":
#                 matching.add_representative()
#             case "Q":
#                 break
#
#     matching.exit()

