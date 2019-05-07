import asyncio
import time
from functools import reduce

async def gg(n):
    print(n)


async def ff():
    print('111')
    await asyncio.Task(gg(1))
    print('ff11')


async def ff2():
    print('222')
    await asyncio.Task(gg(2))
    # await gg(2)
    print('ff22')

async def bar(i):
    await asyncio.sleep(1)
    return [i]


# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([ff(), ff2()]))

async def foo():
    for i in range(100):
        res = await bar(i)
        print(res)

async def foo2():
    t1 = time.time()
    from functools import reduce
    res =  reduce(lambda x,y:x+y, await asyncio.gather(*[bar(i) for i in range(10)]))
    print(res)
    print(time.time() - t1)
    return res

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([foo2()]))
