import asyncio
import uvicorn

from market import main as market

from authentication import main as auth

async def application(router_1, router_2):

    ports = {1: 5000, 2: 8000}

    async def runner(router, type=None):

        config = uvicorn.Config(router, host="0.0.0.0", port=ports[type])
        server = uvicorn.Server(config)
        await server.serve()

    await asyncio.gather(runner(router_1, 1), runner(router_2, 2))


if __name__ == '__main__':
    asyncio.run(application(market.app, auth.app))