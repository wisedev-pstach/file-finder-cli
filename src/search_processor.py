import os
import asyncio
import sys
import nest_asyncio
nest_asyncio.apply()

   
async def search_drive(scope, inp):
    for r, d, f in os.walk(scope): 
        for file in f:
            filepath = os.path.join(r, file)
            if inp in file:
                #counter += 1
                print(os.path.join(r, file))


def search_full_system(input):
    azDiscs = lambda: (chr(i)+":\\" for i in range(ord("A"), ord("Z") + 1))
    loop = asyncio.get_event_loop()
    queue = asyncio.gather(*[search_drive(drv,input) for drv in azDiscs()])  
    loop.run_until_complete(queue) 