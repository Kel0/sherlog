import asyncio
import threading


async def do_task(func, message):
    await asyncio.gather(func(message))


def run_in_separated_thread(func, message):
    threads = threading.Thread(target=asyncio.run, args=(do_task(func, message),))
    threads.start()
