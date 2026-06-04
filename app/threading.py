import asyncio
from functools import partial
from typing import Callable, Any


async def run_in_thread(func: Callable, *args: Any, **kwargs: Any) -> Any:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, partial(func, *args, **kwargs))