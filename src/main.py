import os
import asyncio
import sys
import nest_asyncio
nest_asyncio.apply()

counter = 0
   
async def search_drive(drv, inp):
    for r, d, f in os.walk(drv): 
        for file in f:
            filepath = os.path.join(r, file)
            if inp in file:
                counter += 1
                print(os.path.join(r, file))


async def main():
    args = sys.argv
    print(args)
    azDiscs = lambda: (chr(i)+":\\" for i in range(ord("A"), ord("Z") + 1))
    inp = input("what")

    loop = asyncio.get_event_loop()
    queue = asyncio.gather(*[search_drive(drv,inp) for drv in azDiscs()])  
    loop.run_until_complete(queue)   
   
    print(f"Found {counter} files.")

asyncio.run(main())