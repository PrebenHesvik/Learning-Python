### Coroutine:
# - Coroutines are computer program components that generalize subroutines for non-preemptive multitasking, by allowing execution to be suspended and resumed.
# - Any function that has `async` in front of it.
# - Inside a function, the `await` keyword is what makes that part of the code run

### Event-loop:
# - In computer science, the event loop is a programming construct or design pattern that waits for and dispatches events or messages in a program.

import asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2

asyncio.run(main())