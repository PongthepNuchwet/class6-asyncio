import asyncio
import time


async def example(message):
    """Print a message after the specified delay (in seconds)."""
    print(f"{time.ctime()} - start of :", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of :", message)


async def main():
    # start corotine twice (hopefully they start!)
    first_awatable = example("world")
    secon_awatable = example("Hello")
    # wait for corotines to finish

    await first_awatable
    await secon_awatable

asyncio.run(main())
