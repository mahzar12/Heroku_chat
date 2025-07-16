import asyncio

async def simulate_typing(text, delay=1.2):
    await asyncio.sleep(delay)
    return text