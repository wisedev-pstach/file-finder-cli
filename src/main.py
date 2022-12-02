import os
import asyncio
import sys
import nest_asyncio
from command_processor import *
from search_processor import *
nest_asyncio.apply()


async def main():
    counter = 0
    args = sys.argv

    command = define_command()
    input = get_input()
 
    match command:
        case SearchOptions.FULL:
            search_full_system(input)

    print(f"Found {counter} files.")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Exited')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)



  