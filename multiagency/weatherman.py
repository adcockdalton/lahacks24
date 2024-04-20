from uagents import Agent, Context, Model


# single intelligent agent compiling weather report for a location with a specified activity


class WeatherRequest(Model):
    location: str
    when: str
    intended_activity: str


class WeatherReport(Model):
    condition: str



wm = Agent(name="weatherman", seed = "weatherman")


@wm.on_event("startup")
async def init(ctx: Context):  # singleton sort-of
    ctx.logger.info(f"Weatherman initiated: {ctx.address}")

