import os
import asyncio
import sys
import nest_asyncio
nest_asyncio.apply()

counter = 0

async def search_scope(scope, inp, insides):
    global counter
    for r, d, f in os.walk(scope): 
        for file in f:
            filepath = os.path.join(r, file)
            if not insides and inp in file:
                counter += 1
                print('\033[32m' + filepath + '\033[0m')
            elif insides:
                search_str(filepath, inp)

def search_str(file_path, word):
    try:
        global counter
        with open(file_path, 'r') as file:
            content = file.read()
            if word in content:
                counter +=1
                print('\033[32m' + file_path + '\033[0m')
    except Exception:
        pass

def search_full_system(input, insides):
    azDiscs = lambda: (chr(i)+":\\" for i in range(ord("A"), ord("Z") + 1))
    loop = asyncio.get_event_loop()
    queue = asyncio.gather(*[search_scope(drv,input) for drv in azDiscs()])  
    loop.run_until_complete(queue) 
    return counter

def search_disc(input, disc, insides):
    loop = asyncio.get_event_loop()
    queue = asyncio.gather(*[search_scope(disc,input, insides)])  
    loop.run_until_complete(queue) 
    return counter

def search_current_dir(input, insides):
    loop = asyncio.get_event_loop()
    queue = asyncio.gather(*[search_scope(os.getcwd(), input, insides)])  
    loop.run_until_complete(queue) 
    return counter

def search_directory(input, dir, insides):
    loop = asyncio.get_event_loop()
    queue = asyncio.gather(*[search_scope(dir, input, insides)])
    loop.run_until_complete(queue)
    return counter