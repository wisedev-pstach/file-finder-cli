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

    command, param = define_command()
    input, insides = get_input()

    if insides:
        print('\033[35m' + f"Start with command to search text inside files - '{input}', as type: {command}" + '\033[0m' )
    else:
        print('\033[35m' + f"Start with command to search fileName for - '{input}', as type: {command}" + '\033[0m' )

 
    match command:
        case SearchOptions.FULL:
            counter = search_full_system(input, insides)
        case SearchOptions.DISC:
            counter = search_disc(input, param, insides)
        case SearchOptions.DIR:
            counter = search_directory(input, param, insides)
        case SearchOptions.CURRENT_DIR:
            counter = search_current_dir(input, insides)

    print('\033[31m' + f"Found {counter} matches." '\033[0m')

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Exited')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)



  