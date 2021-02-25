import os
import sys
from contextlib import asynccontextmanager


@asynccontextmanager
async def silent() -> None:
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
