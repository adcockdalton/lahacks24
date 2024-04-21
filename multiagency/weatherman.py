from uagents import Agent, Context


# single intelligent agent compiling weather report for a location with a specified activity


# agent1qv7h7t3fxqpkxvnzuy5yh4a8z4jd5tvlv7s7hnxyxxwgglrzn4cgxnwt970
wm = Agent(name="weatherman", seed = "weatherman")


@wm.on_event("startup")
async def init(ctx: Context):  # singleton sort-of
    ctx.logger.info(f"Weatherman initiated: {ctx.address}")

