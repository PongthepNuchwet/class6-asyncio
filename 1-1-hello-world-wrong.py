import asyncio
import time


async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)."""
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message}")


async def main():
    # start corotine twice (hopefully they start!)
    first_awatable = print_after("world", 2)
    secon_awatable = print_after("Hello", 1)
    # wait for corotines to finish

    await first_awatable
    await secon_awatable

    asyncio.gather([first_awatable, secon_awatable])

asyncio.run(main())
