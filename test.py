from DSMonitor import func_monitor, async_func_monitor
import aiohttp
import asyncio

@func_monitor(level="DEBUG",show_output=True)
def func():
    a = 1
    b = 2
    return a+b


@async_func_monitor(level="INFO",show_output=True)
async def async_func(n):
    async with aiohttp.ClientSession() as client:
        res = await client.get('http://httpbin.org/delay/{}'.format(2))
        result = await res.json()


if __name__ == "__main__":
    func()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_func(3))
