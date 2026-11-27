import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.job.router import router as job_router
from src.webdav import webdav_server, scratch
from src.constants import PORT, VERSION, WORKERS


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start WebDAV server and restore creds for pre existing jobs
    webdav_server.start()
    scratch.restore()
    yield
    # Now FastAPI handle requests ...


app = FastAPI(title="ada-slurm-manager", version=VERSION, lifespan=lifespan)
app.include_router(job_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=PORT,
        log_config="log.ini",
        workers=WORKERS,
    )
