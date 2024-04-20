from uagents import Agent, Context

rep = Agent(name="representative", seed = "blah blah blah")

@rep.on_event("startup")
async def init(ctx: Context):
    print("Representative initiated!")
    print(ctx.name)

@rep.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')
    ctx.logger.info(f'uAgent address: {ctx.address}')
    ctx.logger.info(f'Fetch network address: {rep.wallet.address()}')

@rep.on_interval(period = 3.0)
async def in_mem_info(ctx: Context):
    personality = ctx.storage.get("personality") or 0
    ctx.logger.info(f'My personality is: {personality}')

    ctx.storage.set("personality", personality+1)

@rep.on_interval(period=7.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')
    ctx.logger.info(f'uAgent address: {ctx.address}')
    ctx.logger.info(f'Fetch network address: {rep.wallet.address()}')

if __name__ == '__main__':
    rep.run()
