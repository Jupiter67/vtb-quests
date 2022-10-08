from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI
import uvloop


app = FastAPI()


if __name__ == '__main__':
    config = Config()
    config.bind = '0.0.0.0:8000'
    config.accesslog = '-'
    config.errorlog = '-'
    uvloop.install()
    run(serve(app, config))  # type: ignore
